# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/6 13:07 
# @Author : tester_ye 
# @File : ces.py

#代码调试文件

from Utils import Read_sql

sql = 'select `activity_name` from activity.activities where `type` = 22'

sq = Read_sql.SQL()

print(sq.read_mysql(sql = sql))
print(type(sq.read_mysql(sql = sql)))