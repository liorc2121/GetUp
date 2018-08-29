import os
from Common.common import *
from Features.features import *
import matplotlib.pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
import glob
import sys
import random
from Labeling.labeling import *
from classifier.classifier import  ClassifierFactory

#C:\\Users\\Lior\\Documents\\GitHub\\GetUp\\
RECORDING_PATH = 'Data'
#RECORDING_PATH = 'C:\\Users\\Lior\\Documents\\GitHub\\GetUp\\Data'
FILE_NAME = 'Points'
LABELING = [0,1,2,3,4]


def shuffle_2_list(A,B):
    if len(A) != len(B):
        raise Exception("Lengths don't match")
    indexes = [i for i in range(len(A))]
    random.shuffle(indexes)
    A_shuffled = [A[i] for i in indexes]
    B_shuffled = [B[i] for i in indexes]
    return A_shuffled, B_shuffled


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


def create_features_labels_from_file(path):
    feature_vector = []
    label_vector = []
    for dir in os.walk(RECORDING_PATH):
        for sub_folder in dir[1]:
            try:
                if dir[0] == RECORDING_PATH:
                    label = int(sub_folder)
                    sub_directory = RECORDING_PATH + '\\' + sub_folder
                    for rec in os.walk(sub_directory):
                        for points_folder in rec[1]:
                            if rec[0] == sub_directory:
                                points_path = sub_directory + '\\' + points_folder + '\\Points'
                                if points_path == '' or os.path.exists(points_path):
                                    all_body_coordinates = read_body_coordinates_from_path(points_path)
                                    fa = Features(all_body_coordinates)
                                    f,f_names = fa.get_vector()
                                    feature_vector.append(f)
                                    label_vector.append(label)
            except Exception as e:
                print(e)

    return feature_vector, f_names, label_vector



def main():
    features, scores = create_features_labels_from_file(RECORDING_PATH)
    shuffle_feature,shuffle_scores = shuffle_2_list(features,scores)
    all_labels, labels_names = LabelFactory().all_labels_system(shuffle_scores)

    for i in range(len(all_labels)):
        print(labels_names[i])
        ClassifierFactory().fit_all(shuffle_feature,all_labels[i], 5)







if __name__ == '__main__':
    main()
