# -*- coding: utf-8 -*- 
# @Create_Time : 2020/4/11 18:17 
# @Author : tester_ye 
# @File : Requests.py

from Utils import Token
import requests
from Utils import Log
from Utils import Constans

class Request:
    def __init__(self):
        '''
        初始化日志对象，获取登录token
        '''
        self.token = Token.Token().get_token()
        self.log = Log.MyLog()

    def get(self,url,headers,data):
        '''
        get请求封装
        :param url:
        :param headers:
        :param data:
        :return:
        '''
        try:
            response = requests.get(url=url,headers=headers,params=data)

        except requests.RequestException as e:
            self.log.info("请求异常：" + str(e)+"请求失败url"+ url)
        #获取响应时间
        response_time = response.elapsed.total_seconds()
        Constans.STRESS_LIST.append(response_time)
        return response.json()

    def post(self,url,headers,data):
        '''
        post请求封装
        :param url:
        :param headers:
        :param data:
        :return:
        '''
        try:
            response = requests.post(url=url,headers=headers,data=data)

        except requests.RequestException as e:
            self.log.info("请求失败:"+ str(e)+"请求失败url"+ url)

        response_time = response.elapsed.total_seconds()
        Constans.STRESS_LIST.append(response_time)
        return response.json()

