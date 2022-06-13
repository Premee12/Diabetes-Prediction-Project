# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 15:22:16 2021

@author: ACER
"""

from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import Binarizer
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
#Split the data into input and output variables
X = array[:,0:8]
Y = array[:,8]
binarizer = Binarizer(threshold=0.0).fit(X)
binaryX = binarizer.transform(X)
set_printoptions(precision=3)
print(binaryX[0:5,:])
array.reshape(1, - 1) 