<!--
 * @Description: 
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2021-06-09 10:04:04
 * @LastEditTime: 2022-08-30 19:56:38
 * @FilePath: /python-libraries/anaconda_environments/anaconda_environments.md
-->

# Into

* 虚拟环境配置：https://www.yuque.com/huangzhongqing/efgg5d/kqgvck

```
# 导出
conda env list    查找所有环境

source activate common 激活进入到所要导出的环境中

conda env export --file  path/python36_20190106.yml   导出到yml文件
# 个人例子
conda env export --file  /home/hcq/pointcloud/python-libraries/anaconda_environments/py36_common.yml
conda env export --file  /home/hcq/pointcloud/python-libraries/anaconda_environments/py36_tf.yml
conda env export --file  /home/hcq/pointcloud/python-libraries/anaconda_environments/py36_torch.yml

## 导入(先退出其他环境，包括base)

conda env create -f environment.yml

# 指定环境安装路径
conda env create -f environment.yml -p ~/anaconda3/envs/env_name
### example
conda env create -f environment.yml -p ~/anaconda3/envs/ssd

```


##  yaml目录

```
├── py36_common.yml
├── py36_tf1.11.yml
├── py36_torch1.2_cuda10.0.yml   pcdet
└── py36_torch1.4.yml

```

## py36_torch1.4(torch pcdet)
anaconda_environments/py36_torch1.4.yml
* torch1.4
* cuda10.1
* spconv1.2

## py36_torch1.2_cuda10.0.yml  （SSD）
* ssd代码环境：https://github.com/HuangCongQing/ssd-pytorch

```
scipy==1.2.1
numpy==1.17.0
matplotlib==3.1.2
opencv_python==4.1.2.30
torch==1.2.0
torchvision==0.4.0
tqdm==4.60.0
Pillow==8.2.0
h5py==2.10.0

```

## py37_torch1.5_20220317.yml(open-mmlab)
py37_torch1.5
open-mmlab


## torch1.5_cuda10.2_spconv1.2(py37) 未验证
* centerpoint

```
conda create -n centerpoint python=3.7

conda install pytorch==1.5.0 torchvision==0.6.0 cudatoolkit=10.2 -c pytorch


```

## torch1.9_cuda11.1_spconv111_py38.yaml (pcdet-mayavi已安装) 20220503

* Ubuntu 20.04(cuda11.4)  **注意，本电脑自己安装的cuda11.4**
* python 3.8
* pytorch 1.9
* CUDA 11.1（pytorch 没有支持cuda11.4的）

https://www.yuque.com/huangzhongqing/hre6tf/kdsn8f


```
#创建指定python版本下包含某些包的环境
conda create --name pcdet python=3.8 numpy scipy

pip install torch==1.9.1+cu111 torchvision==0.10.1+cu111 torchaudio==0.9.1 -f https://download.pytorch.org/whl/torch_stable.html

# CUDA 11.1  spconv
pip install spconv-cu111

```

## py38_torh1.10.1_waymo_38_202208.yml(waymo) 202208


## mmmdetection3d

