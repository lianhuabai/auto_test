# -*- coding: utf-8 -*- 
# @Create_Time : 2020/4/27 17:36 
# @Author : tester_ye 
# @File : Assert.py
from Utils import Log
from Utils import Constans

class Assert:

    def __init__(self):
        self.log = Log.MyLog()

    def assert_status(self,code,assert_code):
        '''
        请求响应状态码断言
        :param code:
        :param assert_code:
        :return:
        '''
        if code == assert_code:
            return True
        else:
            return False
