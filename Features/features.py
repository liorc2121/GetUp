from Common.common import *
import numpy as np

class Features:
    def __init__(self, body_coordinates):
        self.all_body_coordinates = body_coordinates
        self.all_normal_coordinates = self.normal_coordinates(body_coordinates)
        self.feature_vector = []

    def get_vector(self):
        self.total_time()
        self.time_to_get_up()
        self.get_variance_mean_max_min
        return self.feature_vector

    def normal_coordinates(self, all_body_coordinates):
        all_normal = []
        for body_coordinates_shot in all_body_coordinates:
            spin_base = body_coordinates_shot[default_base]
            normal_ = {}
            for key in body_coordinates_shot.keys():
                normal_coordinates = {}
                normal_coordinates['x'] = float(body_coordinates_shot[key]['x']) - float(spin_base['x'])
                normal_coordinates['y'] = float(body_coordinates_shot[key]['y']) - float(spin_base['y'])
                normal_coordinates['z'] = float(body_coordinates_shot[key]['z']) - float(spin_base['z'])
                normal_coordinates['score'] = body_coordinates_shot[key]['score']
                normal_coordinates['name'] = body_coordinates_shot[key]['name']
                normal_[normal_coordinates['name']] = normal_coordinates
            all_normal.append(normal_)
        return all_normal

    def time_to_get_up(self):
        for x in self.all_normal_coordinates:
            a = 3
        head_positions = [x['Head']['y'] for x in self.all_normal_coordinates]
        max_l = head_positions.index(max(head_positions))
        min_l = head_positions.index(min(head_positions))
        self.feature_vector.append(max_l - min_l)
        return max_l - min_l

    def total_time(self):
        self.feature_vector.append(len(self.all_normal_coordinates))
        return len(self.all_normal_coordinates)

    @property
    def get_variance_mean_max_min(self):
        all_var_x = []
        for name in list_body_part_mapped:
            positions_x = np.array([body_coordinate[name]['x'] for body_coordinate in self.all_normal_coordinates])
            positions_y = np.array([body_coordinate[name]['y'] for body_coordinate in self.all_normal_coordinates])
            positions_z = np.array([body_coordinate[name]['z'] for body_coordinate in self.all_normal_coordinates])
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

        return []

    def get_degree(self):
        for body_coordinates in self.all_body_coordinates:
            spine_base = body_coordinates['SpineBase']
            spine_base = body_coordinates['']
            spine_base = body_coordinates['']

