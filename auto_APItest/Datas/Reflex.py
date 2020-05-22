# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/21 11:28 
# @Author : tester_ye 
# @File : Reflex.py

#反射数据类

class Reflex_api:
    token = None

    # getattr()获取指定字符串名称的对象属性
    # setattr()为对象设置一个对象
    # hasattr()判断对象是否有对应的对象（字符串）
    # delattr() 删除指定属性

setattr(Reflex_api,'token','test_token')
print(getattr(Reflex_api,'token'))