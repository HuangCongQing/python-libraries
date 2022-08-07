'''
Description:  因为numba内置的函数本身是个装饰器，所以只要在自己定义好的函数前面加个@numba.jit()就行，简单上手。下面以一个求和函数为例 https://www.yuque.com/huangzhongqing/hpc/rmwgv2
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2022-08-07 20:36:27
LastEditTime: 2022-08-07 20:36:29
FilePath: /python-libraries/07numba/01for循环对比测试.py
'''
import numba


# 用numba加速的求和函数
@numba.jit()
def nb_sum(a):
    Sum = 0
    for i in range(len(a)):
        Sum += a[i]
    return Sum

# 没用numba加速的求和函数
def py_sum(a):
    Sum = 0
    for i in range(len(a)):
        Sum += a[i]
    return Sum


from timeit import timeit
import numpy as np
a = np.linspace(0,100,100) # 创建一个长度为100的数组

time1 = timeit(stmt='py_sum(a)', setup='import numpy as np;a = np.linspace(0,100,100);from __main__ import py_sum', number=1) # (__main__表示当前的文件)。
print(time1)
# timeit(np.sum(a) )# numpy自带的求和函数
# timeit(sum(a)) # python自带的求和函数
# timeit(nb_sum(a)) # numba加速的求和函数
# timeit(py_sum(a)) # 没加速的求和函数