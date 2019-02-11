import pandas as pd

from scipy.stats import boxcox
from matplotlib import pyplot as plt

from scipy import stats

def printHist():
    plt.hist(data, bins=5)

def printProbPlot(figure, location, feature_name, feature):
    axs1 = figure.add_subplot(location)
    stats.probplot(feature, dist='norm', plot=axs1)
    plt.xlabel(feature_name)

# Here we are using the BoxCox tranformation to take the feature and normalize it automatically
# 
def findLambdaAndGenerateProbPlot(figure, location, feature_name, feature):
    axs2 = figure.add_subplot(location)
    s_length, lambda_feature = boxcox(data.sepal_length)
    stats.probplot(s_length, dist='norm', plot=axs2)
    plt.xlabel(feature_name)

    print ('Lambda value for ', feature_name, ' is ', lambda_feature)
    return lambda_feature

data = pd.read_csv('iris.csv')

figure = plt.figure()
printProbPlot(figure, 421, 'Sepal Length', data.sepal_length)
lambda_sepal_length = findLambdaAndGenerateProbPlot(figure, 422, 'Normalized Sepal Length', data.sepal_length)
plt.show()

figure = plt.figure()
printProbPlot(figure, 421, 'Sepal Width', data.sepal_width)
lambda_sepal_width = findLambdaAndGenerateProbPlot(figure, 422, 'Normalized Sepal Width', data.sepal_width)
plt.show()

figure = plt.figure()
printProbPlot(figure, 421, 'Petal Length', data.petal_length)
lambda_petal_length = findLambdaAndGenerateProbPlot(figure, 422, 'Normalized Petal Length', data.petal_length)
plt.show()

figure = plt.figure()
printProbPlot(figure, 421, 'Petal Width', data.petal_width)
lambda_petal_width = findLambdaAndGenerateProbPlot(figure, 422, 'Normalized Petal Width', data.petal_width)
plt.show()
