# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:24:38 2019

@author: Abayomi-Ali Ayomide
"""

import numpy
mylist1= [1,2,3] #Create a simple array
mylist2= [4,5,6]
mynumpyarray1 = numpy.array(mylist1) #Here we convert the array into numpy.
mynumpyarray2 = numpy.array(mylist2)
print("The Addition of the Array is: %s" %(mynumpyarray1 + mynumpyarray2)) 
print("The Multiplication of the Array is: %s" % (mynumpyarray1 * mynumpyarray2))
print("The Division of the Array is: %s" %(mynumpyarray1 / mynumpyarray2))
print("The Subtraction of the Array is: %s" %(mynumpyarray2 -  mynumpyarray1))



""" To perform arithmethic operation on numpy array
     Create the different list, convert it to numpy arrays and perform the aritmetic
     operations """

#import numpy
#myCat = numpy.array([[1,2,3],[4,5,6]])
#myGoat = numpy.array([[4,5,6],[7,8,9]])
#print("\n\n")
#print("The Addition of the Array is: ", (myCat + myGoat)) #Print using comma sting interpolation 
##Print using % operator sting interpolation 
#print("The Multiplication of the Array is: %s" %(myCat * myGoat))
#print("The Division of the Array is: %s" %(myCat / myGoat))
#print("The inverse Division of the Array is: %s" %(myGoat / myCat)) # note****
#print("The Subtraction of the Array is: %s" %(myCat -  myGoat))
#
