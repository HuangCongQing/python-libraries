'''
Description: 读取文件通过proto输出
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-09-12 10:49:26
LastEditTime: 2023-09-15 17:10:32
FilePath: /python-libraries/08protobuf/read_proto.py
'''

#coding=utf-8
# file: test_proto.py

# import testProto.person_pb2
from testProto.person_pb2 import one
import numpy as np


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

# 解析=====================
print("解析=====================")
proto_info_msg = np.load("filename.npy") #<<<<<<<<<<<<<<<<<<<<<<<读取二进制
first_parsed = one() # 定义输出数据
first_parsed.ParseFromString(proto_info_msg) # 从字符串中(二进制)反序列化解析
# print(first_parsed)
getInfo(first_parsed)  # 输出数据