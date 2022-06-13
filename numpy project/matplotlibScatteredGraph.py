# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:24:23 2019

@author: Abayomi-Ali Ayomide
"""


""" Scatter graph is used to plot the graph of X againgst y
     it can on consist of just two arrays where one is X axis
         and the other is y axis
 """
  # WORKING WITH MATPLOTLIB FOR PLOTTING GRAPH.
import matplotlib.pyplot as plt #import the matplotlib and save it as plt
import numpy #import NUMPY library
myarray1= numpy.array([1,2,3,5])
myarray2= numpy.array([2,4,6,7])
plt.scatter(myarray1,myarray2)
plt.xlabel('This is x axis')
plt.ylabel('This is y axis')
plt.show()
#


#Another example



#import matplotlib.pyplot as plt
#import numpy 
#Ayomide = numpy.array([2,5,9])
#Temidayo = numpy.array([5,10,15])
#plt.scatter(Ayomide,Temidayo,)
#plt.xlabel('This is x axis')
#plt.ylabel('This is y axis')
#plt.show()