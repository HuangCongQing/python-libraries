'''
Description: sin cos可视化
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2024-09-12 14:32:41
LastEditTime: 2024-09-12 14:50:18
FilePath: /python-libraries/03Matplotlib/08sincos_vis.py
'''
import numpy as np
import matplotlib.pyplot as plt

max_value = 1.0
# 生成数据
x = np.arange(0, 1, 0.01) # 以0.1为单位，生成从0到6的数据
y1 = max_value * 0.5 * np.sin(np.pi * x)
y2 = max_value * 0.5 * (1 + np.cos(np.pi * x))
cur_vaule = 0.5
print("sin: ", max_value * np.sin(np.pi * cur_vaule))
print("cos: ", max_value * np.cos(np.pi * cur_vaule))

# 绘制图形
plt.figure(dpi=128, figsize=(10, 6)) # 窗口大小
plt.plot(x, y1, c='red', label='sin')
plt.plot(x, y2, c='blue', linestyle='--', label='cos')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('sin & cos', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)
plt.legend() # 显示图例参数
plt.show()