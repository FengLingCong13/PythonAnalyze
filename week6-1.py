# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:07:16 2019
@author: lenovo
"""
from __future__ import division
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange   #导入拉格朗日插值函数
from pandas import Series,DataFrame
import pandas as pd

#dataframe合并
#1
df1 = DataFrame({'key':['b','b','a','c','a','a','b'],
                 'data1':range(7)})     #dataframe2
df2 = DataFrame({'key':['a','b','d'],
                 'data2':range(3)})     #dataframe1   
df3 = pd.merge(df1,df2) #多对一的合并
print(df3)