import numpy as np

a = np.array([[1,2,3],
 [3,4,5]],dtype=np.int) # 列表转化为矩阵

print(a)
print(a.dtype)  # np.int,np.float32


z = np.zeros((3, 4))
print(z)


z1 = np.ones((3, 4),dtype=np.int16)
print(z1)

z2 = np.empty((3, 4))
print(z2)


b = np.arange(10, 20, 2)
print(b)

# 3行3列
c = np.arange(12).reshape((3, 4))
print(c)


# 线段

d = np.linspace(1, 10, 12,dtype=np.int16)
print(d)