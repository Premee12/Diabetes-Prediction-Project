# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:47:15 2019

@author: Abayomi-Ali Ayomide
"""

from matplotlib import pyplot
from pandas import read_csv
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
data = read_csv(filename, names=names)
data.hist()
pyplot.show()