 # -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:59:37 2019

@author: Abayomi-Ali Ayomide
"""


from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
#Split the data into input and output variables
X = array[:,0-8]
Y = array[:,8]
scaler = MinMaxScaler(feature_range=(0,1))
rescalex = scaler.fit_transform(X)
set_printoptions(precision=3)
print(rescalex[0.5,:])
array.reshape(1, - 1)