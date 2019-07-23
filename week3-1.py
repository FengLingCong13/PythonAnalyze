# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 22:32:26 2019

@author: lenovo
"""

#向量相加-Python
#def pythonsum(n):
#    a = list(range(n))
#    b = list(range(n))
#    c = []
#    for i in range(len(a)):
#        a[i] = i**2
#        b[i] = i**3
#        c.append(a[i]+b[i])
#    return c
#print(pythonsum(20))

import numpy as np

#向量相加-numpy
def numpysum(n):
    a = np.arange(n)**2
    b = np.arange(n)**3
    c = a + b
    return c
print(numpysum(20))

#numpy数组
a = np.arange(5)
print(a.dtype)
print(a.shape)

#创建多维数组
m = np.array([np.arange(2),np.arange(2)])
print(m)
print(m.shape)
print(m.dtype)

#创建0数组或者空数组
print(np.zeros(10))
print(np.zeros((3,6)))
print(np.empty((2,3,2)))
print(np.arange(15))

#选取数组元素
a = np.array([[1,2],[3,4]])
print(a)
print(a[0,0])
print(a[0,1])
print(a[1,0])
print(a[1,1])


#numpy数据类型
print(np.float64(42))
print(np.int8(42.0))
print(np.bool(42))
print(np.float(True))
print(np.float(False))


#数据类型的转换
arr = np.array([1,2,3,4,5])
print(arr.dtype)
float_arr = arr.astype(np.float64)
print(float_arr.dtype)

arr = np.array([3.7,-1.2,-2.6,0.5,12.9,10.11])
print(arr)
print(arr.astype(np.int32))


#创建自定义数据类型
t = np.dtype([('name',np.str_,40),('numitems',np.int32),('price',np.float32)])
print(t)
itemz = np.array([('Meaning of life',42,3.14),('Butter',13,2.72)],dtype=t)
print(itemz)


#数组与标量的运算
arr = np.array([[1,2,3],[4,5,6]])
print(arr)
print(arr*arr)
print(arr-arr)


print(1/arr)
print(arr**0.5)


#一维数组的索引和切片
a=np.arange(9);
print(a[:7:2])
print(a[3:7])
print(a[::-1])

s = slice(3,7,2)
print(a[s])

s=slice(None, None, -1)
print(a[s])

#多维数组的索引和切片
b= np.arange(24).reshape(2,3,4)
print(b.shape)
print(b)

print(b[0,0,0])
print(b[:,0,0])
print(b[0])
print(b[0,:,:])
print(b[0,...])
print(b[0,1])


print(b[0,1,::2])
print(b[:,1])
print(b[0,:,-1])
print(b[0,::-1,-1])

print(b[::-1])

#布尔型索引
names=np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data=np.random.randn(7,4)
print(names)
print(data)

print(names == 'Bob')
print(data[names == 'Bob'])
print(data[names == 'Bob',2:])

print(names != 'Bob')

mask = (names == 'Bob') | (names == 'Will')
print(mask)
print(data[mask])

data[data < 0] = 0
print(data)

data[names != 'Joe'] = 7
print(data)


#花式索引
arr = np.empty((8,4))
for i in range(8):
    arr[i] = i
print(arr)
print(arr[[4,3,0,0]])


arr = np.arange(32).reshape((8,4))
print(arr)
print(arr[[1,5,7,2],[0,3,1,2]])


#数组转置
#arr = np.arange(15).reshape((3,5))
#print(arr)
#print(arr.T)

#改变数组的维度
arr = np.arange(20).reshape((4,5))
print(arr)
print(arr.flatten())
print(arr.ravel())
arr.shape = (2,5,2)
print(arr)


#组合数组
a = np.arange(9).reshape(3,3)
b = 2*a
#水平组合
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))
#垂直组合
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))
#深度组合
print(np.dstack((a,b)))


oned = np.arange(2)
twice_oned =2*oned
print(np.column_stack((oned,twice_oned)))
print(np.row_stack((oned,twice_oned)))


#数组的分割
a = np.arange(9).reshape(3,3)
print(np.hsplit(a,3))#水平分割
print(np.split(a,3,axis=1))

print(np.vsplit(a,3))
print(np.split(a,3,axis=0))#垂直分割


#数组的转换
b=np.arange(24).reshape(2,12)
print(b.ndim)#二维数组的维数
print(b.size)#数组中元素的总个数

b = np.array([1+1j,3+2j])
print(b.real)
print(b.imag)
b = np.array([1+1j,2+3j])
print(b.tolist())#转换为python的列表
print(b.astype(int))
print(b.astype(complex))
