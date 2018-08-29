from Common.common import *
import numpy as np

VAR_HEAD_START_Z = 15

# the angle is BAC
def calc_angle(A, B, C):
    AB_vec = np.array([B.x - A.x, B.y - A.y, B.z - A.z])
    AC_vec =  np.array([C.x - A.x, C.y - A.y, C.z - A.z])
    dot_ABC = np.dot(AB_vec, AC_vec)
    len_ABC = np.linalg.norm(AB_vec) * np.linalg.norm(AC_vec)
    a = np.arccos((dot_ABC / len_ABC))
    return a


class Features:
    def __init__(self, all_body_coordinates):
        self.all_body_coordinates = all_body_coordinates
        self.all_normal_coordinates = self.normal_coordinates(all_body_coordinates)
        self.persons_involved = set()
        self.feature_vector = []
        self.features_names = []

    def get_vector(self):
        self.total_frames()
        self.time_to_get_up()
        self.get_variance_mean_max_min()
        self.get_max_people_on_frame()
        self.number_of_diffrent_people()
        self.get_degree_features()
        return self.feature_vector, self.features_names

    def check_sitting_body(self,first_bodies_coordinates_shot):
            max_spine_y = 0
            sitting_body = None
            for body in first_bodies_coordinates_shot.keys():
                point_spine = first_bodies_coordinates_shot[body][DEFAULT_BASE]
                if point_spine.y > max_spine_y:
                    max_spine_y = point_spine.y
                    sitting_body = body

            return sitting_body

    def normal_coordinates(self, all_bodies_coordinates):
        all_normal = []
        sitting_body = self.check_sitting_body(self.all_body_coordinates[0])
        old_spine = Point(0,0,0,DEFAULT_BASE)
        for bodies_coordinates_shot in all_bodies_coordinates:
            normal_bodies_shot = {}
            for body in bodies_coordinates_shot.keys():
                body_coordinates_shot = bodies_coordinates_shot[body]

                try:
                    spine_base = bodies_coordinates_shot[sitting_body][DEFAULT_BASE]
                except:
                    spine_base = old_spine

                old_spine = spine_base

                normal_ = {}
                for key in body_coordinates_shot.keys():
                    normal_coordinates = {}
                    normal_point = Point(body_coordinates_shot[key].x - spine_base.x,
                                         body_coordinates_shot[key].y - spine_base.y,
                                         body_coordinates_shot[key].z - spine_base.z,
                                         key)
                    
                    normal_[key] = normal_point
                normal_bodies_shot[body]= normal_

                all_normal.append(normal_bodies_shot)
        return all_normal

    def time_to_get_up(self):
        sitting_body = self.check_sitting_body(self.all_body_coordinates[0])
        head_start_pos = self.all_body_coordinates[0][sitting_body]['Head']
        start_frame = -1
        for i in range(len(self.all_body_coordinates)):
            cur_head_point = self.all_body_coordinates[i][sitting_body]['Head']
            if abs(cur_head_point.z -head_start_pos.z) > VAR_HEAD_START_Z:
                start_frame = i
                break

        self.feature_vector.append(len(self.all_body_coordinates) - start_frame)
        return len(self.all_body_coordinates) - start_frame

    def total_frames(self):
        self.feature_vector.append(len(self.all_body_coordinates))
        return len(self.all_body_coordinates)

    def get_variance_mean_max_min(self):
        sitting_body = self.check_sitting_body(self.all_body_coordinates[0])

        for name in POINT_OF_INTREST:

            positions_x = np.array([body_coordinate[sitting_body][name].x if name in body_coordinate[sitting_body].keys() else 0 for body_coordinate in self.all_normal_coordinates])
            positions_y = np.array([body_coordinate[sitting_body][name].y if name in body_coordinate[sitting_body].keys() else 0 for body_coordinate in self.all_normal_coordinates])
            positions_z = np.array([body_coordinate[sitting_body][name].z if name in body_coordinate[sitting_body].keys() else 0 for body_coordinate in self.all_normal_coordinates])


            self.feature_vector.append(positions_x.var())
            self.feature_vector.append(positions_y.var())
            self.feature_vector.append(positions_z.var())
            self.feature_vector.append(positions_x.mean())
            self.feature_vector.append(positions_y.mean())
            self.feature_vector.append(positions_z.mean())
            self.feature_vector.append(positions_x.max())
            self.feature_vector.append(positions_y.max())
            self.feature_vector.append(positions_z.max())
            self.feature_vector.append(positions_x.min())
            self.feature_vector.append(positions_y.min())
            self.feature_vector.append(positions_z.min())

            self.features_names.append(name + ' x var')
            self.features_names.append(name + ' y var')
            self.features_names.append(name + ' z var')
            self.features_names.append(name + ' x mean')
            self.features_names.append(name + ' y mean')
            self.features_names.append(name + ' z mean')
            self.features_names.append(name + ' x max')
            self.features_names.append(name + ' y max')
            self.features_names.append(name + ' z max')
            self.features_names.append(name + ' x min')
            self.features_names.append(name + ' y min')
            self.features_names.append(name + ' z min')

        return []

    def get_degree(self,name1,name2,name3):
        sitting_body = self.check_sitting_body(self.all_body_coordinates[0])

        try:

            points_a =  np.array([body_coordinate[sitting_body][name1] for body_coordinate in self.all_normal_coordinates])
            points_b = np.array([body_coordinate[sitting_body][name2] for body_coordinate in self.all_normal_coordinates])
            points_c = np.array([body_coordinate[sitting_body][name3] for body_coordinate in self.all_normal_coordinates])

            points_degree = np.array([calc_angle(points_a[i],points_b[i],points_c[i]) for i in range(len(points_a))])
            self.feature_vector.append(points_degree.max())
            self.feature_vector.append(points_degree.var())
            self.feature_vector.append(points_degree.mean())
            self.feature_vector.append(points_degree.std())

        except:
            self.feature_vector.append(0)
            self.feature_vector.append(0)
            self.feature_vector.append(0)
            self.feature_vector.append(0)

        self.features_names.append(name1 + ' ' + name2 + ' ' + name3 + ' degree max')
        self.features_names.append(name1 + ' ' + name2 + ' ' + name3 + ' degree var')
        self.features_names.append(name1 + ' ' + name2 + ' ' + name3 + ' degree mean')
        self.features_names.append(name1 + ' ' + name2 + ' ' + name3 + ' degree std')

    def get_max_people_on_frame(self):
        self.feature_vector.append(max([len(shot) for shot in self.all_body_coordinates]))
        self.features_names.append('max_people_on_frame')

    def number_of_diffrent_people(self):
        for shot in self.all_body_coordinates:
            for body in shot.keys():
                self.persons_involved.add(body)

        self.feature_vector.append(len(self.persons_involved))
        self.features_names.append('number_of_diffrent_people')
        return len(self.persons_involved)

    def get_degree_features(self):
        for triple in LIST_TRIPLE:
            self.get_degree(triple[0],triple[1],triple[2])