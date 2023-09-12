'''
Description: 
Author: HCQ
Company(School): UCAS
Email: 1756260160@qq.com
Date: 2023-09-12 10:49:26
LastEditTime: 2023-09-12 11:09:37
FilePath: /python-libraries/08protobuf/test_proto.py
'''
#coding=utf-8
# file: test_proto.py

# import testProto.person_pb2
import testProto.person_pb2

def setInfo(a_info):
    # 
    a_info.id = 1
    # 
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

# 传入数据
first_info = testProto.person_pb2.one()
one_info = setInfo(first_info)
print(one_info)
proto_info = one_info.SerializeToString() # 序列成字符串
print(proto_info)

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

first_parsed = testProto.person_pb2.one()
first_parsed.ParseFromString(proto_info) # 从字符串中解析
# print(first_parsed)
getInfo(first_parsed)