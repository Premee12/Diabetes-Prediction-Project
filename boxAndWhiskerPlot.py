# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 13:31:13 2019

@author: Abayomi-Ali Ayomide
"""

from matplotlib import pyplot
from pandas import read_csv
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
data = read_csv(filename, names=names)
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False)    #layout wiil determine the size(length,width)
pyplot.show()