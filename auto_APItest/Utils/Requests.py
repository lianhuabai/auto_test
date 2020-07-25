# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:17
# @Author : tester_ye 
# @File : Requests.py

import requests
from Utils import Log
from Datas import Constans
from Utils import Token


class Request:
    def __init__(self):
        '''
        初始化日志对象，获取登录token
        '''
        token = Token.Token().get_token()
        self.log = Log.MyLog()

        self.headers = {
            "X-SITE-ID":"127",
            "Authonrization":token
        }

    def get(self,url,data=None):
        '''
        get请求封装
        :data url:接口地址
        :data headers:请求头
        :data data:请求参数
        :return:
        '''
        try:
            response = requests.get(url=url,headers=self.headers,params=data)

        except requests.RequestException as e:
            self.log.error("请求异常：" + str(e)+"请求失败url"+ url)

        #获取响应时间
        response_time = response.elapsed.total_seconds()
        response_code = response.status_code
        response_body = response.text 
        response_data = dict()
        response_data['response_code'] = response_code
        response_data['response_time'] = response_time
        response_data['response_body'] = response_body

        Constans.STRESS_LIST.append(response_time)
        return response_data

    def post(self,url,data=None):
        '''
        post请求封装
        :data url:接口地址
        :data headers:请求头
        :data data:请求数据
        :return:
        '''
        try:
            response = requests.post(url=url,headers=self.headers,data=data)
            print(self.headers)

        except requests.RequestException as e:
            self.log.error("请求失败:"+ str(e)+"请求失败url:"+ url)

        response_time = response.elapsed.total_seconds()
        response_code = response.status_code
        response_body = response.text
        response_data = dict()
        response_data['response_code'] = response_code
        response_data['response_time'] = response_time
        response_data['response_body'] = response_body

        Constans.STRESS_LIST.append(response_time)
        return response_data

if __name__ == '__main__':
    r = Request()
    re = r.get(url='http://www.baidu.com')
    print(re['response_time'])
