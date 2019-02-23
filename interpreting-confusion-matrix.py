import pandas as pd

from sklearn.metrics import confusion_matrix

def printModelPerformance(TP, FN, FP, TN, modelName):

    #computing metrics, accuracy, sensitivity, specificity and F1-score. Which model is better
    accuracy = (TP+TN)/(TP+TN+FP+FN)
    precision = (TP)/(TP+FP)
    sensitivity = (TP)/(TP+FN)
    specificity = (TN)/(TN+FP)
    f1score = (2*TP)/(2*TP+FP+FN)

    print (' ')
    print ('accuracy of ',modelName,' is ', accuracy)
    print ('precision of ',modelName,' is ', precision)
    print ('sensitivity of ',modelName,' is ', sensitivity)
    print ('specificity of ',modelName,' is ', specificity)
    print ('f1score of ',modelName,' is ', f1score)
    print ('')

    return f1score


model1_TruePositiveTP = 100
model1_FalseNegativeFN = 30
model1_FalsePositiveFP = 20
model1_TrueNegativeTN = 200

model2_TruePositiveTP = 150
model2_FalseNegativeFN = 100
model2_FalsePositiveFP = 50
model2_TrueNegativeTN = 50

model1_f1score = printModelPerformance(model1_TruePositiveTP, model1_FalseNegativeFN, model1_FalsePositiveFP, model1_TrueNegativeTN,'model 1')
model2_f1score = printModelPerformance(model2_TruePositiveTP, model2_FalseNegativeFN, model2_FalsePositiveFP, model2_TrueNegativeTN,'model 2')

print ('Overall the Accuracy & F1 Score of Model 1 is better thatn Model 2, hence Model 1 is better')