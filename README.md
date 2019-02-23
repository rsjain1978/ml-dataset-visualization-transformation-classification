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
- visualize-features.py
Contains code to visualize the relation between each feature and class variable via scatter plot and histogram

- normalize-data.py
Python code which normalizes each feature and does a BoxCox transformation. Code produces one graph for each feature, where-in each graph shows a normalized and non-normalized data view to show the impact of boxcox tranformation.

- find-top-features-rf-kfold.py
Contains code to find top features using RandomForestClassfier and with Cross Validation (K-Fold) for data splitting

- find-top-features-rf-holdout.py
Contains code to find top features using RandomForestClassfier and with Hold Out for data splitting

- find-top-features-knn-kfold.py
Python ode to find top features using KNNClassfier and with Cross Validation (K-Fold) for data splitting

- relational-strength.py
Contains code to plot a corelation between the variables of the provided dataset. This code uses
corr() function to draw the corelation and then plot using matplotlib

- interpreting-confusion-matrix.py
Python code for calculating various performance measures using the TP, FN, FP and TN values of two confusion matrix.

- performancemetrics.py
Python utility code to show the performance metrics for different classifiers