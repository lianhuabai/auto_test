# -*- coding: utf-8 -*- 
# @Create_Time : 2019/5/1 22:50
# @Author : tester_ye 
# @File : Read_yaml.py

import os
import yaml

#读取测试数据


def parse():
    path = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Datas/data'
    data_yaml = {}
    #os.walk方法，主要用来遍历一个目录内各个子目录和子文件
    #返回的是一个三元组(root, dirs, files)
    # root所指的是当前正在遍历的这个文件夹的本身的地址
    # dirs是一个list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    # files同样是list, 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(path):
        for name in files:
            # print(name)
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, encoding='UTF-8') as f:
                #safe_load(),yaml文件转换为python值
                page = yaml.safe_load(f)
                #字典更新
                data_yaml.update(page)
        return data_yaml

class GetPages:
    @staticmethod
    def get_data_list():
        data_list = {}
        #读取原始测试数据
        data_yaml = parse()
        for page, value in data_yaml.items():
            #获取字典中参数
            parameters = value['parameter']
            list = []
            for parameter in parameters:
                # print(parameter)
                list.append(parameter)
            data_list[page] = list
        # print(data_list)
        return data_list

# if __name__ == '__main__':
#     lists = GetPages.get_data_list()
