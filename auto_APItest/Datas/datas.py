# -*- coding: utf-8 -*- 
# @Create_Time : 2019/5/1 23:24
# @Author : tester_ye 
# @File : datas.py

#获取类数据

import os
from Datas import Read_yaml
from Utils import Log

log = Log.MyLog()
#当前文件父目录
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    #根据key 调用数据读取，返回value
    data = Read_yaml.GetPages().get_data_list()
    param = data[name]
    return param

class Test:
    #读取测试数据后封装
    log.info('解析yaml, Path:' + path_dir + '/Datas/Param/test.yaml')
    params = get_parameter('test')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['headers'])

if __name__ == '__main__':
    t = Test()
    print(t.header)
    print(t.url)
    print(t.data)
