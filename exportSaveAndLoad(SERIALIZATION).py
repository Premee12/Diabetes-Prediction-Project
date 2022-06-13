# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:09:11 2019

@author: Abayomi-Ali Ayomide
"""
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load

filename = 'diabete-data.csv' #this will ismport the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values

#split the arry into input and output
X = array[:, 0:8] #Split the array into 9(nine) from 0 to 8
Y = array[:,8] #this will separate the nineth array
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.33, random_state=7)
#Fit the Model on 33%
model = LogisticRegression(solver='liblinear') #Note: there is assumption that logistic regression is the best for academic purpose
model.fit(X_train, Y_train)

#Then save model to disk
filename= 'finalized_model.sav'
dump(model, open(filename,'wb'))

#copy the file to some server or other computers and then

#Load the model from disk

load_model = load(open(filename, 'rb'))
result = load_model.score(X_test, Y_test)
print(result)
print(result*100)
