'''
Description: proto测试 https://www.yuque.com/huangzhongqing/lang/mb3v5givoev1m2n7#PVIOJ
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-09-12 10:49:26
LastEditTime: 2023-09-15 17:12:46
FilePath: /python-libraries/08protobuf/test_proto.py
'''
#coding=utf-8
# file: test_proto.py

# import testProto.person_pb2
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

# 解析=====================
print("解析=====================")
proto_info_msg = np.load("filename.npy") #<<<<<<<<<<<<<<<<<<<<<<<读取二进制
first_parsed = one() # 定义输出数据
first_parsed.ParseFromString(proto_info_msg) # 从字符串中(二进制)反序列化解析
# print(first_parsed)
getInfo(first_parsed)  # 输出数据