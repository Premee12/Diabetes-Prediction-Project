# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:30:50 2019

@author: Abayomi-Ali Ayomide
"""

"""
LOADING CSV USING NUMPY
How to load csv file on NUMPY
and use the function called LOADTXT() 
importing Numpy is a must
"""


#import numpy
#from numpy import loadtxt
#filename = 'diabete-data.csv' #this will import the data file 
#raw_data = open(filename, 'rt') # just like importing a txt file
#reader = loadtxt(raw_data, delimiter= ',')
#print(reader.shape)
#print(reader)

###               OR USING ANOTHER CSV DATA

#import numpy
#from numpy import loadtxt
#filename = 'Boston.csv' #this will import the data file 
#raw_data = open(filename, 'rt') # just like importing a txt file
#reader = loadtxt(raw_data, delimiter= ',')
#print(reader.shape)
#print(reader)



"""
LOADING CSV USING PANDAS
How to load csv file on PANDAS
and use the function called READ_CSV() 
importing Numpy is a must
"""
#this wiil read a specific rows and display
#import csv
#import numpy
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#reader = read_csv(filename) 
## WE CANNOT USE 'rt' HERE BECOZ WE JUST NEED TO INCLUDE A LIST OF THE NAMES OF COLUMN.
#ayo = reader.head(100) #this display the file starting from 0 to 19 for 20 data
#print(ayo)         #OR
##print(reader.head(100))
#print(reader.shape)
#print(reader)

                #OR THE  BEST WAY
        #THIS WILL DISPLAY EACH NAMES FOR COLUNMS:

#import numpy
from pandas import read_csv
filename = 'diabete-data.csv' #this will import the data file 
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
reader = read_csv(filename, names=names)
peek = reader.head(100) #this display the file starting from 0 to 100 of the data
# WE USE PEEK BCOX PEEK IS USED TO TAKE A QUICK GLANCE AT THE DATA.    
print(peek)         #OR
#print(reader.head(100))
print(reader.shape)



