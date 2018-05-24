import os
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

list_body_part_mapped = ['SpineBase',
                         'SpineMid',
                         'Neck',
                         'Head',
                         'ShoulderLeft',
                         'ElbowLeft',
                         'WristLeft',
                         'HandLeft',
                         'ShoulderRight',
                         'ElbowRight',
                         'WristRight',
                         'HandRight',
                         'HipLeft',
                         'KneeLeft',
                         'AnkleLeft',
                         'FootLeft',
                         'HipRight',
                         'KneeRight',
                         'AnkleRight',
                         'FootRight',
                         'SpineShoulder',
                         'HandTipLeft',
                         'ThumbLeft',
                         'HandTipRight',
                         'ThumbRight'
                         ]


def main():
    path = 'Body'
    body_coordinates_shot = []
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
            body_coordinates['name'] = coordinate[4]
            body_coordinates_shot.append(body_coordinates)
            body_coordinates = {}

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        # plt.ion()

        ax.set_xlim([-1.5, 1.5])
        ax.set_ylim([-1.5, 1.5])
        ax.set_zlim([0, 1.5])

        points = {'x': [], 'y': [], 'z': []}
        names = []

        for point in body_coordinates_shot:
            points['x'].append(float(point['x']))
            points['y'].append(float(point['y']))
            points['z'].append(float(point['z']))
            names += [point['name']]

        ax.scatter(points['x'], points['y'], points['z'])

        for i, text in enumerate(names):
            ax.text(points['x'][i], points['y'][i], points['z'][i], text)

        plt.pause(0.01)

        all_body_coordinates_shots.append(body_coordinates_shot)
        body_coordinates_shot = []
        plt.show()

    print('a')


if __name__ == '__main__':
    main()
