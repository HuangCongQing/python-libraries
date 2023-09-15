'''
Description:  保存proto数据成文件
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-09-12 10:49:26
LastEditTime: 2023-09-15 17:09:53
FilePath: /python-libraries/08protobuf/write_proto.py
'''
from testProto.person_pb2 import one
import numpy as np

# 设置参数
def setInfo(a_info):
    # 
    a_info.id = 1
    # 如果遇到protobuf文件引用的情况，访问字段时必须一层一层访问
    a_person = a_info.people   #实例？？？
    a_person.age = 88
    a_person.name = "first_name"
    # 
    score1 = a_person.score.add()
    score1.object = "python"
    score1.score = 90
    score2= a_person.score.add()
    score2.object = "c++"
    score2.score = 88
    # 
    phone = a_person.number
    phone.phone = 400100
    phone.type = 2
    # print(a_info)
    return a_info


# 获取数据
def getInfo(wanted_info):
    wanted_id = wanted_info.id
    print("info id:", wanted_id)
    print("his age: ", wanted_info.people.age)
    for sco in wanted_info.people.score:
        print("his scores:",sco)
    print("his phoneType:", wanted_info.people.number.type)
    if wanted_info.people.number.type == wanted_info.people.PhoneType.HOME:
        print("his phonetype: HOME")

# 传入数据
# first_info = testProto.person_pb2.one()
first_info = one()
one_info = setInfo(first_info) # 填充数据
print("传入数据:", one_info)
proto_info_msg = one_info.SerializeToString() # 序列成字符串(二进制)
print("序列成字符串(二进制):", proto_info_msg)
np.save("filename.npy",proto_info_msg) #<<<<<<<<<<<<<<<<<<<<<<<保存二进制