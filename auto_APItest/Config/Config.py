# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:37
# @Author : tester_ye 
# @File : Config.py

from configparser import ConfigParser
from Utils import Log
import os

class Config:

    #标题
    TITLE = "test_config"
    TITLE_EMAIL = 'email'
    TITILE_DB = 'mysql'

    #登录配置
    TESTER = 'tester'
    HOST = 'host'
    LOGIN_HOST = 'loginHost'
    LOGIN_INFO = 'loginInfo'

    #邮件配置
    SMTP_SERVER = 'smtpserver'
    SENDER = 'sender'
    RECEIVER = 'receiver'
    USERNAME = 'username'
    PASSWORD = 'password'

    #sql配置
    DB_DIR = 'host'
    DB_PORT = 'port'
    DB_USER = 'user'
    DB_PASSWORD = 'password'


    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
    '''
    os.pardir 获取当前目录的父目录字符串名称 '..'
    os.path.dirname(path)返回path的父路劲,__file__当前脚本运行的路劲
    os.path.join(path,name)连接目录与文件名
    os.path.abspath(name)返回脚本的绝对路劲
    '''

    def __init__(self):
        #实例化类ConfigParser、MyLog
        self.config = ConfigParser()
        self.log = Log.MyLog()
        #获取配置文件config.ini绝对路劲
        self.config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'config.ini')
        self.xml_report_path = Config.path_dir + '/Reports/xml'
        self.html_report_path = Config.path_dir + '/Reports/html'

        if not os.path.exists(self.config_path):
            raise FileNotFoundError("配置路径错误")

        self.config.read(self.config_path,encoding='utf-8')

        self.tester = self.get_config(Config.TITLE,Config.TESTER)
        self.host = self.get_config(Config.TITLE,Config.HOST)
        self.login_host = self.get_config(Config.TITLE,Config.LOGIN_HOST)
        self.login_info = self.get_config(Config.TITLE,Config.LOGIN_INFO)
        #邮件配置信息读取
        self.smtpserver = self.get_config(Config.TITLE_EMAIL,Config.SMTP_SERVER)
        self.sender = self.get_config(Config.TITLE_EMAIL,Config.SENDER)
        self.receiver = self.get_config(Config.TITLE_EMAIL,Config.RECEIVER)
        self.username = self.get_config(Config.TITLE_EMAIL,Config.USERNAME)
        self.password = self.get_config(Config.TITLE_EMAIL,Config.PASSWORD)
        #sql配置信息读取
        self.sql_host = self.get_config(Config.TITILE_DB,Config.DB_DIR)
        self.sql_port = self.get_config(Config.TITILE_DB,Config.DB_PORT)
        self.sql_user = self.get_config(Config.TITILE_DB,Config.DB_USER)
        self.sql_password = self.get_config(Config.TITILE_DB,Config.DB_PASSWORD)


    def get_config(self,title,value):
        '''
        配置文件读取
        :param self:
        :param title:
        :param value:
        :return:
        '''
        return self.config.get(title,value)

    def set_config(self,title,value,text):
        '''
        配置文件更新
        :param self:
        :param title:
        :param value:
        :param text:
        :return:
        '''
        self.config.set(title,value,text)
        with open(self.congfig_path,'wb') as f:
            return self.config.write(f)

    def add_config(self,title):
        '''
        配置文件添加
        :param title:
        :return:
        '''
        self.config.add_section(title)
        with open(self.config_path,'wb') as f:
            return self.config.write(f)