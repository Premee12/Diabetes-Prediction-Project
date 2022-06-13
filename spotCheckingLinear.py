# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 09:51:24 2019

@author: Abayomi-Ali Ayomide
"""
## the accuraccy must not be less than 76%
#from pandas import read_csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LogisticRegression #this is a model
#
#filename = 'diabete-data.csv' #this will ismport the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#dataframe = read_csv(filename, names=names)
#array = dataframe.values
##Slit the data into input and output
#X = array[:, 0:8] 
#Y = array[:,8]
#
##this is where we start the test
#num_folds = 10 #The dataset should be randomly divided into any number folds
#kfold = KFold(n_splits=10, random_state=7) #where seed is 7
#model = LogisticRegression(solver='liblinear')
#
#result = cross_val_score(model, X, Y, cv=kfold)
#print(result.mean()) #The value gotten will not be in percentage, it will have been converted to numbers by already dividing it by 100


""" Spot-Checking of liner classificationAlgorithms
linear Discriminant Analysis(LDA)
the threshold accuracy must not be less than 77%
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis #this is a model

filename = 'diabete-data.csv' #this will ismport the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
#Slit the data into input and output
X = array[:, 0:8] 
Y = array[:,8]

#this is where we start the test
num_folds = 10 #The dataset should be randomly divided into any number folds
kfold = KFold(n_splits=10, random_state=7) #where seed is 7
model = LinearDiscriminantAnalysis() #note you should remove the solver when dealing with Discriminant analysis or set your solver to svd 
#for example (solver='svd')

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers by already dividing it by 100
print("Accuracy:%.4f%% (%.4f%%) " % (results.mean()*100.0, results.std()*100.0))