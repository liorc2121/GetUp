import os
import matplotlib.pyplot as plt
from Common.common import *
from Features.features import *
from classifier.classifier import  *
import random

def print_dots(body_coordinates_shot):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([0, 1.5])

    points = {'x': [], 'y': [], 'z': []}
    names = []

    for name in list_body_part_mapped:
        point = body_coordinates_shot[name]
        points['x'].append(float(point['x']))
        points['y'].append(float(point['y']))
        points['z'].append(float(point['z']))
        names += [point['name']]

    ax.scatter(points['x'], points['y'], points['z'])

    for i, text in enumerate(names):
        ax.text(points['x'][i], points['y'][i], points['z'][i], text)

    plt.pause(0.01)
    plt.show()


def read_body_coordinates_from_path(path):
    body_coordinates_shot = {}
    all_body_coordinates_shots = []
    body_coordinates = {}

    for body_coordinate_text in os.listdir(path):
        s = open(path + '\\' + body_coordinate_text)
        lines = s.readlines()
        for line in lines:
            coordinate = line.split('#')
            body_coordinates['x'] = coordinate[0]
            body_coordinates['y'] = coordinate[1]
            body_coordinates['z'] = coordinate[2]
            body_coordinates['score'] = coordinate[3]
            body_coordinates['name'] = coordinate[4].replace('\n', '')
            body_coordinates_shot[body_coordinates['name']] = body_coordinates
            body_coordinates = {}

        #        print_dots(body_coordinates_shot)
        all_body_coordinates_shots.append(body_coordinates_shot)
        body_coordinates_shot = {}

    return all_body_coordinates_shots




def main():
    path = 'C:\\Users\\Lior\\Documents\\GitHub\\GetUp\\\Recording'
    feature_vector = []
    label_vector = []

    sub_directory = os.walk(path)
    for rec in sub_directory:
        for sub_b in rec[1]:
            try:
                all_body_coordinates = read_body_coordinates_from_path(path + '\\' + sub_b + '\\Body')
                fa = Features(all_body_coordinates)
                f = fa.get_vector()
                if int(sub_b) > 66:
                    label_vector.append(1)
                    feature_vector.append(f)

                elif int(sub_b) < 38:
                    label_vector.append(0)
                    feature_vector.append(f)

            except:
                a =3

    ClassifierFactory().fit_all(feature_vector,label_vector, 5)




if __name__ == '__main__':
    main()
