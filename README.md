# GetUp
GetUp Project - 3D Photography


# problem definition 
Given stream of pictures from kinect of person get up from the chair,
Need to understand if the person will suffer from Loss of balance.

# Input:
Get the Data:
Build a picture Enrollment with the library of pyKinect2 and get the 3D map of 24 points in every frame
the camera save the Data


How it works:





# Analyze the Data:
Features: 
points of interest:
max on How many people in the frame.
how many different people 
total of frames per record
the number of frames its took the person to get up
list of 15 points of interest points: body parts are used to get up, for each point we take: var, min, max on all 3D coordinates
list of 15 triple and takes the angle betweens the three points for each angle we take: var,min,max,std

  


# Label System:

after discussion with the hospital's physiotherapist we get 5 different labels for each get up.
4 - no problem
3 - slightly used his arm to get up
2 - massive used his arm to get up
1 - got minor outside help
0 - got massive outside help

1 - main labels - hospital diversion - no change
2 - chunk labels -  3 chunck:
	            0,1 - help use, 
		    2.3 - arm use
		    4   - no problem
3 - binary labels - 4 - healthy
		    0+1+2+3 -not healthy

# Classifiers
KNN - k nearest neighbor
SVM - support vector machine
DecisionTree - decision tree

# Result:
main label (baseline- 0.2):
SVM - 0.305
KNN - 0.301
DecisionTree- 0.71  

chunk label (baseline- 0.33):
SVM - 0.567
KNN - 0.517
DecisionTree- 0.69

binary label (baseline- 0.5):
SVM - 0.697
KNN - 0.746
DecisionTree- 0.687
