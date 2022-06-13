# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:08:09 2019

@author: Abayomi-Ali Ayomide
"""

# Creating a multidimensional array
import numpy
mylist= [[1,2,3], [4,5,6],[7,8,9]] #Create a multi-Dimensional array using 2 square-brackets to group it
#mylist= [[1,2,3], [4,5,6]] #This will create a 2-Dimensional array
mynumpyarray = numpy.array(mylist) #Here we convert the array into numpy.
print(mynumpyarray) #this will just print the array out.
print("\nDimension of the array",(mynumpyarray.shape)) #This line print out the shape of the array.
 #accessing the array
print("First Row: %s" % (mynumpyarray[0]))
print("\nFirst Row: ", (mynumpyarray[0])) #another way to print the first row without using %
#Using % here we can choose to put the array we are accessing in the bracket if we like.
print("Last Row: %s" % mynumpyarray[-1])
print("This is the third element in row one: %s" % mynumpyarray[0,2])
#We can also accept the value in the list as an integer e.g %d but the array or list must be accessed in string %s.
print("This is the last element in row two: %d" % mynumpyarray[1,-1])
print("This is the last element in the last row: %d" % mynumpyarray[-1,-1])
print("This is the whole Second Column of each row in the array: %s" %mynumpyarray[:,1]) #this will print each 2nd column in the array.
print("This is the whole Third Column of each row in the array: %s" %mynumpyarray[:,2]) #this will print each 3 column in the array

#this will print each first column in the array
print("This is the whole first Column of each row in the array: ", (mynumpyarray[:,0]))
print("This is the whole first Column of each row in the array: %s" %  (mynumpyarray[:,-3]))
 