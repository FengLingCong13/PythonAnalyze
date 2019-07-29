# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:34:54 2019

@author: lenovo
"""

import xlrd
import numpy as np
import matplotlib.pyplot as plt

#从excel文件中读取数据
def read(file):
    wb = xlrd.open_workbook(filename=file)#打开文件
    sheet = wb.sheet_by_index(1)#通过索引获取表格
    all_content = []        #存放读取的数据
    temp = []
    
    for i in range(4,12) :
        for j in range(2,10):    
            cell = sheet.cell_value(i, j)   #获取数据 
            temp.append(cell)           
        all_content.append(temp)    #按列添加到结果集中
        temp = []
    return np.array(all_content)


def deal(X,Y):
    print(X)
    print(Y)
#    X=np.arange(-np.pi,np.pi,1) #定义样本点X，从-pi到pi每次间隔1
#    Y= np.sin(X)#定义样本点Y，形成sin函数
    new_x=np.array([2,4,6,8,10,12,14]) #定义差值点
     
    #进行样条差值
    import scipy.interpolate as spi
     
    #进行一阶样条差值
    ipo1=spi.splrep(X,Y,k=1) #源数据点导入，生成参数
    iy1=spi.splev(new_x,ipo1) #根据观测点和样条参数，生成插值
     
    #进行三次样条拟合
    ipo3=spi.splrep(X,Y,k=3) #源数据点导入，生成参数
    iy3=spi.splev(new_x,ipo3) #根据观测点和样条参数，生成插值
    
    return iy1
     
     
#    ##作图
#    fig,(ax1,ax2)=plt.subplots(2,1,figsize=(10,12))
#    
#    ax1.plot(X,Y,'o',label='样本点')
#    ax1.plot(new_x,iy1,label='插值点')
#    ax1.set_ylim(Y.min()-1,Y.max()+1)
#    ax1.set_ylabel('指数')
#    ax1.set_title('线性插值')
#    ax1.legend()
#    
#    ax2.plot(X,Y,'o',label='样本点')
#    ax2.plot(new_x,iy3,label='插值点')
#    ax2.set_ylim(Y.min()-1,Y.max()+1)
#    ax2.set_ylabel('指数')
#    ax2.set_title('三次样条插值')
#    ax2.legend()

answer1 = read('C:\\Users\\lenovo\\Desktop\\数学建模\\插值法\\第3讲.插值算法7.17\\扩展资料\\第六届MathorCupA题题目和特等奖论文\\题目\\附件1-附件7.xls')
answer3 = []
#for i in range(0,8):
#    answer2 = deal(np.array([1,3,5,7,9,11,13,15]),answer1[i])
#    answer3.append(answer2)
answer2 = deal(np.array([1,3,5,7,9,11,13,15]),answer1[1])    
print(answer2)