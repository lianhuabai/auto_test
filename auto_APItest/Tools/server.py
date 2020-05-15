# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/14 15:01 
# @Author : tester_ye 
# @File : server.py
import os
import json
# import socket
#
# s = socket.socket()
# host = socket.gethostname()
# port = 1231
# s.bind((host,port))
#
# s.listen(5)
# while True:
#     c,adrss = s.accept()
#     data = c.recv(1024)
#     print('连接地址：',adrss)
#     c.send(data)
#     c.close()
e = 'F:\\test\\auto_APItest\\Reports\\xml'

for root,dirs,files in os.walk(e):
    for file in files:
        if file[file.rfind('.')+1:len(file)] == 'json':
            print(file)
# with open(e,'r',encoding='utf-8') as f:
#     j = json.load(f)
#     print(j)