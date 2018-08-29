from Common.common import *


def binary_labels(scores):
    return [1 if score == 4 else 0 for score in scores]


def chunck_labels(scores):
    chunck_score = []
    for score in scores:
        if score in [2, 3]:
            chunck_score.append(2)
        elif score in [0, 1]:
            chunck_score.append(1)
        else:
            chunck_score.append(score)

    return chunck_score


def main_labels(scores):
    return scores


class LabelFactory:
    def all_labels_system(self, scores):
        names_labels = ['main_labels','chunck_labels','binary_labels']
        all_labels = [main_labels(scores), chunck_labels(scores), binary_labels(scores)]
        return all_labels, names_labels

