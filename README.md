# ml-dataset-visualization-transformation-classification

#Top Features for class variable 'species' are
- Feature Importance is                importance
- petal_length    0.570218
- petal_width     0.292544
- sepal_length    0.102146
- sepal_width     0.035091

#Model Performance
- KNN Model - Average model score is 0.9600000000000002
- Random Forest - Average model score is 0.9400000000000001


#Files Description
- VisualizeFeatures.py
{ Contains code to visualize the relation between each feature and class variable via scatter plot and histogram}

-DataNormalization.py
{ Contians code to do normalize each feature and do BoxCox transformation}

- TopFeatures-KFold.py
{ Contains code to find top features using RandomForestClassfier and with Cross Validation (K-Fold) for data splitting}

- TopFeatures.py
{ Contains code to find top features using RandomForestClassfier and with Hold Out for data splitting}

- TopFeaturesKNN-KFold.py
{ Contains code to find top features using KNNClassfier and with Cross Validation (K-Fold) for data splitting}

- RelationalStrengthOfVariables.py
{ Contains code to plot a corelation between the variables of the provided dataset. This code uses
corr() function to draw the corelation and then plot using matplotlib}

- InterpretingConfusionMatrix.py
{ Conatins code to calculating various performance measures using the TP, FN, FP and TN values of two confusion matrix}