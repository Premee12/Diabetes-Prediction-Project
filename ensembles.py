# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:00:14 2019

@author: Abayomi-Ali Ayomide
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import VotingClassifier

#Load the data
filename = 'diabete-data.csv' #this will ismport the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
#split the arry into input and output
X = array[:, 0:8] #Split the array into 9(nine) from 0 to 8
Y = array[:,8] #this will separate the nineth array

num_folds = 10 #The dataset should be randomly divided into any number folds
kfold = KFold(n_splits=10, random_state=7)
#Create the sub models
estimators=[]
model1 = LogisticRegression(solver='liblinear')
estimators.append(('Logistic', model1))
model2 =DecisionTreeClassifier()
estimators.append(('CART', model2))
model3 = SVC(gamma='auto')
estimators.append(('SVC', model3))
#Create the ensemble model
ensemble = VotingClassifier(estimators)
#print(ensemble)
results = cross_val_score(ensemble, X, Y, cv=kfold)
#print(results)

print(results.mean())