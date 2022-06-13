# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 12:01:33 2019

@author: Abayomi-Ali Ayomide
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier

#Load the data
filename = 'diabete-data.csv' #this will ismport the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values

#split the arry into input and output
X = array[:, 0:8] #Split the array into 9(nine) from 0 to 8
Y = array[:,8] #this will separate the nineth array
seed= 7
num_trees = 100 #The dataset should be randomly divided into any number folds
max_features = 3
kfold = KFold(n_splits=10, random_state=seed)

# Bagged Decision Tree Model
cart = DecisionTreeClassifier()
model = BaggingClassifier(base_estimator=cart, n_estimators=num_trees, random_state=seed)
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy Bagged Decision: %f" %(results.mean()))

#random Desision Tree Model
bag = RandomForestClassifier()
model= RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy Ramdom Forest: %f" %(results.mean()))

#Extra tree model
Book = ExtraTreesClassifier()
model = BaggingClassifier(n_estimators=num_trees, max_features=max_features)
results = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy Extra Tree: %f" %(results.mean()))
