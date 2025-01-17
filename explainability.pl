#pred diagnosis(X,1,Y) :: 'Doctor @(Y) said that @(X) is at the gates of heaven'.
#pred diagnosis(X,0,Y) :: 'Doctor @(Y) said that @(X) is fresh like a daisy'.

#pred age(X, Age) :: 'has @(Age) years old'.

#pred sex(X, 1) :: 'is male'.
#pred sex(X, 0) :: 'is female'.

#pred cp(X, 0) :: 'has typical angina'.
#pred cp(X, 1) :: 'has atypical angina'.
#pred cp(X, 2) :: 'has non-anginal pain'.
#pred cp(X, 3) :: 'is asymptomatic'.

#pred trestbps(X, BP) :: 'has a resting blood pressure of @(BP) mm/HG'.

#pred chol(X, Chol) :: 'has a cholesterol level of @(Chol) mg/dl'.

#pred fbs(X, 1) :: 'has a high fasting blood sugar level'.
#pred fbs(X, 0) :: 'has a normal fasting blood sugar level'.

#pred restecg(X, 0) :: 'has a normal resting ECG result'.
#pred restecg(X, 1) :: 'has an ST-T wave abnormality in the resting ECG result'.
#pred restecg(X, 2) :: 'has left ventricular hypertrophy in the resting ECG result'.

#pred thalach(X, HR) :: 'has a maximum heart rate of @(HR)'.

#pred exang(X, 1) :: 'has exercise-induced angina: yes'.
#pred exang(X, 0) :: 'has exercise-induced angina: no'.

#pred oldpeak(X, Depression) :: 'has exercise-induced ST depression of @(Depression)'.

#pred slope(X, 0) :: 'has an upsloping ST segment during peak exercise'.
#pred slope(X, 1) :: 'has a flat ST segment during peak exercise'.
#pred slope(X, 2) :: 'has a downsloping ST segment during peak exercise'.

#pred ca(X, Vessels) :: 'has @(Vessels) major vessels'.

#pred thal(X, 1) :: 'has normal blood flow'.
#pred thal(X, 2) :: 'has a fixed defect'.
#pred thal(X, 3) :: 'has a reversible defect'.




