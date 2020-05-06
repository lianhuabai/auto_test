# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/27 17:36
# @Author : tester_ye 
# @File : Assert.py
from Utils import Log
from Datas import Constans
import json

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
        try:
            assert code == assert_code
            return True
        except:
            self.log.error("请求状态码对比失败,请求状态码为:{0},断言状态码为:{1}".format(code,assert_code))
            Constans.RESULT_LIST.append('fail')
            raise

    def assert_body(self,body,assert_body):
        '''
        请求响应body断言
        :param body:
        :param assert_body:
        :return:
        '''
        try:
            assert body == assert_body
            return True
        except:
            self.log.error("响应body对比失败，响应body为:{0},断言body为:{1}".format(body,assert_body))
            Constans.RESULT_LIST.append('fail')
            raise

    def assert_in_body(self,body,assert_text):
        '''
        响应信息断言
        :param body:
        :param assert_text:
        :return:
        '''
        try:
            #字段转换为字符串，ensure_ascii参数为输出是否为ASCII编码(序列化时中文默认使用ASCII编码)
            text = json.dumps(body,ensure_ascii=False)
            assert assert_text in text
            return True
        except:
            self.log.error("断言字符串不在响应体中，断言字符串为:{0},响应信息为:{1}".format(assert_text,text))
            Constans.RESULT_LIST.append('fail')
            raise

    def assert_time(self,time,assert_time):
        '''
        响应时间断言
        :param time:
        :param assert_time:
        :return:
        '''
        try:
            assert time < assert_time
            return True
        except:
            self.log.error("响应时间超时，断言时间:{0},响应时间:{1}".format(assert_time,time))
            Constans.RESULT_LIST.append('fail')
            raise