# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:33:53 2019

@author: Abayomi-Ali Ayomide
"""
# WORKING WITH MATPLOTLIB FOR PLOTTING GRAPH.
import matplotlib.pyplot as plt #import the matplotlib and save it as plt
import numpy #import NUMPY library
myarray = numpy.array([3,8,9,10,12]) #put the array into numpy
plt.plot(myarray)
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.show()

