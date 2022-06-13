# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 14:53:35 2019

@author: Abayomi-Ali Ayomide
"""

from pickle import load
#name the saved model from another computer
filename = 'finalized_model.sav'
#load the file
load_model = load(open(filename, 'rb'))
#define one new data instance for prediction
#xnew = [[0,132,90,33,167,40.1,3.288,30]] #note it going to be a double array
xnew = [[7,142,90,24,480,30.4,0.128,43]]
#xnew = [[2,174,88,37,120,44.5,0.646,24]]
#make the prdiction
ynew = load_model.predict(xnew)
print("input = %s, Predicted = %s" %(xnew[0], ynew[0]))