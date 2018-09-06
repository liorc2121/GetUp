# GetUp
GetUp Project - 3D Photography

Report


problem definition 
Given stream of pictures from kinect of person get up from the chair,
Need to understand if the person will suffer from Loss of balance.

Input:
Get the Data:
Build a picture Enrollment with the library of pyKinect2 and get the 3D map of 24 points in every frame
the camera save the Data



How it works:













Analyze the Data:
Normalize the data by defines the spineBase to be the First of the contractions,
And then create features vectors from the normal vectors points.

Features: 
points of interest:
max on How many people in the frame.

how many different people 
total of frames per record
the number of frames its took the person to get up
list of 15 points of interest points: body parts are used to get up, for each point we take: var, min, max on all 3D coordinates
list of 15 triple and takes the angle betweens the three points for each angle we take: var,min,max,std
  


Label System:

after discussion with the hospital's physiotherapist we get 5 different labels for each get up.
4 - no problem
3 - slightly used his arm to get up
2 - massive used his arm to get up
1 - got minor outside help
0 - got massive outside help


i used 3 different label system:
1 - main labels - hospital חלוקה  - no change
2 - chunk labels -  0+1, 2+3,4 basically category of helps: no problem,arm use, outside help
3 - binary labels - 4,0+1+2+3 - healthy/ not health









output:
3 text file of result:
<your output file name>_main_labels.txt 
<your output file name>_chunck_labels.txt
<your output file name>_binary_labels.txt

Result:  


Main Label
SVM
Decision Tree
KNN
baseline
0.2
0.2
0.2
all-features
0.305
0.71
0.301
Best 10 features
0.33
0.674
0.307
Best 20 features
0.33
0.702
0.374
Best 30 features
0.33
0.724
0.424
Best 50 features
0.33
0.715
0.426
	

Binary Label
SVM
Decision Tree
KNN
baseline
0.5
0.5
0.627
all-features
0.697
0.746
0.687
Best 10 features
0.697
0.846
0.717
Best 20 features
0.697
0.739
0.734
Best 30 features
0.697
0.743
0.734
Best 50 features
0.697
0.766
0.732


Chunk Label
SVM
Decision Tree
KNN
baseline
0.33
0.33
0.33
all-features
0.567
0.69
0.517
Best 10 features
0.567
0.83
0.619
Best 20 features
0.567
0.805
0.726
Best 30 features
0.567
0.733
0.681
Best 50 features
0.567
0.726
0.674


List Of Best Features And Conclusion: 

SVM,KNN-  the difficulties to separate between each mains (between the "chunk class") after the change the label system increase the accuracy as expected
Decision Tree -  gives the best results.

Best 20 features:

max_people_on_frame
Neck y var
ElbowLeft z min
WristLeft x var
WristLeft y max
ShoulderRight x var
ShoulderRight z min
ElbowRight z var
ElbowRight x max
ElbowRight z max
WristRight x var
WristRight z mean
WristRight z max
WristRight x min
KneeLeft x mean
AnkleLeft x mean
KneeRight x mean
AnkleRight x mean
Neck SpineBase Head degree std
KneeRight FootRight HipRight degree var
Far more pictures of right-handed people than left-handed therefore more use of the right upper body and left body and this have been seen by the best features.
Max_people_on_frame - differents automatically between health and unhealthy, and even between chunks.
Neck SpineBase Head degree std - the degree of the spine is good feature because we can see the move back and forward of the people to get up.
