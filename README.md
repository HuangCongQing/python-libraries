# python-libraries
python库(numpy,pandas...)学习

加载github jupyter文件网址：https://nbviewer.jupyter.org/

注：开始用py文件写的，后面用的jupyter写的，可以写文档，更方便日后看，更容易看懂！
**环境： win7 python35**

# libraries

#### [01Numpy](./01Numpy)

* 矩阵运算

1. [学习莫凡讲解视频](https://www.bilibili.com/video/av16378934/)

```
C =np.concatenate((A,B,B,A),axis=0) #行操作，纵向合并
print(C)
C =np.concatenate((A,B,B,A), axis=1) #列操作，横向合并
```



####  [02Pandas](./02Pandas)
* 数据分析处理库Pandas，基于Numpy

####  [03Matplotlib](./03Matplotlib)
* 画图-可视化工具

#### [04Seaborn](./04Seaborn)

* Seaborn基于Matplotlib
    * 更简洁的语法
    * 了解df，更轻松从CSV绘制数据
    * 将包含许多行数据的Pandas DataFrames汇总到聚合图表中



#### [05Scikit-learn](./05Scikit-learn)


------------


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
