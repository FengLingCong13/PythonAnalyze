# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 15:50:52 2019

@author: lenovo
"""

import matplotlib.pyplot as plt


###matplotlib创建图表

###figure与subplot

#figure对象
fig = plt.figure()      #figure是图象对象

ax1 = fig.add_subplot(2,2,1)    #创建一个2*2的子图，放在第一个位置
ax2 = fig.add_subplot(2,2,2)    #创建一个2*2的子图，放在第二个位置
ax3 = fig.add_subplot(2,2,3)    #创建一个2*2的子图，放在第三个位置

from numpy.random import randn
plt.plot(randn(50).cumsum(),'k--')    #'k--'告诉python要画出黑色的虚线
ax1.hist(randn(100),bins=20,color='k',alpha=0.3)

import numpy
#调整subplot周围的间距
fig,axes = plt.subplots(2,2,sharex=True,sharey=True)    #直接生成fiure对象和Axes实例(数组)
for i in range(2):
    for j in range(2):
        axes[i, j ].hist(numpy.random.randn(500),bins = 50,color='k',alpha=0.5)     #遍历创建图
plt.subplots_adjust(left=None,bottom=None,right=None,top=None,wspace=0,hspace=0)   #用于调整subplot周围的间距


#matplotlib基本设置
#颜色、标记和线型
#plt.figure()
##linestyle设置线型，color设置颜色,marker设置设置连接点
#plt.plot(numpy.random.randn(30).cumsum(),linestyle='--',color='g',marker='o')


#设置标题、轴标签，刻度以及刻度标签
fig = plt.figure()      #创建figure对象
ax = fig.add_subplot(1,1,1)     #获得Axes对象
ax.plot(numpy.random.randn(1000).cumsum())  #生成随机数
ax.set_xticks([0,250,500,750,1000])     #设置x轴刻度
ax.set_yticks([-20,-10,0,10,20])        #设置y轴刻度
ax.set_title('My first matplotlib plot')    #设置标题
ax.set_xlabel('Xtages')     #设置x轴标签
ax.set_ylabel('Ytages')     #设置y轴标签

#添加图例
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(numpy.random.randn(1000).cumsum(),'k',label='one')  #label标签用于添加图例
ax.plot(numpy.random.randn(1000).cumsum(),'k',label='two')
ax.plot(numpy.random.randn(1000).cumsum(),'k',label='three')

ax.legend(loc='best')       #loc选项可以选择图例的位置

#添加注释
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(numpy.random.randn(1000).cumsum(),'k',label='one')  #label标签用于添加图例
plt.annotate("Important value", (55,20), xycoords='data',   #添加注释的方法
         xytext=(5, 38),
         arrowprops=dict(arrowstyle='->'))

#绘制常用图形
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rect = plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)   #长方形
circ = plt.Circle((0.7,0.2),0.15,color='b',alpha=0.3)           #椭圆形

ax.add_patch(rect)      #添加到图版中
ax.add_patch(circ)

#图标的保存
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
rect = plt.Rectangle((0.2,0.75),0.4,0.15,color='k',alpha=0.3)   #长方形
ax.add_patch(rect)      #添加到图版中
fig.savefig('figpath.png',dpi = 400,bbox_inches='tight')  #dpi可以控制图象的分辨率,bbox_inches可以剪除图表的空白部分
