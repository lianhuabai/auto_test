# -*- coding: utf-8 -*- 
# @Create_Time : 2020/6/4 16:22 
# @Author : tester_ye 
# @File : MD5.py

import hashlib

class MD_5:

    def __init__(self):
        pass

    def get_md5(self,data):
        '''
        :param data:md5加密数据
        :return:
        '''
        hash_object = hashlib.md5('tester_ye'.encode('utf-8'))
        hash_object.update(data.encode('utf-8'))
        result_md = hash_object.hexdigest()

        return result_md
