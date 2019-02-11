import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold

import PrintClassifierPerformance as pcp

irisData = pd.read_csv('iris.csv')

#Split the data set into X and Y
X = irisData.iloc[:,0:4]
Y = irisData.iloc[:,4:5]
#print (type(Y))

#Convert Y values into numerica values
Y.replace(to_replace='setosa', value=0, inplace=True)
Y.replace(to_replace='versicolor', value=1, inplace=True)
Y.replace(to_replace='virginica', value=2, inplace=True)

kFolds = 5

#Split the data into test and train using K-Fold
kf = KFold(n_splits=kFolds,shuffle=True)

#Initialize Random Forest Classifier
#rfClassifier = RandomForestClassifier(criterion='entropy',max_depth=100, max_features='auto', oob_score=True, bootstrap=True)
rfClassifier = KNeighborsClassifier(n_neighbors=3, algorithm='auto')

runningModelScore = 0
for train_index, test_index in kf.split(X):

    train_x = X.iloc[train_index]
    test_x = X.iloc[test_index]
    train_y = Y.iloc[train_index]
    test_y = Y.iloc[test_index]

    #see if the classifier is doing an overfitting of the training data
    model = rfClassifier.fit(train_x, train_y.values.ravel()) 
    modelScore = model.score(test_x, test_y)
    predicted_y_with_test_data = predicted_y=rfClassifier.predict(test_x)

    pcp.printKNNClassifierPerformance(rfClassifier, modelScore, test_x, test_y, predicted_y_with_test_data)

    runningModelScore = runningModelScore + modelScore

print ('Average Model Score is ', runningModelScore/kFolds)
