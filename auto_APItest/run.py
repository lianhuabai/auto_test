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
    cofig = Config.Config()
    log = Log.MyLog()
    log.info('用例执行开始--------------------------')
    xml_report_path = cofig.xml_report_path
    html_report_path = cofig.html_report_path
    email = Email.SendMail()
    cmd = 'allure generaten {0} -o {1} --clean'.format(xml_report_path,html_report_path)

    pytest.main(['-s','-v','--alluredir',xml_report_path])
    try:
        subprocess.Popen(args=cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,encoding='utf-8')

    except Exception as e:
        log.error("html报告命令执行失败,错误信息:{}".format(e))
        raise
    try:
        email.send_mail()
    except Exception as e:
        log.error("邮件发送失败，错误信息:{}".format(e))
        raise



    #生成html测试报告
    #allure generaten ./Reports -o Reports/html --clean




