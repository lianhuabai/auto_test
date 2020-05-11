# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:17
# @Author : tester_ye 
# @File : Requests.py

import requests
from Utils import Log
from Datas import Constans


class Request:
    def __init__(self):
        '''
        初始化日志对象，获取登录token
        '''
        # self.token = Token.Token().get_token()
        self.log = Log.MyLog()

    def get(self,url,headers,data):
        '''
        get请求封装
        :data url:接口地址
        :data headers:请求头
        :data data:请求参数
        :return:
        '''
        try:
            response = requests.get(url=url,headers=headers,params=data)

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

    def post(self,url,headers,data):
        '''
        post请求封装
        :data url:接口地址
        :data headers:请求头
        :data data:请求数据
        :return:
        '''
        try:
            response = requests.post(url=url,headers=headers,data=data)

        except requests.RequestException as e:
            self.log.info("请求失败:"+ str(e)+"请求失败url:"+ url)

        response_time = response.elapsed.total_seconds()
        response_code = response.status_code
        response_body = response.text
        response_data = dict()
        response_data['response_code'] = response_code
        response_data['response_time'] = response_time
        response_data['response_body'] = response_body

        Constans.STRESS_LIST.append(response_time)
        return response_data

# if __name__ == '__main__':
#     r = Request()
#     r.get(url='http://www.baidu.com',headers=None,data=None)