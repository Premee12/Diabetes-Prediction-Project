# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:54:43 2019

@author: Abayomi-Ali Ayomide
"""

"""
How to load csv file using standard python library 
and use the function called READER() 
importing Numpy is a must
"""
import csv #import CSV
import numpy #import Numpy
filename = 'diabete-data.csv' #this will import the data file 
raw_data = open(filename, 'rt') # just like importing a txt file
reader = csv.reader(raw_data, delimiter= ',', quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype('float')
print(data) #it wiil print it in form of list
print(data.shape) #This will print the numbers of rows and columns

                   


