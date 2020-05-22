# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/19 10:21 
# @Author : tester_ye 
# @File : Draw_red_packet.py

#红包领取

import requests
from Utils import Read_sql
import time


url = "http://47.97.206.151:3030/api-v2/activity/redPacket/DrawPacket"
headers = {"Content-Type":"application/json",
           "X-SITE-ID":'127'}
sql = Read_sql.SQL()
user = []

user =sql.read_mysql(sql ='select phone from exchange.users order by created_at',type=1,num=150)
packet_id = str(sql.read_mysql(sql='select order_no from activity.rp_give_red_packet order by created_at desc')[0])
print(packet_id)
time.sleep(1)

zi = "com"
users = []

for i in user:
    users.append(i[0])

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
    time.sleep(0.2)
    if res["result"]==2:
        print(res)
        # break
    print("用户{0}抢红包:{1}".format(i,res["result"]))
time.sleep(3)
amount = sql.read_mysql(sql='select draw_amount from activity.rp_give_red_packet where order_no = {}'.format(packet_id))
draw_sum = sql.read_mysql(sql='select sum(amount) from activity.rp_draw_red_packet where order_no = {}'.format(packet_id))
sum = sql.read_mysql(sql='select count(*) from activity.rp_draw_red_packet where order_no = {}'.format(packet_id))
sum_rp = sql.read_mysql(sql='select draw_count from activity.rp_give_red_packet where order_no = {}'.format(packet_id))
print("用户红包合计已抢数量{0}，用户领取总金额{1},发红包已抢个数{2},发红包领取总金额{3}".format(sum,draw_sum,sum_rp,amount))
