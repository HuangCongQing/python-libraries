'''
Description: numpy属性
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2020-11-16 11:52:49
LastEditTime: 2021-06-09 09:51:33
FilePath: /python-libraries/01Numpy/21numpy属性.py
'''
import numpy as np

array1 = np.array([[1, 2, 3],
                   [3, 4, 5]])  # 列表转化为矩阵

print(array1)
print('几维number of dim:', array1.ndim)
print('shape:', array1.shape)
print('size:', array1.shape)
print('dytpe:', array1.dtype)
