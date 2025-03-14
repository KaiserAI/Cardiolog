% Rules generated by tree 5
% ---------------------------------------------

diagnosis(Patient,0,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #=< 1.95,
    slope(Patient,0),
    ca(Patient,2).

diagnosis(Patient,0,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #=< 1.95,
    slope(Patient,0),
    ca(Patient,3).

diagnosis(Patient,0,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #=< 1.95,
    slope(Patient,1),
    fbs(Patient,0).

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #=< 1.95,
    slope(Patient,1),
    fbs(Patient,1).

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #> 1.95,
    thalach(Patient,X2),
    X2 #=< 166.5,
    chol(Patient,X3),
    X3 #=< 269.5.

diagnosis(Patient,0,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #> 1.95,
    thalach(Patient,X2),
    X2 #=< 166.5,
    chol(Patient,X3),
    X3 #> 269.5.

diagnosis(Patient,0,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #> 1.95,
    thalach(Patient,X2),
    X2 #> 166.5,
    exang(Patient,0).

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,2),
    oldpeak(Patient,X1),
    X1 #> 1.95,
    thalach(Patient,X2),
    X2 #> 166.5,
    exang(Patient,1).

diagnosis(Patient,0,'Dra. Davis') :- 
    cp(Patient,3),
    thalach(Patient,X1),
    X1 #=< 151.0,
    thal(Patient,2),
    chol(Patient,X3),
    X3 #=< 232.5.

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,3),
    thalach(Patient,X1),
    X1 #=< 151.0,
    thal(Patient,2),
    chol(Patient,X3),
    X3 #> 232.5.

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,3),
    thalach(Patient,X1),
    X1 #=< 151.0,
    thal(Patient,3).

diagnosis(Patient,0,'Dra. Davis') :- 
    cp(Patient,3),
    thalach(Patient,X1),
    X1 #> 151.0,
    age(Patient,X2),
    X2 #=< 59.5,
    ca(Patient,0).

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,3),
    thalach(Patient,X1),
    X1 #> 151.0,
    age(Patient,X2),
    X2 #=< 59.5,
    ca(Patient,1).

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,3),
    thalach(Patient,X1),
    X1 #> 151.0,
    age(Patient,X2),
    X2 #> 59.5,
    age(Patient,X3),
    X3 #=< 63.5.

diagnosis(Patient,1,'Dra. Davis') :- 
    cp(Patient,3),
    thalach(Patient,X1),
    X1 #> 151.0,
    age(Patient,X2),
    X2 #> 59.5,
    age(Patient,X3),
    X3 #> 63.5.

