# -*- coding: utf-8 -*- 
# @Create_Time : 2019/5/6 12:03
# @Author : tester_ye 
# @File : Read_sql.py

from Config import Config
import pymysql
from Utils import Log

class SQL:

    def __init__(self):
        config = Config.Config()
        self.log = Log.MyLog()

        host = config.sql_host
        port = int(config.sql_port)
        user = config.sql_user
        password = config.sql_password

        # 创建mysql连接
        self.db = pymysql.connect(host=host, port=port, user=user, password=password)
        # cursor获取数据库操作游标
        self.cursor = self.db.cursor()

    def read_mysql(self,sql,type = 0,num = 10):
        '''
        :param sql: 查询sql语句
        :param type: 查询类型,0为默认返回一条，1返回指定条数num,2返回所有数据
        :param num: 查询返回条数
        :return:
        '''

        try:

            #执行sql语句
            self.cursor.execute(sql)
            '''
            默认返回查询一条数据，type为1时需要传入返回数据条数，type为2时返回所有查询结果
            '''
            if type == 0:
                reslut = self.cursor.fetchone()
            elif type == 1:
                reslut = self.cursor.fetchmany(num)
            elif type == 2:
                reslut = self.cursor.fetchall()

            return reslut

        except Exception as e:
            self.log.error("数据库查询错误，错误信息:{0}".format(e))
            raise
        # 关闭数据库连接
        self.cursor.close()
        self.db.close()

    def update_sql(self,sql):
        '''
        数据库更新，删除，插入
        :param sql: sql语句
        :return:
        '''
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.log.error("sql执行出错，数据回滚。错误信息:{}".format(e))
            self.db.rollback()

        # 关闭数据库连接
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    sql = 'select `activity_name` from activity.activities where `type` = 7'
    sql1 = 'delete from activity.lae_asset_exchange_log where `uid` = 1003346'
    sq = SQL()
    # print(sq.read_mysql(sql = sql,type=2))
    sq.update_sql(sql=sql1)