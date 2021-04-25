'''
Description: numpy项目相关
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2021-04-25 19:49:38
LastEditTime: 2021-04-25 19:57:55
FilePath: /python-libraries/01Numpy/np_project.py
'''
import numpy as np

# 通过下标列表获取np数据
# A = [[ 3  4  5  6]
#  [ 7  8  9 10]
#  [11 12 13 14]]
A = np.arange(3,15).reshape((3,4))

index = np.arange(1,2) # [1]
print(index)
print(A[index])  # [[ 7  8  9 10]]