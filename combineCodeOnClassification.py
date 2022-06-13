# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:24:00 2019

@author: Abayomi-Ali Ayomide
"""

from pandas import read_csv
from matplotlib import pyplot
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

filename = 'diabete-data.csv' #this will ismport the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:, 0:8] #Split the array into 9(nine) from 0 to 8
Y = array[:,8] #this will separate the nineth array

"""Prepare the model
we cannot use all the models one after the order. The best thing to do is to pass all the models
into one array and access them from there.
"""
models = []
#when adding into an array you shpuld append
models.append(('LR', LogisticRegression(solver='liblinear')))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVC', SVC(gamma='auto')))

"""
Evaluate each of the model in order
toselect the appropraite model to use
"""
results = []
names = []
scoring = 'accuracy'
for name, model in models:
    kfold = KFold(n_splits=10, random_state=7) #where seed is 7
    cv_results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f(%f)" %(name, cv_results.mean(), cv_results.std())
    print(msg)
    
"""
Construct the boxplot for the algorithm comparison
"""

fig = pyplot.figure()
fig.suptitle('Algorithm Comparison and Evaluation')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show