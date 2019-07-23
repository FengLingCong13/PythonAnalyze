# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 16:50:45 2019

@author: lenovo
"""
#生成Excel工作簿
import xlrd,xlwt
import numpy

wb = xlwt.Workbook()    #生成工作簿

ws_3 = wb.add_sheet('third_sheet')  #生成第一个工作表
ws_4 = wb.add_sheet('forth_sheet')  #生成第二个工作表

data = numpy.arange(1,65).reshape((8,8))    #生成一组数据

for c in range(data.shape[0]):
    for r in range(data.shape[1]):
        ws_3.write(r,c,data[c,r])
        ws_4.write(r,c,data[r,c])
