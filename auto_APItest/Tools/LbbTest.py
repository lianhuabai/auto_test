# -*- coding: utf-8 -*- 
# @Create_Time : 2020/6/3 18:12 
# @Author : tester_ye 
# @File : LbbTest.py

from Utils import Read_sql

rd = Read_sql.SQL()

inve = 'select lb_in.uid,sum(lb_in.amount) from activity.lbb_invest_log lb_in where lb_in.deposit_time < "2020-06-03" group by lb_in.uid'
lock = 'select lb_un.uid,sum(lb_un.amount) from activity.lbb_unlock_log lb_un where lb_un.unlock_time < "2020-06-03" group by lb_un.uid'
inve_two = 'select lb_in.uid,lb_in.amount,lb_in.deposit_time from activity.lbb_invest_log lb_in where lb_in.deposit_time > "2020-06-03" and lb_in.deposit_time < "2020-06-04"'
lock_two = 'select lb_un.uid,lb_un.amount,lb_un.unlock_time from activity.lbb_unlock_log lb_un where lb_un.unlock_time > "2020-06-03" and lb_un.unlock_time < "2020-06-04"'
inves = {}
locks = {}
r = rd.read_mysql(sql=inve,type=2)
print(len(r))
for i in r:
    inves[i[0]] = i[1]
print(len(inves))
print("inve{}".format(inves))
r = rd.read_mysql(sql=lock,type=2)
for i in r:
    locks[i[0]] = i[1]
print("lock{}".format(locks))
num = 0
for key,value in inves.items():
    for key1,value1 in locks.items():
        if key == key1:
            inves[key] = value-value1
#具备条件用户
print(inves)
print(len(inves))

with open('./data_1.txt','w') as f:
    for key,value in inves.items():
        f.write("id:{0}      amount:{1} \n".format(key,value))

print(len(inves))
