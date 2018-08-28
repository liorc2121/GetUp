import os
from Common.common import *
from Features.features import *
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import glob

RECORDING_PATH = 'D:\Recordings'
FILE_NAME = 'Points'



def print_dots(body_coordinates_shot):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim([0, 520])
    ax.set_ylim([0, 450])
    ax.set_zlim([0, 3000])

    points = {'x': [], 'y': [], 'z': []}
    names = []

    for body in body_coordinates_shot:
        for name in list_body_part_mapped:
            if name in body_coordinates_shot[body].keys():
                point = body_coordinates_shot[body][name]
                points['x'].append(float(point.x))
                points['y'].append(float(point.y))
                points['z'].append(float(point.z))
                names += [point.name]


        ax.scatter(points['x'], points['y'], points['z'])

        for i, text in enumerate(names):
            ax.text(points['x'][i], points['y'][i], points['z'][i], text)

        plt.pause(0.01)
        plt.show()


def read_body_coordinates_from_path(path):
    all_body_coordinates_shots = []
    list = sorted([int(x[6:-4]) for x in os.listdir(path)])


    for file_number in list:
        file_path = path  + '\\' + FILE_NAME +  str(file_number) + '.txt'
        try:
            list = bodies_coordinates_from_file(file_path)
            all_body_coordinates_shots.append(list)
        except:
            print(file_path + ' ' + 'cannot be read')

    return all_body_coordinates_shots


def bodies_coordinates_from_file(file_path):
    s = open(file_path)
    lines = s.readlines()
    index = ''
    list_all_bodies = {}

    for line in lines:
        if line.replace('\n','').replace(' ','').replace('\t','') != '':
            if line.replace('\n', '')[0:4] == 'body':
                index = line.replace('\n', '')
                list_all_bodies[index] = {}

            else:

                    coordinate = line.split('#')
                    point = Point(int(coordinate[0]),
                                  int(coordinate[1]),
                                  int(coordinate[2]),
                                  coordinate[3].replace('\n', ''),
                                  os.path.splitext(os.path.basename(file_path))[0])
                    list_all_bodies[index][coordinate[3].replace('\n', '')] = point


    return list_all_bodies




def main():
    feature_vector = []
    label_vector = []

    sub_directory = os.walk(RECORDING_PATH)
    for rec in sub_directory:
        for sub_b in rec[1]:
            try:
                if rec[0] == RECORDING_PATH:
                    #print(sub_b)
                    points_path = RECORDING_PATH + '\\' + sub_b + '\\Points'
                    if points_path == '' or os.path.exists(points_path):
                        print(points_path)
                        all_body_coordinates = read_body_coordinates_from_path(points_path)
                        #for x in all_body_coordinates:
                         #   print_dots(x)


                        fa = Features(all_body_coordinates)
                        f = fa.get_vector()
                        print(len(f))

                        '''
                        if int(sub_b) > 66:
                            label_vector.append(1)
                            feature_vector.append(f)
                        elif int(sub_b) < 38:
                            label_vector.append(0)
                            feature_vector.append(f)
                            '''
            except Exception as e:
                print(e)




if __name__ == '__main__':
    main()
