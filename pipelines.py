# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:32:36 2019

@author: Abayomi-Ali Ayomide
"""

from pandas import read_csv
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import pipeline
from sklearn.pipeline import FeatureUnion
from sklearn.linear_model import LogisticRegression
from sklearn.decomposition import PCA
from sklearn.feature_selection import SelectKBest
#Load the data


#Create feature union
features = []
features.append((‘pca’, PCA(n_conponents=3)))
features.append((‘select_best’, SelectKbest(k=6)))
feature_union = FeatureUnion(features)
# Create pipeline
estimators= []
estimators.append