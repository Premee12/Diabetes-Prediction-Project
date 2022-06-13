# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:33:53 2019

@author: Abayomi-Ali Ayomide
"""
#WORKING WITH MATPLOTLIB FOR PLOTTING GRAPH.

import matplotlib.pyplot as plt #import the matplotlib and save it as plt
import numpy #import NUMPY library
arraylist = [3,8,9,10,12]
myarray = numpy.array(arraylist) #put the array into numpy
#myarray = numpy.array([3,8,9,10,12]) #This is a faster approach of accessing the numpy array 
#line 12 will save the stress of line 10 and 11.
plt.plot(myarray) # Now plot the numpy array.
plt.xlabel('This is x axis') #this will be ritten on the side of the x-axis
plt.ylabel('This is y axis') #this will be ritten on the side of the y_axis
plt.show()

#
#THIS WILL PLOT TWO ARRAYS ON THE SAME LINE PLOT GRAPH (Y AXIS)
#import matplotlib.pyplot as plt #import the matplotlib and save it as plt
#import numpy #import NUMPY library
#myarray = numpy.array([[2,4,6,],[5,10,15,]]) #put the array into numpy
#plt.plot(myarray)
#plt.xlabel('This is x axis')
#plt.ylabel('This is y axis')
#plt.show()


#import matplotlib.pyplot as plt
#import numpy
#Ayomide = numpy.array([[4,6,8],[6,9,12],[10,15,20]])
#plt.plot(Ayomide)
#plt.xlabel("This is x axis")
#plt.ylabel("This is y axis")
#plt.show()