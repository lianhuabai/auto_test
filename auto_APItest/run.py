# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:09
# @Author : tester_ye 
# @File : run.py

import pytest
from Utils import Log
from Utils import Email
from Config import Config
import subprocess

if __name__ == '__main__':
    #初始化配置文件读取，日志打印类，邮件发送
    cofig = Config.Config()
    log = Log.MyLog()
    email = Email.SendMail()
    log.info('用例执行开始--------------------------')
    #读取报告路劲
    xml_report_path = cofig.xml_report_path
    html_report_path = cofig.html_report_path
    #cmd命令，allure生成html测试报告
    cmd = 'allure generaten {0} -o {1} --clean'.format(xml_report_path,html_report_path)
    #执行用例，设置报告路劲
    pytest.main(['-s','-v','--alluredir',xml_report_path])
    try:
        #执行cmd命令
        subprocess.Popen(args=cmd,encoding='utf-8')

    except Exception as e:
        log.error("html报告命令执行失败,错误信息:{}".format(e))
        raise
    try:
        #发送邮件
        email.send_mail()
    except Exception as e:
        log.error("邮件发送失败，错误信息:{}".format(e))
        raise






