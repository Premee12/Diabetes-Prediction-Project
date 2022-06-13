# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 13:33:15 2019

@author: Abayomi-Ali Ayomide
"""

from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
filename = 'churn-dat.csv' #this will import the data file 
names = ['area_len','area_code','phone_no','num_vmail_messages','total_day_mins','total_day_call','total_day_charge','total_eve_mins','total_eve_calls''total_eve_charge','total_night_mins','total_night_calls','total_night_charge','total_intl_mins','total_intl_calls','total_intl_charge','customer_service','churn']
dataframe = read_csv(filename, names=names)
#array = dataframe.values
##Split the data into input and output variables
#X = array[:,0:16]
#Y = array[:,16]
#scaler = MinMaxScaler(feature_range=(0,1))
#rescalex = scaler.fit_transform(X)
#set_printoptions(precision=3)
#print(rescalex[0.5,:])
print(dataframe)
