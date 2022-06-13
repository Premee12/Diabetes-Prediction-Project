# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:30:50 2019

@author: Abayomi-Ali Ayomide
"""

"""
How to load csv file on NUMPY
and use the function called READER() 
importing Numpy is a must
"""
#import csv
#import numpy 
#from numpy import loadtxt
#filename = 'diabete-data.csv' #this will import the data file 
#raw_data = open(filename, 'rt') # just like importing a txt file
#reader = loadtxt(raw_data, delimiter= ',') #the reader here can be any name
#print(reader.shape)
#print(reader)
      #         OR
#import csv
#import numpy
#from numpy import loadtxt
#raw_data = open('diabete-data.csv', 'rt')
#reader = loadtxt(raw_data, delimiter= ',')
#print(reader.shape)



"""
How to load csv file on PANDAS
and use the function called READER() 
importing Numpy is a must
"""
#import csv
#import numpy
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#reader = read_csv(filename, names=names)
#peek = reader.head(100) #this display the file starting from 0 to 99 for 100 data
#print(peek)         #OR
##print(reader.head(100))
#print(reader.shape)

##    OR 
#import csv
#import numpy
#from pandas import read_csv
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#reader = read_csv('diabete-data.csv', names=names)
#print(reader)
#print(reader.head(10))
#print(reader.shape)

# OR USING ANOTHER CSV DATA

#from pandas import read_csv
#names = ['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','black','lstat','medv']
#reader = read_csv('Boston.csv', names=names)
#print(reader)
#print(reader.head(10))
#print(reader.shape)



# Without listing the NAMES, How to read CSV data using pandas or using url link  
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
##urlfile = 'http//myfile.com/file.csv'       #This is a sample if you want to import file from the cloud
 # OR
#data = read_csv(filename)
##data =read_csv(urlfile,names=names)     #This will read the data name that has been stated  as a url file    
#shape = data.shape
#print(shape)  
#print(data)


#How to get data attribute from data
#import csv
#import pandas
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#type =data.dtypes
#print(type) 
## OR 
#print(data.dtypes)


'''
DESCRIPTIVE DATA STATISTICS
'''
# import pandas
#from pandas import read_csv
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#reader = read_csv('diabete-data.csv', names=names)
#pandas.set_option('display.width', 100)
#pandas.set_option('precision', 4) #to round up the decimal values to 3dp (float)
## this code will print the statistics or description of the data
#description = reader.describe()
#print(description)

# OR
#import pandas
#from pandas import read_csv 
#reader = read_csv('Boston.csv')
#pandas.set_option('display.width', 100)
#pandas.set_option('precision', 3) #to round up the decimal values to 3dp (float)
#
#description = reader.describe()
#print(description)
#


'''
WORKING WITH CORRELATION 
#'''
import pandas
from pandas import read_csv
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#names = ['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','black','lstat','medv']

baby = read_csv('diabete-data.csv', names=names)
#baby = read_csv('Boston.csv', names=names)

pandas.set_option('display.width', 100)
pandas.set_option('precision', 3)
correlations = baby.corr(method='pearson') # we have 3 methods they are: pearson, kendall, spearman
print(correlations)
#




'''
THIS WILL COUNT A SPECIFIC COLUNM NAMED "CLASS" 
AND GROUP THE NUMBER OF 0's and 1's 

FOR THE SECOND CODE IT WILL GROUP THE TOTAL AMOUNT OF TIME A PARTICULAR 
NUMBER OCCURED IN COLUNM "RAD" 
'''
#import pandas
#from pandas import read_csv
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#ayomide = read_csv('diabete-data.csv', names=names)
#class_counts = ayomide.groupby('class').size()
## we can also group another row using the same code to check the number of occurence
##countskin = ayomide.groupby('skin').size()
##print(countskin)
#print(class_counts)

# OR

#import pandas
#from pandas import read_csv
#names = ['crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio','black','lstat','medv']
#ayomide = read_csv('Boston.csv', names=names)
#rad_counts = ayomide.groupby('rad').size()
#print(rad_counts)





"'' WORKING WITH SKEWNESS "''
import pandas
from pandas import read_csv
names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
ayomide = read_csv('diabete-data.csv', names=names)
skew = data.skew()
print(skew)

