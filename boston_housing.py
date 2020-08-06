# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:27:15 2019

@author: Administrator
"""
from jupyter_core.paths import jupyter_data_dir, jupyter_runtime_dir, secure_write

'''
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
for feature in features.columns:
    features['标准化'+feature] = scaler.fit_transform(features[[feature]])
    
font={
      'family':'SimHei'
      }
matplotlib.rc('font', **font)
pd.plotting.scatter_matrix(features[['标准化RM', '标准化PTRATIO', '标准化LSTAT ']], alpha=0.7, figsize=(6,6), diagonal='hist')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('D:\\download\\boston_housing-master\\housing.csv')
prices = data['MEDV']
#features = data.drop('MEDV', axis = 1)
features = data[['RM', 'PTRATIO', 'LSTAT ']]
pd.plotting.scatter_matrix(features, alpha=0.7, figsize=(6,6), diagonal='hist')


pd.plotting.scatter_matrix(data, alpha=0.7, figsize=(10,10), diagonal='kde')   
# 完成

print("Boston housing dataset has {} data points with {} variables each.".format(*data.shape))

prices.describe()

#目标：计算价值的最小值
minimum_price = np.min(prices)# prices.min()

#目标：计算价值的最大值
maximum_price = np.max(prices)# prices.max()

#目标：计算价值的平均值
mean_price = np.mean(prices)# prices.mean()

#目标：计算价值的中值
median_price = np.median(prices)# prices.median()

#目标：计算价值的标准差
std_price = np.std(prices)# prices.std()

#目标：输出计算的结果
print ("Statistics for Boston housing dataset:\n")
print ("Minimum price: ${:,.2f}".format(minimum_price))
print ("Maximum price: ${:,.2f}".format(maximum_price))
print ("Mean price: ${:,.2f}".format(mean_price))
print ("Median price ${:,.2f}".format(median_price))
print ("Standard deviation of prices: ${:,.2f}".format(std_price))
'''