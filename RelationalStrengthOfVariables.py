# “corr()” is very easy to use and very powerful for the early stages of data analysis (data preparation)
# when there is no correlation between 2 variables (when correlation is 0 or near 0) the color is gray. 
# The darkest red means there is a perfect positive correlation, while the darkest blue means there is a perfect negative correlation
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('iris.csv')

corr = data.corr()

figure = plt.figure(1)
axis = figure.add_subplot(111)

cax = axis.matshow(corr, cmap='coolwarm', vmin=-1, vmax=1)
figure.colorbar(cax)
ticks = np.arange(0,len(data.columns),1)
axis.set_xticks(ticks)
plt.xticks(rotation=90)
axis.set_yticks(ticks)
axis.set_xticklabels(data.columns)
axis.set_yticklabels(data.columns)

plt.show()
