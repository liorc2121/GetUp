from typing import List, Any, Union

list_body_part_mapped: List[Union[str, Any]] = ['SpineBase',
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
                                                 'ThumbRight']

DEFAULT_BASE = 'SpineBase'


POINT_OF_INTREST = ['SpineBase',
                     'Neck',
                     'Head',
                     'ShoulderLeft',
                     'ElbowLeft',
                     'WristLeft',
                     'ShoulderRight',
                     'ElbowRight',
                     'WristRight',
                     'KneeLeft',
                     'AnkleLeft',
                     'FootLeft',
                     'KneeRight',
                     'AnkleRight',
                     'FootRight',
                     'SpineShoulder']


LIST_TRIPLE = [['SpineBase', 'HipLeft', 'HipRight'],
               ['Neck', 'SpineBase', 'Head'],
               ['KneeRight', 'FootRight', 'HipRight'],
               ['KneeLeft', 'AnkleLeft', 'HipLeft'],
               ['SpineBase', 'SpineMid', 'SpineShoulder'],
               ['ElbowRight','WristRight','ShoulderRight'],
               ['ElbowLeft','ShoulderLeft','WristLeft'],
               ['Neck','Head','ShoulderLeft'],
               ['Neck','Head','ShoulderRight']]

class Point:
    def __init__(self,x,y,z,name,file_name = ''):
        self.x = x
        self.y = y
        self.z = z
        self.name = name
        self.file_name = file_name