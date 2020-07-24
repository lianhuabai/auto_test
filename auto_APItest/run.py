# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:09
# @Author : tester_ye 
# @File : run.py

import pytest
from Utils import Log
from Utils import Email
from Config import Config
import subprocess
import os
import json
from Datas import Constans

if __name__ == '__main__':
    #初始化配置文件读取，日志打印类，邮件发送
    cofig = Config.Config()
    log = Log.MyLog()
    email = Email.SendMail()
    log.info('用例执行开始--------------------------')
    #读取报告路劲
    xml_report_path = cofig.xml_report_path
    html_report_path = cofig.html_report_path
    print(xml_report_path)
    del_xml = 'del /q {0}'.format(xml_report_path)
    print(html_report_path)
    #linux
    # del_xml = 'rm -rf {0}'.format(xml_report_path)
    # cmd命令，allure生成html测试报告
    cmd = 'allure generate {0} -o {1} --clean'.format(xml_report_path, html_report_path)
    #开启allure服务命令
    server = 'allure open -h 127.0.0.1 -p 7777 ./Reports/'
    json_path = str(os.path.abspath(os.path.dirname(__file__)))+'/Reports/xml/'

    try:
        out = subprocess.Popen(args=del_xml,shell=True,encoding='utf-8',stdout=subprocess.PIPE).communicate()
        log.debug("删除旧报告数据执行结果:{}".format(out))

    except Exception as e:
        log.error("删除数据失败:{}".format(e))

    pytest.main(['-s','-v','--alluredir',xml_report_path])
    try:
        out = subprocess.Popen(args=cmd,encoding='utf-8',shell=True,stdout=subprocess.PIPE).communicate()
        log.debug("生成html报告命令执行结果{}".format(out))

    except Exception as e:
        log.error("html报告命令执行失败,错误信息:{}".format(e))
        raise

    result_path = []
    for root,dirs,files in os.walk(json_path):
        for file in files:
            if file[file.rfind('.') + 1:len(file)] == 'json':
                result_path.append(file)
    for i in result_path:
        with open(json_path+i,'r',encoding='utf-8') as f:
            reslut = json.load(f)
            Constans.RESULT_LIST[reslut['name']] = reslut['status']

    try:
        #发送邮件
        email.send_mail()
    except Exception as e:
        log.error("邮件发送失败，错误信息:{}".format(e))
        raise

    # try:
    #     subprocess.Popen(args=server,shell=True,encoding='utf-8').communicate()
    # except Exception as e:
    #     log.error("启动服务失败:{}".format(e))

