# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:01:54 2019

@author: lenovo
"""

import numpy as np

#  建立平均随机一致性指标R.I
RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}

def get_w(array):
    print('' * 50)
    print('*' * 50)
    print('我是炫酷的分割线')
    print('-' * 50)
    print('' * 50)
    # 1、计算出阶数 看这个数组是几维的 也就是后面对应字典查询！
    row = array.shape[0]  
    # 2、按列求和
    a_axis_0_sum = array.sum(axis=0) 
    # 3、得到新的矩阵b 就是把每一个数都除以列和 
    b = array / a_axis_0_sum  
    # 4、计算新矩阵b行和
    b_axis_1_sum = b.sum(axis=1)  
    # 5、将b_axis_1_sum每一个值除以总和
    W = b_axis_1_sum / sum(b_axis_1_sum)
    # 6、将原始矩阵乘以W
    a_W = np.dot(array, W)
    # 7、求解最大特征值 
    lambda_max = 0
    for i in range(len(a_W)):
        lambda_max += (a_W[i] / W[i])
    lambda_max = lambda_max / len(a_W)
    # 8、检验判断矩阵的一致性
    C_I = (lambda_max - row) / (row - 1)
    R_I = RI_dict[row] 
    C_R = C_I / R_I 
    if C_R < 0.1:
        print('矩阵 %s 一致性检验通过' % (array))
        print('判断矩阵对应的指标的权重为：%s' % W)
        print('判断矩阵对应的最大特征值为 %.2f' % lambda_max)
        print('大功告成！！！')
        return W
    else:
        print('矩阵 %s 一致性检验未通过，需要重新进行调整判断矩阵' % (array))
    
def main(array):
    if type(array) is np.ndarray:
        return get_w(array)
    else:
        print('请输入正确的numpy对象')


if __name__ == '__main__':
    # 由于地方问题，矩阵我就写成一行了
    # 检验以下判断矩阵的一致性并输出权重
    a = np.array([[1, 1 / 3, 1 / 8], [3, 1, 1 / 3], [8, 3, 1]])
    b = np.array([[1, 3, 6], [1 / 3, 1, 4], [1 / 5, 1 / 2, 1]])
    c = np.array([[1, 1, 3], [1, 1, 3], [1 / 3, 1 / 3, 1]])
    d = np.array([[1, 3, 4], [1 / 3, 1, 1], [1 / 4, 1, 1]])
    e = np.array([[1, 2, 7, 5, 5], [1 / 2, 1, 4, 3, 3], [1 / 7, 1 / 4, 1, 1 / 2, 1 / 3], [1 / 5, 1 / 3, 2, 1, 1], [1 / 5, 1 / 3, 3, 1, 1]])
    f = np.array([[1, 4, 1 / 2], [1 / 4, 1, 1 / 4], [2, 4, 1]])
    
    main(a)
#    main(b)
#    main(c)
#    main(d)
#    main(e)
#    main(f)
