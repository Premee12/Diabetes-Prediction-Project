# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:58:49 2019

@author: Abayomi-Ali Ayomide
"""

""" THis consists of the various    MACHINE LEARNING
 Algorithm Evaluation TECNIQUE. """
 
"""using the test and train method to test the accuracy 
of the model used """
#
#from pandas import read_csv
#from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression #this is a model
#
#filename = 'diabete-data.csv' #this will ismport the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#dataframe = read_csv(filename, names=names)
#array = dataframe.values
##Slit the data into input and output
#X =array[:, 0:8]  #All the input columns
#Y = array[:,8]  #consist of just the output column
#
##this is where we start the test
#test_data = 0.33 #using 33% which is 0.33
#seed = 7 #this denotes that there are 8 colunms (0 -7)
#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_data, random_state= seed)
#model = LogisticRegression(solver='liblinear')
#model.fit(X_train, Y_train)
#result = model.score(X_test, Y_test)
#print("Accuracy:%.4f%%" % (result*100.0)) 


""" using the K-fold  method to test the accuracy 
of the model used testing it randomly. Note: you can
set the number of folds to any number """
#from pandas import read_csv
#from sklearn.model_selection import KFold
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LogisticRegression #this is a model
#
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#dataframe = read_csv(filename, names=names)
#array = dataframe.values
##Slit the data into input and output
#X = array[:, 0:8] 
#Y = array[:,8]
#
##this is where we start the test
#num_folds = 10 #The dataset should be randomly divided into any number folds
#seed = 7
#kfold = KFold(n_splits=num_folds, random_state=seed)
#model = LogisticRegression(solver='liblinear')
#
#result = cross_val_score(model, X, Y, cv=kfold)
#print("Accuracy:%.3f%% (%.3f%%) " % (result.mean()*100.0, result.std()*100.0))



""" using the LEAVE ONE OUT CROSS VALIDATION  method
 to test the accuracy of the model used testing it randomly. 
Note: Here you set the number of splits to any number too
and split the dataset into 67%(7) and 33%(0.33)
"""

#
#from pandas import read_csv
#from sklearn.model_selection import ShuffleSplit
#from sklearn.model_selection import cross_val_score
#from sklearn.linear_model import LogisticRegression #this is a model
#
#filename = 'diabete-data.csv' #this will ismport the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#dataframe = read_csv(filename,names=names)
#array = dataframe.values
##Slit the data into input and output
#X = array[:, 0:8] 
#Y = array[:,8]
#
##this is where we start the test
#num_splits = 10 #The dataset should be randomly divided into any number folds
#test_size = 0.33
#seed = 7
#splits = ShuffleSplit(n_splits=num_splits, test_size=test_size, random_state=seed)
#model = LogisticRegression(solver='liblinear')
#
#result = cross_val_score(model, X, Y, cv= kfold)
#print("Accuracy:%.3f%% (%.3f%%) " % (result.mean()*100.0, result.std()*100.0))




""" using REPEATED RANDOM TRAIN TEST SPLITS method
 to test the accuracy of the model used testing it randomly. 
Note: Here you set the number of splits to any number too
and split the dataset into 67%(7) and 33%(0.33)
"""


from pandas import read_csv
from sklearn import model_selection 
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression #this is a model

filename = 'diabete-data.csv' #this will ismport the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
#Slit the data into input and output
X = array[:, 0:8] 
Y = array[:,8] 

#this is where we start the test
num_folds = 10 #The dataset should be randomly divided into any number folds
num_instances = len(X)
seed = 7
splits = ShuffleSplit(n_splits=num_splits, test_size=test_size, random_state=seed)
model = LogisticRegression(solver='liblinear')

result = cross_val_score(model, X, Y, cv=kfold)
print("Accuracy:%.3f%% (%.3f%%) " % (result.mean()*100.0, result.std()*100.0))