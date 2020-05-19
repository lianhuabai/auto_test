# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/19 10:21 
# @Author : tester_ye 
# @File : Draw_red_packet.py

#红包领取

import requests
from Utils import Read_sql
import time


url = "http://47.97.206.151:3030/api-v2/activity/redPacket/DrawPacket"
headers = {"Content-Type":"application/json"}
sql = Read_sql.SQL()

user =sql.read_mysql(sql ='select phone from exchange.users order by created_at',type=1,num=50)
packet_id = sql.read_mysql(sql='select order_no from activity.rp_give_red_packet order by created_at desc')
amount = sql.read_mysql(sql='select amount from activity.rp_give_red_packet where order_no = {}'.format(packet_id))
sum_sql = 'select sum(amount) from activity.rp_draw_red_packet where uid != 0 and order_no = {}'.format(packet_id)
sum_rp_sql = 'select draw_amount from activity.rp_give_red_packet where order_no = {}'.format(packet_id)

str(packet_id)
zi = "com"
users = []

for i in user:
    users.append(i[0])
print(users)

for i in users:
    if (zi in i) == True:
        type = 2
    else:
        type = 1

    body = {"packet_id": packet_id,
            "in_type": type,
            "email_phone": i}
    response = requests.post(url=url,headers=headers,json=body)
    res = response.json()
    if res["result"]==2:
        print(res)
        # break
    print("用户{0}抢红包:{1}".format(i,res["result"]))
time.sleep(3)
sum = sql.read_mysql(sql=sum_sql)
sum_rp = sql.read_mysql(sql=sum_rp_sql)
print("用户红包合计已抢数量{0}，红包已抢{1},红包创建总金额{2}".format(sum,sum_rp,amount))
