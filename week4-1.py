# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:01:51 2019

@author: lenovo
"""

from __future__ import division
from numpy.random import randn
import numpy as np

#通用函数
arr = np.arange(10)
#print(np.sqrt(arr)) #求平方根


x = randn(8)    #8个随机服从正态分布对的数字
y = randn(8)

#print(np.maximum(x, y)) #元素级最大值

arr = randn(7)*5
#print(arr)
#print(np.modf(arr)) #将整数部分和小数部分区分开

#利用数组进行数据处理
#向量化
points = np.arange(-5,5,0.01)
xs, ys = np.meshgrid(points,points)  #分别进行赋值
print(xs)
print(ys)

import matplotlib.pyplot as plt
z=np.sqrt(xs**2+ys**2)
print(z)
plt.imshow(z,cmap=plt.cm.gray);plt.colorbar()
plt.title("Image plot of gray")
plt.draw()


#将条件逻辑表达为数组运算
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result=np.where(cond,xarr,yarr)  #如果是True就选择xarr，如果是False就选择yarr
print(result)

arr=randn(4,4)
result=np.where(arr>0,2,-2)
print(result)
result=np.where(arr>0,2,arr)
print(result)#如果为False就保持不变


#数学与统计方法
arr=randn(5,4)
print(arr.mean())#求均值
print(arr.sum()) #求和

arr=np.array([[0,1,2],[3,4,5],[6,7,8]])
print(arr)
print(arr.cumsum(1))#计算累计和   0的话行累加，1的话列累加
print(arr.cumprod(1))#计算累计鸡


#用于布尔型数组的方法
arr=randn(100)
print((arr > 0).sum()) #正值的数量

bools = np.array([False,False,True,False])
print(bools.any())  #是否存在一个为真
print(bools.all())  #是否都是真的


#排序
arr=randn(8)
arr.sort()
print(arr)


arr=randn(5,3)
arr.sort(1)#按照行进行排序
print(arr)


#唯一化以及其他的逻辑集合
names=np.array(['Bob','Joe','Will','Bob','Joe'])
print(np.unique(names))  #返回唯一一个元素
ints = np.array([3,3,2,1,4,5,1,3,2])
print(np.unique(ints))

values=np.array([6,0,0,3,2,5,6])
print(np.in1d(values,[2,3,6]))  #一个数组中的元素是否在另一个数组里面


#线性代数
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[6,23],[-1,7],[8,9]])
print(x.dot(y)) #矩阵相乘


from numpy.linalg import inv,qr   #计算线性代数矩阵的标准库
x=randn(5,5)
mat = x.T.dot(x)


#随机数生成
samples = np.random.normal(size=(4,4)) #4*4的随机数服从正态分布
print(samples)
