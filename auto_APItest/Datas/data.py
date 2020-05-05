# -*- coding: utf-8 -*- 
# @Create_Time : 2019/5/1 23:35
# @Author : tester_ye 
# @File : data.py

import os
from Datas import Read_yaml
from Utils import Log

log = Log.MyLog()
path_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir))

def get_parameter(name):
    data = Read_yaml.G