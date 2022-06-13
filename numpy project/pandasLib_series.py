# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:24:23 2019

@author: Abayomi-Ali Ayomide
"""

import numpy #import NUMPY library
import pandas #import pandas library
myarray = numpy.array([4,6,10,12,14]) #put the array into numpy
rownames = ['a','b','c','d','e']  #becos its single dimensional
myseries = pandas.Series(myarray, index=rownames) # .Series the S is in capital letter.
print(myseries)

#To access data from the series.
# This will print the value assigned to each index
print(myseries['a']) #Using the row names
#Using each index value
print("This is a value of data which is: %s" % (myseries[2]))
print(myseries[-1]) 
print(myseries.shape)



#try your own
#import pandas
#import numpy
#ayomide = numpy.array([2,4,6,8,10,12])
#rownames = ['a','b','c','d','e','f']
#ayomideseries = pandas.Series(ayomide, index=rownames)
#print(ayomideseries)
#
#print("Value assigned to second index is: ", (ayomideseries['b']))
#print(ayomideseries[-2])  #print the second to the last value