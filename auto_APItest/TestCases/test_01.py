# -*- coding: utf-8 -*- 
# @Create_Time : 2019/5/1 23:28
# @Author : tester_ye 
# @File : test_01.py

import allure

from Datas.params import Test
from Config.Config import Config
from Utils import Requests
from Datas import Constans
from Utils import Assert


class TestBasic:

    # @allure.feature # 用于定义被测试的功能，被测产品的需求点
    # @allure.story # 用于定义被测功能的用户场景，即子功能点
    # @allure.severity #用于定义用例优先级
    # @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
    # @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址

    @allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Test')
    def test_001(self, action):

        #实例化配置文件读取类、断言类、测试数据类
        config = Config()
        data = Test()
        _assert = Assert.Assert()
        request = Requests.Request(action)
        #读取host,读取url,data,headers
        host = config.host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = host + urls[0]
        response = request.get(api_url, params[0], headers[0])

        assert _assert.assert_status(response['response_code'], 200)
        assert _assert.assert_in_body(response['response_body'], 'hhhh')
        assert _assert.assert_time(response['response_time'], 100)
        Constans.RESULT_LIST.append('True')
