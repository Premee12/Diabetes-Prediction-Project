# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:23:51 2019

@author: Abayomi-Ali Ayomide
"""
from matplotlib import pyplot
from pandas import read_csv
from pandas.plotting import scatter_matrix
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
data = read_csv(filename, names=names)
scatter_matrix(data)
pyplot.show
