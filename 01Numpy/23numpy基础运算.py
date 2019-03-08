import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a, b)

print(a - b)
print(a ** 2)

print(10 * np.sin(a))

print(b)
print(b < 3)  # [ True  True  True False]

# np.dot矩阵运算结果

c = np.array([
    [1, 2],
    [3, 4]])
d = np.arange(4).reshape((2, 2))
m = c * d
m_dot = np.dot(c, d)  # 矩阵运算
m_dot2 = c.dot(d) # 同上

print(c)
print(d)

print(m)
print('\n矩阵运算\n\n',m_dot)
print('\n矩阵运算\n\n',m_dot2)