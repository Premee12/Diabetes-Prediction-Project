# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 12:08:46 2019

@author: Abayomi-Ali Ayomide

THERE ARE FOUR METHODS FOR SPOT CHECKING OF LINEAR REGRESSION ALGORITHM
NOTE: LR uses CONTINOUS VALUES and not a True or False measurement
"""

"""1. Spot-Checking of Linear Regression Algorithms
LOGISTIC REGRESSION
the threshold accuracy must not be less than -34.075
"""
#USING HOUSING CSV FILE
#from pandas import read_csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LinearRegression #this is a model we are to use
#
#filename = 'housing.csv' #this will ismport the data file 
#names = ['CRIM','ZN','INDUS','CHAS','NOS','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
#dataframe = read_csv(filename, delim_whitespace=True, names=names) # Using delim_whitespace This will remove(close) the white spaces btw the data if its not properly formatted 
#array = dataframe.values
##print(dataframe.shape) #this is always used to find the number of rows and the numbers of column
#
#
#X = array[:,0:13] 
#Y = array[:,13]
#
##this is where we start the test
#kfold = KFold(n_splits=10, random_state=7) #where seed is 7
#model = LinearRegression()
#scoring = 'neg_mean_squared_error'
#results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
#print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers bcoz its not multiplied by 100 yet.
#print("Mean Square Error Linear Regression: %.4f%% (%.4f%%) " % (results.mean()*100.0, results.std()*100.0)) 


## USING DIABETE-DATA CSV FILE
## note: diabete-data is not suitable for this regression method bcoz the output colunm comprises of 0's and 1's(bolean)
#from pandas import read_csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LinearRegression #this is a model we are to use
#
#filename = 'diabete-data.csv' #this will ismport the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#dataframe = read_csv(filename, delim_whitespace=False, names=names) # we don't need to remove(close) the white spaces bcoz there is no whitespace therefore set it to false.
#array = dataframe.values
##print(dataframe.shape) #this is always used to find the number of rows and the numbers of column
#
#
#X = array[:,0:8] 
#Y = array[:,8]
#
##this is where we start the test
#kfold = KFold(n_splits=10, random_state=7) #where seed is 7
#model = LinearRegression()
#scoring = 'neg_mean_squared_error'
#results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
#print(results.mean())



#"""2. Spot-Checking of Linear Regression Algorithms
#RIDGE REGRESSION
#the threshold accuracy must not be less than -34.078
#"""
##USING HOUSING CSV FILE
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import Ridge #this is a model we are to use

filename = 'housing.csv' #this will ismport the data file 
names = ['CRIM','ZN','INDUS','CHAS','NOS','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
dataframe = read_csv(filename, delim_whitespace=True, names=names) # Using delim_whitespace This will remove(close) the white spaces btw the data if its not properly formatted 
array = dataframe.values
#print(dataframe.shape) #this is always used to find the number of rows and the numbers of column


X = array[:,0:13] 
Y = array[:,13]

#this is where we start the test
kfold = KFold(n_splits=10, random_state=7) #where seed is 7
model = Ridge()
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers bcoz its not multiplied by 100 yet.
print("Mean Square Error Linear Regression: %.3f%% (%.3f%%) " % (results.mean()*100.0, results.std()*100.0)) 
#



#"""3. Spot-Checking of Linear Regression Algorithms
#LASSO LINEAR REGRESSION 
#the threshold accuracy must not be less than -34.464
#"""
##USING HOUSING CSV FILE
#from pandas import read_csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import Lasso  #this is a model we are to use
#
#filename = 'housing.csv' #this will ismport the data file 
#names = ['CRIM','ZN','INDUS','CHAS','NOS','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
#dataframe = read_csv(filename, delim_whitespace=True, names=names) # Using delim_whitespace This will remove(close) the white spaces btw the data if its not properly formatted 
#array = dataframe.values
##print(dataframe.shape) #this is always used to find the number of rows and the numbers of column
#
#
#X = array[:,0:13] 
#Y = array[:,13]
#
##this is where we start the test
#kfold = KFold(n_splits=10, random_state=7) #where seed is 7
#model = Lasso()
#scoring = 'neg_mean_squared_error'
#results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
#print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers bcoz its not multiplied by 100 yet.
#print("Mean Square Error of Linear Regression: %.3f%% (%.3f%%) " % (results.mean()*100.0, results.std()*100.0)) 




"""4. Spot-Checking of Linear Regression Algorithms
LASSO LINEAR REGRESSION 
the threshold accuracy must not be less than -34.464
"""
#USING HOUSING CSV FILE
from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import ElasticNet  #this is a model we are to use

filename = 'housing.csv' #this will ismport the data file 
names = ['CRIM','ZN','INDUS','CHAS','NOS','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']
dataframe = read_csv(filename, delim_whitespace=True, names=names) # Using delim_whitespace This will remove(close) the white spaces btw the data if its not properly formatted 
array = dataframe.values
#print(dataframe.shape) #this is always used to find the number of rows and the numbers of column


X = array[:,0:13] 
Y = array[:,13]

#this is where we start the test
kfold = KFold(n_splits=10, random_state=7) #where seed is 7
model = ElasticNet()
scoring = 'neg_mean_squared_error'
results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers bcoz its not multiplied by 100 yet.
print("Mean Square Error of Linear Regression: %.2f%% (%.2f%%) " % (results.mean()*100.0, results.std()*100.0)) 



