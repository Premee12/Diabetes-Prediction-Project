# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:40:05 2019

@author: Abayomi-Ali Ayomide
"""

import numpy #import NUMPY library
import pandas #import pandas library
myarray = numpy.array([[4,6,10,12,14],[4,6,10,12,8]]) #put the multi-dimensional array into numpy
rownames = ['a','b'] #Because we have just two rows
colnames = ['x','y','z','p','q']
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

# Ways of accessing the table and printing
print("\nPrinting one Row\n%s\n" %mydataframe[:1]) 
#This will print the rows before the second row in this case it is just one

print("\nPrinting one Column\n%s\n" %mydataframe['y'])
#               OR
print("Printing one Column\n%s\n" %mydataframe.y)

print(mydataframe[:2])
#this will print every row before the third row but we just have two rows so it will print all the rows. 




#TRY YOUR OWN 
#import pandas
#import numpy
#ayomide = numpy.array([[2,4,6,8,10,12],[3,5,7,9,11,15],[1,3,5,6,8,9]])
#rownames = ['i','ii','iii']
#colnames = ['a','b','c','d','e','f']
#ayomidedataframe = pandas.DataFrame(ayomide, index=rownames, columns=colnames)
#print(ayomidedataframe)
#
#
#
