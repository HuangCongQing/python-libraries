# python-libraries

python库(numpy,pandas...)学习

加载github jupyter文件网址：https://nbviewer.jupyter.org/

注：开始用py文件写的，后面用的jupyter写的，可以写文档，更方便日后看，更容易看懂！
**环境： win7 python35**

* python基础：https://github.com/HuangCongQing/Python

# libraries

* 虚拟环境安装 ： [anaconda_environments](anaconda_environments)
  * tensorflow=1.11.0
  * torch==1.4.0

#### [01Numpy](./01Numpy)

* 矩阵运算

1. [学习莫凡讲解视频](https://www.bilibili.com/video/av16378934/)

```
C =np.concatenate((A,B,B,A),axis=0) #行操作，纵向合并
print(C)
C =np.concatenate((A,B,B,A), axis=1) #列操作，横向合并
```

#### [02Pandas](./02Pandas)

* 数据分析处理库Pandas，基于Numpy

#### [03Matplotlib](./03Matplotlib)

画图-可视化工具

笔记：ttps://www.yuque.com/huangzhongqing/lang/gv9n6f

菊安酱和菜菜的Python可视化

中文版[数据分析最有用的 Top 50 Matplotlib 图（附完整的Python代码](https://cloud.tencent.com/developer/article/1535159#:~:text=%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E6%9C%80%E6%9C%89%E7%94%A8%E7%9A%84%20Top%2050%20Matplotlib%20%E5%9B%BE%EF%BC%88%E9%99%84%E5%AE%8C%E6%95%B4%E7%9A%84Python%E4%BB%A3%E7%A0%81%EF%BC%89%20%28%E4%B8%8A%29%201%201.%E5%85%B3%E8%81%94,6%206.%E5%8F%98%E5%8C%96%207%207.%E5%88%86%E7%BB%84%208%201.%E6%95%A3%E7%82%B9%E5%9B%BE%209%202.%E5%B8%A6%E8%BE%B9%E7%95%8C%E7%9A%84%E6%B0%94%E6%B3%A1%E5%9B%BE.)

英文原版：[https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/](https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/)


* 代码目录： [03Matplotlib/Python可视化Top50Matplotlib](03Matplotlib/Python可视化Top50Matplotlib)

#### [04Seaborn](./04Seaborn)

* Seaborn基于Matplotlib
  * 更简洁的语法
  * 了解df，更轻松从CSV绘制数据
  * 将包含许多行数据的Pandas DataFrames汇总到聚合图表中

#### [05Scikit-learn](./05Scikit-learn)

---

学习素材：[给深度学习入门者的Python快速教程 - numpy和Matplotlib篇](https://zhuanlan.zhihu.com/p/24309547)

...

### Install

```
# cv2
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple opencv-python



````

---

# 2 Python-module Download

python直接install安装不了一些python包，下载的whl文件集合

### whl文件集合

下载whl链接：https://www.lfd.uci.edu/~gohlke/pythonlibs/

#### python35

* [numpy](./python3/numpy-1.13.3+mkl-cp35-cp35m-win_amd64.whl)
* [scipy](./python3/scipy-1.0.0rc1-cp35-cp35m-win_amd64.whl)
* [xgboost](./python3/xgboost-0.6-cp35-cp35m-win_amd64.whl)
* [matplotlib](./python3/matplotlib-1.5.0-cp35-none-win_amd64.whl)
* [wordcloud](./python3/wordcloud-1.4.1-cp35-cp35m-win_amd64.whl)

### 下载库文件

如果是python2(python2.exe)
`python2 -m pip install 库名`

如果是python3（python3.exe）
`python3 -m pip install 库名`

如果不能下载报错，尝试下面两种方式

### 其他下载库文件两种方式

#### 一、下载whl文件方式

1. 命令行执行
   `pip install wheel `
2. 下载相应版本的lxml后缀为.whl的文件
   https://www.lfd.uci.edu/~gohlke/pythonlibs/
3. 安装

到包含`.whl`的文件夹下，打开命令行窗口
命令行执行

`pip install 文件名.whl`

完成

#### 二、下载库文件安装压缩包

1. 下载对应库文件的压缩包
2. 将压缩包解压到对应位置
3. 安装（解压文件夹里有setup.py）

执行
`python setup.py install`

安装完成

### License

Copyright (c) [ChungKing](https://github.com/HuangCongQing). All rights reserved.

Licensed under the MIT License.
