# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 10:14:14 2019

@author: lenovo
"""
import numpy as np
from scipy.stats import t     #导入t分布函数
import matplotlib.pyplot as plot
import xlrd
from scipy.stats import pearsonr 
from scipy.stats import spearmanr


#假设检验部分
def judge():
    x = np.arange(-4,4,0.1)
    y = t.pdf(x,28) #产生t分布的概率密度函数，28是自由度
    fig = plot.figure()  #获得figure对象
    ax1 = fig.add_subplot(1,1,1)    #添加一个图纸
    ax1.plot(x,y)
    tppf = t.ppf(0.975,28)    #ppf求累计密度函数的反函数，
    ax1.plot([-tppf,-tppf],[0,t.pdf(-2.048,28)])    #pdf就是求累计密度函数
    ax1.plot([tppf,tppf],[0,t.pdf(2.048,28)])       #pdf就是求累计密度函数
    ax1.set_ylim([0,0.5])    #设置y轴刻度

#计算p值
def calculate():
    x = np.arange(-4,4,0.1)
    y = t.pdf(x,28) #产生t分布的概率密度函数，28是自由度
    fig = plot.figure()  #获得figure对象
    ax1 = fig.add_subplot(1,1,1)    #添加一个图纸
    ax1.plot(x,y)
    tppf = t.ppf(0.975,28)    #ppf求累计密度函数的反函数，
    ax1.plot([-tppf,-tppf],[0,t.pdf(-2.048,28)])    #pdf就是求累计密度函数
    ax1.plot([tppf,tppf],[0,t.pdf(2.048,28)])       #pdf就是求累计密度函数
    ax1.set_ylim([0,0.5])    #设置y轴刻度
    print("该检验值对应的p值是:",1-t.cdf(3.055,28)*2)    #双侧检验要乘以2
    
#从excel文件中读取数据
def read(file):
    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet = wb.sheet_by_index(0)#通过索引获取表格
    rows = sheet.nrows # 获取行数
    all_content = []        #存放读取的数据
    for j in range(0, 6):       #取第1~第6列对的数据
        temp = []
        for i in range(1,rows) :
            cell = sheet.cell_value(i, j)   #获取数据 
            temp.append(cell)           
        all_content.append(temp)    #按列添加到结果集中
        temp = []
    return np.array(all_content)
#calculate()
file='C:\\Users\\lenovo\\Desktop\\数学建模\\相关系数\\第5讲.相关系数7.17\\代码和例题数据\\八年级女生体测数据.xlsx'
R,P = spearmanr(read(file))
np.correlate
print(R)
print(P)  
 
