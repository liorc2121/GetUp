function  analayzeData(dirName)
hipLeft = [0 0 0];
hipRight = [0 0 0];
KneeLeft= [0 0 0];
KneeRight= [0 0 0];
AnkleLeft= [0 0 0];
AnkleRight= [0 0 0];
FootLeft= [0 0 0];
FootRight= [0 0 0];
SpineShoulder = [0 0 0];
tmpName  = strcat(dirName,'\Body\');
txtName = strcat(tmpName,'*.TXT');
files = dir(txtName);
for file = files'
    
    fname = strcat(tmpName,file.name);
    fid = fopen(fname);
    A = textscan(fid,'%f %f %f %f %s','Delimiter','#');
    x = A{:,1};
    y = A{:,2};
    z = A{:,3};
    hipLeft = [hipLeft;x(13) y(13) z(13)];
    KneeLeft = [KneeLeft;x(14) y(14) z(14)];
    AnkleLeft = [AnkleLeft;x(15) y(15) z(15)];
    FootLeft= [FootLeft;x(16) y(16) z(16)];
    hipRight = [hipRight;x(17) y(17) z(17)];
    KneeRight = [KneeRight;x(18) y(18) z(18)];
    AnkleRight = [AnkleRight;x(19) y(19) z(19)]; 
    FootRight = [FootRight;x(20) y(20) z(20)]; 
    SpineShoulder = [SpineShoulder;x(21) y(21) z(21)];
        fclose(fid);

   % csv = load(file.name);
    % Do some stuff
end
% open file to write results  
resName = strcat(dirName,'\results.txt');
res = fopen( resName, 'wt' );


%write max x for left hip
fprintf( res, 'MAX X coordinate for Left Hip: ');
fprintf(res,'%f\n',max(hipLeft(2:end,1)));
%write min x for left hip
fprintf( res, 'MIN X coordinate for Left Hip: ');
fprintf(res,'%f\n',min(hipLeft(2:end,1)));
%write mean x for left hip
fprintf( res, 'Mean X coordinate for Left Hip: ');
fprintf(res,'%f\n',mean(hipLeft(2:end,1)));
%write Var x for left hip
fprintf( res, 'Variance X coordinate for Left Hip: ');
fprintf(res,'%f\n',var(hipLeft(2:end,1)));



%write max y for left hip
fprintf( res, 'MAX Y coordinate for Left Hip: ');
fprintf(res,'%f\n',max(hipLeft(2:end,2)));
%write min y for left hip
fprintf( res, 'MIN Y coordinate for Left Hip: ');
fprintf(res,'%f\n',min(hipLeft(2:end,2)));
%write mean y for left hip
fprintf( res, 'Mean Y coordinate for Left Hip: ');
fprintf(res,'%f\n',mean(hipLeft(2:end,2)));
%write Var y for left hip
fprintf( res, 'Variance Y coordinate for Left Hip: ');
fprintf(res,'%f\n',var(hipLeft(2:end,2)));

%write max z for left hip
fprintf( res, 'MAX Z coordinate for Left Hip: ');
fprintf(res,'%f\n',max(hipLeft(2:end,3)));
%write min z for left hip
fprintf( res, 'MIN Z coordinate for Left Hip: ');
fprintf(res,'%f\n',min(hipLeft(2:end,3)));
%write mean z for left hip
fprintf( res, 'Mean Z coordinate for Left Hip: ');
fprintf(res,'%f\n',mean(hipLeft(2:end,3)));
%write Var z for left hip
fprintf( res, 'Variance Z coordinate for Left Hip: ');
fprintf(res,'%f\n',var(hipLeft(2:end,3)));



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for right hip
fprintf( res, 'MAX X coordinate for Right Hip: ');
fprintf(res,'%f\n',max(hipRight(2:end,1)));
%write min x for right hip
fprintf( res, 'MIN X coordinate for Right Hip: ');
fprintf(res,'%f\n',min(hipRight(2:end,1)));
%write mean x for right hip
fprintf( res, 'Mean X coordinate for Right Hip: ');
fprintf(res,'%f\n',mean(hipRight(2:end,1)));
%write Var x for right hip
fprintf( res, 'Variance X coordinate for Right Hip: ');
fprintf(res,'%f\n',var(hipRight(2:end,1)));



%write max y for right hip
fprintf( res, 'MAX Y coordinate for Right Hip: ');
fprintf(res,'%f\n',max(hipRight(2:end,2)));
%write min y for right hip
fprintf( res, 'MIN Y coordinate for Right Hip: ');
fprintf(res,'%f\n',min(hipRight(2:end,2)));
%write mean y for right hip
fprintf( res, 'Mean Y coordinate for Right Hip: ');
fprintf(res,'%f\n',mean(hipRight(2:end,2)));
%write Var y for right hip
fprintf( res, 'Variance Y coordinate for Right Hip: ');
fprintf(res,'%f\n',var(hipRight(2:end,2)));

%write max z for right hip
fprintf( res, 'MAX Z coordinate for Right Hip: ');
fprintf(res,'%f\n',max(hipRight(2:end,3)));
%write min z for right hip
fprintf( res, 'MIN Z coordinate for Right Hip: ');
fprintf(res,'%f\n',min(hipRight(2:end,3)));
%write mean z for right hip
fprintf( res, 'Mean Z coordinate for Right Hip: ');
fprintf(res,'%f\n',mean(hipRight(2:end,3)));
%write Var z for right hip
fprintf( res, 'Variance Z coordinate for Right Hip: ');
fprintf(res,'%f\n',var(hipRight(2:end,3)));
[x] = eig(hipRight(2:end,1),'vector');
plot(x)


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for Left Knee
fprintf( res, 'MAX X coordinate for Left Knee: ');
fprintf(res,'%f\n',max(KneeLeft(2:end,1)));
%write min x for Left Knee
fprintf( res, 'MIN X coordinate for Left Knee: ');
fprintf(res,'%f\n',min(KneeLeft(2:end,1)));
%write mean x for Left Knee
fprintf( res, 'Mean X coordinate for Left Knee: ');
fprintf(res,'%f\n',mean(KneeLeft(2:end,1)));
%write Var x for Left Knee
fprintf( res, 'Variance X coordinate for Left Knee: ');
fprintf(res,'%f\n',var(KneeLeft(2:end,1)));



%write max y for Left Knee
fprintf( res, 'MAX Y coordinate for Left Knee: ');
fprintf(res,'%f\n',max(KneeLeft(2:end,2)));
%write min y for Left Knee
fprintf( res, 'MIN Y coordinate for Left Knee: ');
fprintf(res,'%f\n',min(KneeLeft(2:end,2)));
%write mean y for Left Knee
fprintf( res, 'Mean Y coordinate for Left Knee: ');
fprintf(res,'%f\n',mean(KneeLeft(2:end,2)));
%write Var y for rLeft Knee
fprintf( res, 'Variance Y coordinate for Left Knee: ');
fprintf(res,'%f\n',var(KneeLeft(2:end,2)));

%write max z for Left Knee
fprintf( res, 'MAX Z coordinate for Left Knee: ');
fprintf(res,'%f\n',max(KneeLeft(2:end,3)));
%write min z for Left Knee
fprintf( res, 'MIN Z coordinate for Left Knee: ');
fprintf(res,'%f\n',min(KneeLeft(2:end,3)));
%write mean z for Left Knee
fprintf( res, 'Mean Z coordinate for Left Knee: ');
fprintf(res,'%f\n',mean(KneeLeft(2:end,3)));
%write Var z for Left Knee
fprintf( res, 'Variance Z coordinate for Left Knee: ');
fprintf(res,'%f\n',var(KneeLeft(2:end,3)));



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for right hip
fprintf( res, 'MAX X coordinate for Right Hip: ');
fprintf(res,'%f\n',max(hipRight(2:end,1)));
%write min x for right hip
fprintf( res, 'MIN X coordinate for Right Hip: ');
fprintf(res,'%f\n',min(hipRight(2:end,1)));
%write mean x for right hip
fprintf( res, 'Mean X coordinate for Right Hip: ');
fprintf(res,'%f\n',mean(hipRight(2:end,1)));
%write Var x for right hip
fprintf( res, 'Variance X coordinate for Right Hip: ');
fprintf(res,'%f\n',var(hipRight(2:end,1)));



%write max y for right hip
fprintf( res, 'MAX Y coordinate for Right Hip: ');
fprintf(res,'%f\n',max(hipRight(2:end,2)));
%write min y for right hip
fprintf( res, 'MIN Y coordinate for Right Hip: ');
fprintf(res,'%f\n',min(hipRight(2:end,2)));
%write mean y for right hip
fprintf( res, 'Mean Y coordinate for Right Hip: ');
fprintf(res,'%f\n',mean(hipRight(2:end,2)));
%write Var y for right hip
fprintf( res, 'Variance Y coordinate for Right Hip: ');
fprintf(res,'%f\n',var(hipRight(2:end,2)));

%write max z for right hip
fprintf( res, 'MAX Z coordinate for Right Hip: ');
fprintf(res,'%f\n',max(hipRight(2:end,3)));
%write min z for right hip
fprintf( res, 'MIN Z coordinate for Right Hip: ');
fprintf(res,'%f\n',min(hipRight(2:end,3)));
%write mean z for right hip
fprintf( res, 'Mean Z coordinate for Right Hip: ');
fprintf(res,'%f\n',mean(hipRight(2:end,3)));
%write Var z for right hip
fprintf( res, 'Variance Z coordinate for Right Hip: ');
fprintf(res,'%f\n',var(hipRight(2:end,3)));



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for Left Knee
fprintf( res, 'MAX X coordinate for Left Knee: ');
fprintf(res,'%f\n',max(KneeLeft(2:end,1)));
%write min x for Left Knee
fprintf( res, 'MIN X coordinate for Left Knee: ');
fprintf(res,'%f\n',min(KneeLeft(2:end,1)));
%write mean x for Left Knee
fprintf( res, 'Mean X coordinate for Left Knee: ');
fprintf(res,'%f\n',mean(KneeLeft(2:end,1)));
%write Var x for Left Knee
fprintf( res, 'Variance X coordinate for Left Knee: ');
fprintf(res,'%f\n',var(KneeLeft(2:end,1)));



%write max y for Left Knee
fprintf( res, 'MAX Y coordinate for Left Knee: ');
fprintf(res,'%f\n',max(KneeLeft(2:end,2)));
%write min y for Left Knee
fprintf( res, 'MIN Y coordinate for Left Knee: ');
fprintf(res,'%f\n',min(KneeLeft(2:end,2)));
%write mean y for Left Knee
fprintf( res, 'Mean Y coordinate for Left Knee: ');
fprintf(res,'%f\n',mean(KneeLeft(2:end,2)));
%write Var y for rLeft Knee
fprintf( res, 'Variance Y coordinate for Left Knee: ');
fprintf(res,'%f\n',var(KneeLeft(2:end,2)));

%write max z for Left Knee
fprintf( res, 'MAX Z coordinate for Left Knee: ');
fprintf(res,'%f\n',max(KneeLeft(2:end,3)));
%write min z for Left Knee
fprintf( res, 'MIN Z coordinate for Left Knee: ');
fprintf(res,'%f\n',min(KneeLeft(2:end,3)));
%write mean z for Left Knee
fprintf( res, 'Mean Z coordinate for Left Knee: ');
fprintf(res,'%f\n',mean(KneeLeft(2:end,3)));
%write Var z for Left Knee
fprintf( res, 'Variance Z coordinate for Left Knee: ');
fprintf(res,'%f\n',var(KneeLeft(2:end,3)));


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for Right Knee
fprintf( res, 'MAX X coordinate for Right Knee: ');
fprintf(res,'%f\n',max(KneeRight(2:end,1)));
%write min x for Right Knee
fprintf( res, 'MIN X coordinate for Right Knee: ');
fprintf(res,'%f\n',min(KneeRight(2:end,1)));
%write mean x for Right Knee
fprintf( res, 'Mean X coordinate for Right Knee: ');
fprintf(res,'%f\n',mean(KneeRight(2:end,1)));
%write Var x for Right Knee
fprintf( res, 'Variance X coordinate for Right Knee: ');
fprintf(res,'%f\n',var(KneeRight(2:end,1)));



%write max y for Right Knee
fprintf( res, 'MAX Y coordinate for Right Knee: ');
fprintf(res,'%f\n',max(KneeRight(2:end,2)));
%write min y for Right Knee
fprintf( res, 'MIN Y coordinate for Right Knee: ');
fprintf(res,'%f\n',min(KneeRight(2:end,2)));
%write mean y for Right Knee
fprintf( res, 'Mean Y coordinate for Right Knee: ');
fprintf(res,'%f\n',mean(KneeRight(2:end,2)));
%write Var y for Right Knee
fprintf( res, 'Variance Y coordinate for Right Knee: ');
fprintf(res,'%f\n',var(KneeRight(2:end,2)));

%write max z for Right Knee
fprintf( res, 'MAX Z coordinate for Right Knee: ');
fprintf(res,'%f\n',max(KneeRight(2:end,3)));
%write min z for Right Knee
fprintf( res, 'MIN Z coordinate for Right Knee: ');
fprintf(res,'%f\n',min(KneeRight(2:end,3)));
%write mean z for Right Knee
fprintf( res, 'Mean Z coordinate for Right Knee: ');
fprintf(res,'%f\n',mean(KneeRight(2:end,3)));
%write Var z for Right Knee
fprintf( res, 'Variance Z coordinate for Right Knee: ');
fprintf(res,'%f\n',var(KneeRight(2:end,3)));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for Left Foot
fprintf( res, 'MAX X coordinate for Left Foot: ');
fprintf(res,'%f\n',max(FootLeft(2:end,1)));
%write min x for Left Foot
fprintf( res, 'MIN X coordinate for Left Foot: ');
fprintf(res,'%f\n',min(FootLeft(2:end,1)));
%write mean x for Left Foot
fprintf( res, 'Mean X coordinate for Left Foot: ');
fprintf(res,'%f\n',mean(FootLeft(2:end,1)));
%write Var x for Left Foot
fprintf( res, 'Variance X coordinate for Left Foot: ');
fprintf(res,'%f\n',var(FootLeft(2:end,1)));



%write max y for Left Foot
fprintf( res, 'MAX Y coordinate for Left Foot: ');
fprintf(res,'%f\n',max(FootLeft(2:end,2)));
%write min y for Left Foot
fprintf( res, 'MIN Y coordinate for Left Foot: ');
fprintf(res,'%f\n',min(FootLeft(2:end,2)));
%write mean y for Left Foot
fprintf( res, 'Mean Y coordinate for Left Foot: ');
fprintf(res,'%f\n',mean(FootLeft(2:end,2)));
%write Var y for Left Foot
fprintf( res, 'Variance Y coordinate for Left Foot: ');
fprintf(res,'%f\n',var(FootLeft(2:end,2)));

%write max z for Left Foot
fprintf( res, 'MAX Z coordinate for Left Foot: ');
fprintf(res,'%f\n',max(FootLeft(2:end,3)));
%write min z for Left Foot
fprintf( res, 'MIN Z coordinate for Left Foot ');
fprintf(res,'%f\n',min(FootLeft(2:end,3)));
%write mean z for Left Foot
fprintf( res, 'Mean Z coordinate for Left Foot: ');
fprintf(res,'%f\n',mean(FootLeft(2:end,3)));
%write Var z for Left Foot
fprintf( res, 'Variance Z coordinate for Left Foot: ');
fprintf(res,'%f\n',var(FootLeft(2:end,3)));


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for Right Foot
fprintf( res, 'MAX X coordinate for Right Foot: ');
fprintf(res,'%f\n',max(FootRight(2:end,1)));
%write min x for Right Foot
fprintf( res, 'MIN X coordinate for Right Foot: ');
fprintf(res,'%f\n',min(FootRight(2:end,1)));
%write mean x for Right Foot
fprintf( res, 'Mean X coordinate for Right Foot: ');
fprintf(res,'%f\n',mean(FootRight(2:end,1)));
%write Var x for Right Foot
fprintf( res, 'Variance X coordinate for Right Foot: ');
fprintf(res,'%f\n',var(FootRight(2:end,1)));



%write max y for Right Foot
fprintf( res, 'MAX Y coordinate for Right Foot: ');
fprintf(res,'%f\n',max(FootRight(2:end,2)));
%write min y for Right Foot
fprintf( res, 'MIN Y coordinate for Right Foot: ');
fprintf(res,'%f\n',min(FootRight(2:end,2)));
%write mean y for Right Foot
fprintf( res, 'Mean Y coordinate for Right Foot: ');
fprintf(res,'%f\n',mean(FootRight(2:end,2)));
%write Var y for Right Foot
fprintf( res, 'Variance Y coordinate for Right Foot: ');
fprintf(res,'%f\n',var(FootRight(2:end,2)));

%write max z for Right Foot
fprintf( res, 'MAX Z coordinate for Right Foot: ');
fprintf(res,'%f\n',max(FootRight(2:end,3)));
%write min z for Right Foot
fprintf( res, 'MIN Z coordinate for Right Foot ');
fprintf(res,'%f\n',min(FootRight(2:end,3)));
%write mean z for Right Foot
fprintf( res, 'Mean Z coordinate for Right Foot: ');
fprintf(res,'%f\n',mean(FootRight(2:end,3)));
%write Var z for Right Foot
fprintf( res, 'Variance Z coordinate for Right Foot: ');
fprintf(res,'%f\n',var(FootRight(2:end,3)));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for Left Ankle
fprintf( res, 'MAX X coordinate for Left Ankle: ');
fprintf(res,'%f\n',max(AnkleLeft(2:end,1)));
%write min x for Left Ankle
fprintf( res, 'MIN X coordinate for Left Ankle: ');
fprintf(res,'%f\n',min(AnkleLeft(2:end,1)));
%write mean x for Left Ankle
fprintf( res, 'Mean X coordinate for Left Ankle: ');
fprintf(res,'%f\n',mean(AnkleLeft(2:end,1)));
%write Var x for Left Ankle
fprintf( res, 'Variance X coordinate for Left Ankle: ');
fprintf(res,'%f\n',var(AnkleLeft(2:end,1)));



%write max y for Left Ankle
fprintf( res, 'MAX Y coordinate for Left Ankle: ');
fprintf(res,'%f\n',max(AnkleLeft(2:end,2)));
%write min y for Left Ankle
fprintf( res, 'MIN Y coordinate for Left Ankle: ');
fprintf(res,'%f\n',min(AnkleLeft(2:end,2)));
%write mean y for Left Ankle
fprintf( res, 'Mean Y coordinate for Left Ankle: ');
fprintf(res,'%f\n',mean(AnkleLeft(2:end,2)));
%write Var y for Left Ankle
fprintf( res, 'Variance Y coordinate for Left Ankle: ');
fprintf(res,'%f\n',var(AnkleLeft(2:end,2)));

%write max z for Left Ankle
fprintf( res, 'MAX Z coordinate for Left Ankle: ');
fprintf(res,'%f\n',max(AnkleLeft(2:end,3)));
%write min z for Left Ankle
fprintf( res, 'MIN Z coordinate for Left Ankle ');
fprintf(res,'%f\n',min(AnkleLeft(2:end,3)));
%write mean z for Left Ankle
fprintf( res, 'Mean Z coordinate for Left Ankle: ');
fprintf(res,'%f\n',mean(AnkleLeft(2:end,3)));
%write Var z for Left Ankle
fprintf( res, 'Variance Z coordinate for Left Ankle: ');
fprintf(res,'%f\n',var(AnkleLeft(2:end,3)));

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5

%write max x for Right Ankle
fprintf( res, 'MAX X coordinate for Right Ankle: ');
fprintf(res,'%f\n',max(AnkleRight(2:end,1)));
%write min x for Right Ankle
fprintf( res, 'MIN X coordinate for Right Ankle: ');
fprintf(res,'%f\n',min(AnkleRight(2:end,1)));
%write mean x for Right Ankle
fprintf( res, 'Mean X coordinate for Right Ankle: ');
fprintf(res,'%f\n',mean(AnkleRight(2:end,1)));
%write Var x for Right Ankle
fprintf( res, 'Variance X coordinate for Right Ankle: ');
fprintf(res,'%f\n',var(AnkleRight(2:end,1)));



%write max y for Right Ankle
fprintf( res, 'MAX Y coordinate for Right Ankle: ');
fprintf(res,'%f\n',max(AnkleRight(2:end,2)));
%write min y for Right Ankle
fprintf( res, 'MIN Y coordinate for Right Ankle: ');
fprintf(res,'%f\n',min(AnkleRight(2:end,2)));
%write mean y for Right Ankle
fprintf( res, 'Mean Y coordinate for Right Ankle: ');
fprintf(res,'%f\n',mean(AnkleRight(2:end,2)));
%write Var y for Right Ankle
fprintf( res, 'Variance Y coordinate for Right Ankle: ');
fprintf(res,'%f\n',var(AnkleRight(2:end,2)));

%write max z for Right Ankle
fprintf( res, 'MAX Z coordinate for Right Ankle: ');
fprintf(res,'%f\n',max(AnkleRight(2:end,3)));
%write min z for Right Ankle
fprintf( res, 'MIN Z coordinate for Right Ankle ');
fprintf(res,'%f\n',min(AnkleRight(2:end,3)));
%write mean z for Right Ankle
fprintf( res, 'Mean Z coordinate for Right Ankle: ');
fprintf(res,'%f\n',mean(AnkleRight(2:end,3)));
%write Var z for Right Ankle
fprintf( res, 'Variance Z coordinate for Right Ankle: ');
fprintf(res,'%f\n',var(AnkleRight(2:end,3)));
fclose(res);
end