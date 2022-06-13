# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 10:22:52 2019

@author: Abayomi-Ali Ayomide

THERE ARE FOUR(4) NON_LINEAR CLASSIFICATION ALGORITHMS
"""

"""1. Spot-Checking of Non_Linear classification Algorithms
K Nearest Neighbors syntax(KNN)
the threshold accuracy must not be less than 72% to 75%
"""
#
from pandas import read_csv 
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier #this is a model we are to use

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
model = KNeighborsClassifier() #note you should remove the solver when dealing with Discriminant analysis or set your solver to svd 
#for example (solver='svd')

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers  bcoz its not multiplied by 100 yet
print("Accuracy:%.4f%% (%.4f%%) " % (results.mean()*100.0, results.std()*100.0))



#"""2. Spot-Checking of Non_Linear classification Algorithms
#Naive Bayes(NB)
#the threshold accuracy must not be less than 75% to 76%
#"""
#
#from pandas import read_csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.naive_bayes import GaussianNB #this is a model we are to use
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
#model = GaussianNB() #note you should remove the solver.
#
#results = cross_val_score(model, X, Y, cv=kfold)
#print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers bcoz its not multiplied by 100 yet
#print("Accuracy:%.4f%% (%.4f%%) " % (results.mean()*100.0, results.std()*100.0))



"""3. Spot-Checking of Non_Linear classification Algorithms
Classification and Regression Trees(CAT)
the threshold accuracy must not be less than 69.2%
"""

#from pandas import read_csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.tree import DecisionTreeClassifier #this is a model we are to use
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
#model = DecisionTreeClassifier() #note you should remove the solver.
#
#results = cross_val_score(model, X, Y, cv=kfold)
#print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers  bcoz its not multiplied by 100 yet
#print("Accuracy:%.4f%% (%.4f%%) " % (results.mean()*100.0, results.std()*100.0))
#


"""4. Spot-Checking of Non_Linear classification Algorithms
Support Vector Machine(SVM) using SVC bcoz its classification
the threshold accuracy must not be less than 65.1%
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC #this is a model we are to use

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
model = SVC(gamma=True) #note you should remove the solver.

results = cross_val_score(model, X, Y, cv=kfold)
print(results.mean()) #he value gotten will not be in percentage, it will have been converted to numbers bcoz its not multiplied by 100 yet.
print("Accuracy:%.4f%% (%.4f%%) " % (results.mean()*100.0, results.std()*100.0))