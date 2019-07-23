# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 15:42:05 2019

@author: lenovo
"""

###数据读取
import pandas as pd
from pandas import Series

#读取csv文件的两种方式
f = open('E:/建模/第5周/data/ex1.csv')  #方法一
df = pd.read_csv(f)
print(df)
f.close

f = open('E:/建模/第5周/data/ex1.csv')  #方法二，必须指定分隔符为','，否则会读取失败
df = pd.read_table(f,sep=',')
print(df)
f.close


#根据需要条件读取csv文件
f = open('E:/建模/第5周/data/csv_mindex.csv')  
df = pd.read_csv(f,header=None)     #不需要表头
df = pd.read_csv(f,names=['a','b','c','d','message'])   #添加表头
df = pd.read_csv(f,names=['a','b','c','d','message'],index_col = 'message')   #指定某一列作为行索引
df = pd.read_csv(f,index_col = ['key1','key2'])   #指定多列作为行索引
print(df)
f.close

#利用正则表达式读取不同含有不同分隔符的文件
f = open('E:/建模/第5周/data/ex3.txt')  
df = pd.read_table(f,sep='\s+')
print(df)

#根据需要选择需要读的行
f = open('E:/建模/第5周/data/ex4.csv')  
df = pd.read_table(f,sep=',',skiprows=[0,2,3])  #跳过不想读的行
print(df)

#处理缺失值
f = open('E:/建模/第5周/data/ex5.csv')  
df = pd.read_table(f,sep=',',na_values='world')  #如果数据中有’world’，也会视为缺失值
print(df)

#逐行读取文件
f = open('E:/建模/第5周/data/ex6.csv')  
df = pd.read_table(f,sep=',',nrows=5)  #只读取前面5行
print(df)

#将dataframe数据写入csv文件
f = open('E:/建模/第5周/data/ex5.csv')  
data =  pd.read_csv(f)
data.to_csv('E:/建模/第5周/data/out.csv')   #将dataframe输出到csv文件中
data.to_csv('E:/建模/第5周/data/out.csv',na_rep='ok')   #将缺失值补上‘ok’
data.to_csv('E:/建模/第5周/data/out.csv',header=None)   #不设置表头
data.to_csv('E:/建模/第5周/data/out.csv',columns=['a','b'])   #写出指定的列

#将csv文件读取位Series
f = open('E:/建模/第5周/data/tseries.csv') 
series = Series.from_csv(f,parse_dates=True)
print(series)