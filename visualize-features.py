import pandas as pd

from matplotlib import pyplot  as plt

data = pd.read_csv('iris.csv')

plt.figure(1)

plt.subplot(2,2,1)
plt.hist(data.sepal_length,5,normed=True)
plt.ylabel('sepal length f')

plt.subplot(2,2,2)
plt.hist(data.sepal_width,5,normed=True)
plt.ylabel('sepal width f')

plt.subplot(2,2,3)
plt.hist(data.petal_length,5,normed=True)
plt.ylabel('petal length f')

plt.subplot(2,2,4)
plt.hist(data.petal_width,5,normed=True)
plt.ylabel('petal width f')

plt.figure(2)

plt.subplot(2,2,1)
plt.scatter(data.sepal_length, data.species, norm=True)
plt.xlabel('Sepal Length')
plt.ylabel('Species')

plt.subplot(2,2,2)
plt.scatter(data.sepal_width, data.species, norm=True)
plt.xlabel('Sepal Width')
plt.ylabel('Species')

plt.subplot(2,2,3)
plt.scatter(data.petal_length, data.species, norm=True)
plt.xlabel('Petal Length')
plt.ylabel('Species')

plt.subplot(2,2,4)
plt.scatter(data.petal_width, data.species, norm=True)
plt.xlabel('Petal Width')
plt.ylabel('Species')

plt.show()
