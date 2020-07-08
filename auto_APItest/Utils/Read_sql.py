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

        self.host = config.sql_host
        self.port = int(config.sql_port)
        self.user = config.sql_user
        self.password = config.sql_password
    def connect(self):
        # 创建mysql连接
        self.db = pymysql.connect(host=self.host, port=self.port, user=self.user, password=self.password)
        # cursor获取数据库操作游标
        self.cursor = self.db.cursor()
        print("创建连接")

    def close(self):
        self.cursor.close()
        self.db.close()
        print("连接已释放")

    def read_mysql(self,sql,type = 0,num = 10):
        '''
        :param sql: 查询sql语句
        :param type: 查询类型,0为默认返回一条，1返回指定条数num,2返回所有数据
        :param num: 查询返回条数
        :return:
        '''

        try:

            self.connect()
            #执行sql语句
            self.cursor.execute(sql)
            print('查询开始')
            '''
            默认返回查询一条数据，type为1时需要传入返回数据条数，type为2时返回所有查询结果
            '''
            if type == 0:
                reslut = self.cursor.fetchone()
            elif type == 1:
                reslut = self.cursor.fetchmany(num)
            elif type == 2:
                reslut = self.cursor.fetchall()

            # 关闭数据库连接
            self.close()

            return reslut

        except Exception as e:
            self.log.error("数据库查询错误，错误信息:{0}".format(e))
            raise


    def update_sql(self,sql):
        '''
        数据库更新，删除，插入
        :param sql: sql语句
        :return:
        '''
        try:
            self.connect()
            self.cursor.execute(sql)
            self.db.commit()

            # 关闭数据库连接
            self.close()
        except Exception as e:
            self.log.error("sql执行出错，数据回滚。错误信息:{}".format(e))
            self.db.rollback()


# if __name__ == '__main__':
#     sql = 'select username from exchange.users order by created_at'
#     # sql1 = 'delete from activity.lae_asset_exchange_log where `uid` = 1003346'
#     sq = SQL()
#     user = sq.read_mysql(sql=sql,type=1,num=1100)
#     with open('./data_1.txt','w',encoding='utf-8')as f:
#         for i in user:
#             if i[0] is not None:
#                 f.write(i[0]+'\n')
    # sq.read_mysql(sql=sql)
    # print(sq.read_mysql(sql=sql,type=2))