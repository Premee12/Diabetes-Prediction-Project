# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:14:01 2019

@author: Abayomi-Ali Ayomide
"""


#Density plot with Matplotlib

from matplotlib import pyplot
from pandas import read_csv
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
data = read_csv(filename, names=names)
data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()