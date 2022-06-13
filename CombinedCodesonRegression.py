# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:03:11 2019

@author: Abayomi-Ali Ayomide
"""

#USING HOUSING CSV FILE

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression #this is a model we are to use
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.linear_model import ElasticNet 

filename = 'housing.csv' #this will ismport the data file 
names = ['CRIM','ZN','INDUS','CHAS','NOS','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
dataframe = read_csv(filename, delim_whitespace=True, names=names) # Using delim_whitespace This will remove(close) the white spaces btw the data if its not properly formatted 
array = dataframe.values
X = array[:,0:13] 
Y = array[:,13]

#this is where we start the test
kfold = KFold(n_splits=10, random_state=7) #where seed is 7
model1 = LinearRegression()
model2 = Ridge()
model3 = Lasso()
model4 = ElasticNet()


scoring = 'neg_mean_squared_error'
results1 = cross_val_score(model1, X, Y, cv=kfold, scoring=scoring)
print(results1.mean()) #he value gotten will not be in percentage, it will have been converted to numbers bcoz its not multiplied by 100 yet.

results2 = cross_val_score(model2, X, Y, cv=kfold, scoring=scoring)
print(results2.mean()) 

results3 = cross_val_score(model3, X, Y, cv=kfold, scoring=scoring)
print(results3.mean()) 

results4 = cross_val_score(model4, X, Y, cv=kfold, scoring=scoring)
print(results4.mean()) 

