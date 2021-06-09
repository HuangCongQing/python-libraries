<!--
 * @Description: 
 * @Author: HCQ
 * @Company(School): UCAS
 * @Email: 1756260160@qq.com
 * @Date: 2021-06-09 10:04:04
 * @LastEditTime: 2021-06-09 10:05:10
 * @FilePath: /python-libraries/anaconda_environments/README.md
-->

```shell
├── py36_common.yml
├── py36_tf.yml
├── py36_torch.yml
└── README.md
```

导出虚拟环境：https://www.yuque.com/huangzhongqing/efgg5d/kqgvck#jfbdF

```shell
conda env list    查找所有环境

source activate common 激活进入到所要导出的环境中

conda env export --file  path/python36_20190106.yml   导出到yml文件
# 个人例子
conda env export --file  /home/hcq/pointcloud/python-libraries/anaconda_environments/py36_common.yml
conda env export --file  /home/hcq/pointcloud/python-libraries/anaconda_environments/py36_tf.yml
conda env export --file  /home/hcq/pointcloud/python-libraries/anaconda_environments/py36_torch.yml
```
