# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:09
# @Author : tester_ye 
# @File : run.py

import pytest
from Utils import Log
from Utils import Email
from Config import Config

# if __name__ == '__main__':
#     cofig = Config.Config()
#     log = Log.MyLog()
#
#     pytest.main(['-s','-v','--alluredir','./Reports/xml'])
#
#     #生成html测试报告
#     #allure generaten ./Reports -o Reports/html --clean

a = {'SIPC_CNT': '4.08', 'SIPC_USDT': '28.49'}
print(type(a))
print(max(a.keys(),key=(lambda k: a[k])))



