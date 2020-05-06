# -*- coding: utf-8 -*- 
# @Create_Time : 2019/5/6 12:03
# @Author : tester_ye 
# @File : Read_sql.py

from Config import Config
import pymysql
from Utils import Log

class SQL:

    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def read_mysql(self,sql,type = 0,num = 10):
        host = self.config.sql_host
        port = int(self.config.sql_port)
        user = self.config.sql_user
        password = self.config.sql_password
        try:
            #创建mysql连接
            mysql = pymysql.connect(host=host,port=port,user=user,password=password)
            #cursor获取数据库操作游标
            cursor = mysql.cursor()
            #执行sql语句
            cursor.execute(sql)
            '''
            默认返回查询一条数据，type为1时需要传入返回数据条数，type为2时返回所有查询结果
            '''
            if type == 0:
                reslut = cursor.fetchone()
            elif type == 1:
                reslut = cursor.fetchmany(num)
            elif type == 2:
                reslut = cursor.fetchall()
            return reslut
            #关闭数据库连接
            cursor.close()
            mysql.close()

        except Exception as e:
            self.log.error("数据库查询错误，错误信息:{0}".format(e))
            raise

