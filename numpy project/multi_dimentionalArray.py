# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:08:09 2019

@author: Abayomi-Ali Ayomide
"""

# Creating a multidimensional array
import numpy
mylist= [[1,2,5], [4,5,6],[7,8,9]] #Create a multi-Dimensional array using 2 square-brackets to group it
mynumpyarray = numpy.array(mylist) #Here we convert the array into numpy.
print(mynumpyarray) 
print(mynumpyarray.shape) #This line print out the shape of the array.
 #accessing the array
print("First Row: %s" % mynumpyarray[0])
print("Last Row: %s" % mynumpyarray[-1])
print("Row one Column three: %s" %(mynumpyarray[0,2]))
""" 
This is another way of writing the same code
"""

import numpy
myCat = numpy.array([[1,2,3],[4,5,6],[7,8,9]]) #skip creating the list and convert the array to numpy array
print("\n") #to create a new line to separate the codes output
print(myCat)
print(myCat.shape)

print(myCat[0]) #will print first row
print(myCat[-1]) #will print the last row
print(myCat[-2]) #will print the 2nd row
print(myCat[1]) #will print the 2nd row again
