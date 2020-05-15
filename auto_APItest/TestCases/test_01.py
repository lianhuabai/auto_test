# -*- coding: utf-8 -*- 
# @Create_Time : 2019/5/1 23:28
# @Author : tester_ye 
# @File : test_01.py

import allure

from Datas.datas import Test
from Config.Config import Config
from Utils import Requests
from Datas import Constans
from Utils import Assert
from Utils import Token

@allure.feature('小额资产兑换')
class TestExchange:

    # @allure.feature # 用于定义被测试的功能，被测产品的需求点
    # @allure.story # 用于定义被测功能的用户场景，即子功能点
    # @allure.severity #用于定义用例优先级
    # @allure.issue #用于定义问题表识，关联标识已有的问题，可为一个url链接地址
    # @allure.testcase #用于用例标识，关联标识用例，可为一个url链接地址


    @allure.severity('blocker')
    @allure.story('兑换资产')
    @allure.description('小额资产兑换测试')
    @allure.link('www.baidu.com')
    @allure.issue(('BUG编号:123'))
    @allure.testcase('验证兑换资产是否成功')
    def test_001(self):
        '''
        参数信息
        :return:
        '''

        #实例化配置文件读取类、断言类、测试数据类
        config = Config()
        data = Test()
        _assert = Assert.Assert()
        request = Requests.Request()
        token = Token.Token().get_token()
        #读取host,读取url,data,headers
        host = config.activity_front_host
        urls = data.url
        params = data.data
        headers = data.header
        headers[0]['Authorization'] = token

        allure.attach('用例参数:{0}'.format(params))
        with allure.step("测试步骤调用"):
            allure.attach('失败','期望结果')

        api_url = host + urls[0]
        response = request.post(url=api_url, data=params[0][0], headers=headers[0])

        assert _assert.assert_status(response['response_code'], 200)
        # assert _assert.assert_in_body(response['response_body'], '兑换成功')
        # assert _assert.assert_time(response['response_time'], 100)

    @allure.story('用例2')
    def test_002(self):
        _assert = Assert.Assert()
        assert _assert.assert_body(1,2)
