# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:09
# @Author : tester_ye 
# @File : run.py

import pytest
from Utils import Log
from Utils import Email
from Config import Config

if __name__ == '__main__':
    cofig = Config.Config()
    log = Log.MyLog()
    log.info('初始化文件，path = ' + cofig.config_path)