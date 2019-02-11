import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

import PrintClassifierPerformance as pcp

irisData = pd.read_csv('iris.csv')

#Split the data set into X and Y
X = irisData.iloc[:,0:4]
Y = irisData.iloc[:,4:5]

#Convert Y values into numerica values
Y.loc [Y['species'] == 'setosa', 'species'] = 0
Y.loc [Y['species'] == 'versicolor', 'species'] = 1
Y.loc [Y['species'] == 'virginica', 'species'] = 2

#Split the data into test and train using K-Fold
kf = KFold(n_splits=10)
train_x, test_x, train_y, test_y =  train_test_split(X,Y)

#Initialize Random Forest Classifier
rfClassifier = RandomForestClassifier(criterion='entropy',max_depth=100, max_features='auto', oob_score=True, bootstrap=True)

#see if the classifier is doing an overfitting of the training data
rfClassifier.fit(train_x, train_y)
predicted_y_with_train_data = rfClassifier.predict(train_x)
pcp.printClassifierPerformanceOnTrainData(rfClassifier, train_x, train_y,predicted_y_with_train_data)

predicted_y_with_test_data = predicted_y=rfClassifier.predict(test_x)
pcp.printClassifierPerformanceOnTestData(rfClassifier, test_x, test_y, predicted_y_with_test_data)


# for train_index, test_index in kf.split(X):

#     print (train_index)
#     print (test_index)

#     train_x = X[train_index]
#     test_x = X[test_index]
#     train_y = Y[train_index]
#     test_y = Y[test_index]

    # print (train_x)
    # print (train_y)


