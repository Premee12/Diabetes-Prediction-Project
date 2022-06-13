# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:31:13 2019

@author: Abayomi-Ali Ayomide
"""

from matplotlib import pyplot
from pandas import read_csv
import numpy
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
data = read_csv(filename, names=names)
correlations = data.corr()
#Plot the correlation Matrix
fig = pyplot.figure()
ax = fig.add_subplot(111) #It can be 222 or 333 etc but the numbers must not include zero's
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = numpy.arange(0,10,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show

