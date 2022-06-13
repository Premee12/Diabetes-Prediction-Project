# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:47:15 2019

@author: Abayomi-Ali Ayomide

WAYS OF DATA VISUALIZATION
"""

## HISTOGRAM WITH MATPLOTLIB
#from matplotlib import pyplot
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#data.hist()
#pyplot.show()

# OR
# HISTOGRAM WITH MATPLOTLIB
#from matplotlib import pyplot
#from pandas import read_csv
#filename = 'Boston.csv' #this will import the data file 
#names = ['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','black','lstat','medv']
#temi = read_csv(filename, names=names)
#temi.hist()
#pyplot.show()



# BOX AND WHISKERS PLOTS with MATPLOTLIB 
#from matplotlib import pyplot
#from pandas import read_csv
#filename = 'Boston.csv' #this will import the data file 
#names = ['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','black','lstat','medv']
#data = read_csv(filename, names=names)
#data.plot(kind='box', subplots=True, layout=(3,3), sharex=False)    #layout wiil determine the size(length,width)
#pyplot.show()

# OR   
from matplotlib import pyplot
from pandas import read_csv
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
data = read_csv(filename, names=names)
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False)    #layout wiil determine the size(length,width)
pyplot.show()
#
##Density plot with Matplotlib
#from matplotlib import pyplot
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#data.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
#pyplot.show()