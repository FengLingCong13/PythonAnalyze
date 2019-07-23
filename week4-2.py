# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 17:13:44 2019

@author: lenovo
"""

#利用numpy进行历史股分析
import sys
import numpy as np

#读入文件
c,v=np.loadtxt('E:\\建模\\第4周\\data.csv',delimiter=',',usecols=(6,7),unpack=True)  #unpack代表分开赋值

#计算成交量的加权平均价格
vwap = np.average(c, weights=v)
#print(vwap)

#算数平均数
#print(np.mean(c))

#时间加权平均价格
t = np.arange(len(c))
#print(np.average(c,weights=t))

#寻找最大值和最小值
h,l=np.loadtxt('E:\\建模\\第4周\\data.csv',delimiter=',',usecols=(4,5),unpack=True)
#print(np.max(h))
#print(np.min(l))

#统计分析

#中位数
c=np.loadtxt('E:\\建模\\第4周\\data.csv',delimiter=',',usecols=(6,),unpack=True)
  #print(np.median(c))
#数据进行排序
#print(np.msort(c))

#计算总体方差
#print(np.var(c))

#日期分析
from datetime import datetime
def datestr2num(s):
    return datetime.strptime(s,"%d-%m-%Y").date().weekday()
dates,closes=np.loadtxt('E:\\建模\\第4周\\data.csv',delimiter=',',usecols=(1,6),converters={1:datestr2num},unpack=True)
print(dates)