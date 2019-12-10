import pandas as pd
import numpy as np
df_all = pd.read_csv('./Result.csv') 
from sklearn.model_selection import train_test_split 
train_data, test_data = train_test_split(df, test_size = 0.2, random_state=0)
# step 1: computer the sqrt of all the feature

from math import sqrt

# All of the features of interest
features = ['accommodates','bathrooms','bedrooms','beds','review_scores_rating']
# Compute the square and sqrt of each feature
all_features = []
for feat in features:
    square_feat = feat + '_square'
    sqrt_feat = feat + '_sqrt'
    
    df[square_feat] = df[feat] ** 2
    df[sqrt_feat] = df[feat].apply(sqrt)
    
    all_features.extend([feat, square_feat, sqrt_feat])
# step 2:standardized (mean 0, std. dev. 1)
def standardize(v):
    std = v.std()
    if std == 0:
        return np.zeros(len(v))
    else:
        return (v - v.mean()) / std

# Standardize each of the features
for feature in all_features:
    df[feature] = standardize(df[feature])
# step 3 split the data:
from sklearn.model_selection import train_test_split

train_and_validation, test = train_test_split(df, test_size=0.2, random_state=6)
train, validation = train_test_split(train_and_validation, test_size=0.125, random_state=6)
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
import math
regr = linear_model.LinearRegression()
model=regr.fit(train[all_features], train['price'])