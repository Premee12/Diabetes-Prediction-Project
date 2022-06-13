# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:01:39 2020

@author: ACER
"""
"""
How to load csv file on using PYTHON STANDARD LIB
and use the function called READER() Function

 """

#import csv
#import numpy
#rawdata = open('Boston.csv', 'rt')
#reader = csv.reader(rawdata, delimiter= ',', quoting=csv.QUOTE_NONE) #MEANING NO QUOTES
#x =list(reader)
#data = numpy.array(x).astype('float') #To convert the data type to float
#print(data.shape)
#print(data)


#for another CSV data 
import csv
import numpy
rawdata = open('diabete-data.csv', 'rt')
reader = csv.reader(rawdata, delimiter= ',', quoting=csv.QUOTE_NONE) #MEANING NO QUOTES
x =list(reader)
data = numpy.array(x).astype('float') #To convert the data type to float
print(data.shape)
print(data)