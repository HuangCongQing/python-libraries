<!--
 * @Description: 
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2021-06-09 10:04:04
 * @LastEditTime: 2022-03-17 19:24:17
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
conda env create -f environment.yml -p /home/user/anaconda3/envs/env_name
### example
conda env create -f environment.yml -p /home/user/anaconda3/envs/ssd

```


##  yaml目录

```
├── py36_common.yml
├── py36_tf1.11.yml
├── py36_torch1.2_cuda10.0.yml   pcdet
└── py36_torch1.4.yml

```

## py36_torch1.4(torch pcdet)



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

## python37_torch1.5_20220317.yml(open-mmlab)
py37_torch1.5
open-mmlab


