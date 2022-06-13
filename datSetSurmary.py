# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 10:21:09 2019

@author: Abayomi-Ali Ayomide
"""
## this will give us peek of data, it will print the specified number of rows of data
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
##Peek = data.head() #this will just print from 0 to 4 rows
#Peek = data.head(20) #this will print 20 rows of the data
#print(Peek)



##This code will give the summary of the data types
#How to get data attribute from data (data type)
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#type =data.dtypes
#print(type)




#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
##urlfile = 'http//myfile.com/file.csv       #This is a sample if you want to import file from the cloud
## How to read  just data shape(number of rows and columns) using pandas or using url using 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
##data =read_csv(urlfile,names=names)     #This will read the data name that has been stated  as a url file    
#shape = data.shape
#print(shape)  






#this code will give a statistics or discription of the data to be analyzed

#from pandas import read_csv
#from pandas import set_option
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#set_option('display.width', 100)
#set_option('precision', 2)
#  #the 2 here can be any number it detrmines the decimal place of the values
#statistics = data.describe() # description = data.descripbe()
#print(statistics)            # print(description )


"""This will count sum total (frequency distribution) of each value 
in each column e.g age , class, bmass etc.  AKA: Class Distribution
"""
#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#
#class_count_age = data.groupby('age').size()
##this will sum up how many individual age occured
#
#class_count_pregnant = data.groupby('pregnant').size()
#
#class_count_plasma = data.groupby('plasma').size()
#
#class_count_bpdia = data.groupby('bpdia').size()
#
#class_count_skin = data.groupby('skin').size()
#
#class_count_bmass = data.groupby('bmass').size()
#
#class_count_class = data.groupby('class').size() 
##this will determine the total number of diabetic & non-diabetic patient.
#
#
#print(class_count_age)
#print("---------------------------------------------------------------")
#print(class_count_pregnant)
#print("---------------------------------------------------------------")
#print(class_count_plasma)
#print("---------------------------------------------------------------")
#print(class_count_bpdia)
#print("---------------------------------------------------------------")
#print(class_count_skin)
#print("---------------------------------------------------------------")
#print(class_count_bmass)
#print("---------------------------------------------------------------")
#print(class_count_class)



# This code will compute the correlation
#from pandas import read_csv
#from pandas import set_option
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#set_option('display.width', 100)
#set_option('precision', 3)   
#correlations = data.corr(method='spearman') 
#there are different methods of correlation we have:kendall or spearman or pearson
#print(correlations)



# THIS WILL SHOW THE SKEWNWSS OF THE DATA.

#from pandas import read_csv
#filename = 'diabete-data.csv' #this will import the data file 
#names = ['pregnant','plasma','bpdia','skin','test','bmass','diapedi','age','class']
#data = read_csv(filename, names=names)
#skewness = data.skew()
#print(skewness)