# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/19 10:21 
# @Author : tester_ye 
# @File : Draw_red_packet.py

#红包领取

import requests
from Utils import Read_sql
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor



url_create = "http://47.97.206.151:3030/api-v2/activity/redPacket/RegisterUser"
url_give = "http://47.97.206.151:3030/api-v2/activity/redPacket/GivePacket"


url = "http://47.97.206.151:3030/api-v2/activity/redPacket/DrawPacket"
headers = {
           "X-SITE-ID":'127'
}
sql = Read_sql.SQL()

user =sql.read_mysql(sql ='select username from exchange.users order by created_at desc ',type=1,num=1200)

# users = []
# with open('./data.txt','r',encoding='utf-8')as f:
#     for line in f:
#         users.append(line.rstrip())
# time.sleep(1)

def give_packet():
    data = 'amount=3&asset_pwd=yeguochun1993&count=10000&theme=http%3A//ztstatictest.oss-cn-hangzhou.aliyuncs.com/chengxin_rz/15753558135de605a55bf104.50999843.jpg&asset=CNT&blessing=%u4F60%u5C3D%u7BA1%u9886%uFF0C%u9886%u5230%u4E86%u7B97%u6211%u8F93%u3002%u54C8%u54C8%u54C8%u54C8'
    header = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjEwMDMyNzcsIkxvZ2luVmVyaWZ5IjoxLCJleHAiOjE1OTA1MjM5Mjl9.fuxcPKnDwUSoYYUiWqODw5MT_gEIXxFKLJgGQ8XVKFs',
        'lang': 'zh-hans',
        'X-SITE-ID': '127',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    requests.post(url=url_give,headers=header,data=data)

def rigister(data_path):
    users = []
    with open(data_path, 'r', encoding='utf-8')as f:
        for line in f:
            users.append(line.rstrip())
    time.sleep(1)
    for i in users:
        body = {
            "packet_id": packet_id,
            "username": i,
            "code": 567765
        }
        response = requests.post(url=url_create,data=body,headers=headers)
        res = response.json()
        # time.sleep(0.1)
        print("新用户{0}抢红包:{1}".format(i, res))

def draw(data_path):
    zi = "com"
    # users = []
    #
    # for i in user:
    #     users.append(i[0])
    users = []
    with open(data_path, 'r', encoding='utf-8')as f:
        for line in f:
            users.append(line.rstrip())
    time.sleep(1)

    for i in users:
        if i == None:
            type = 1
        else:
            if (zi in i) == True:
                type = 2
            else:
                type = 1
        if i != '18781082906':
            body = {"packet_id": packet_id,
                    "in_type": type,
                    "email_phone": i}
            response = requests.post(url=url,headers=headers,json=body)
            res = response.json()
            # time.sleep(0.1)
            # if res["result"]==2:
            #     print(res)
                # break
            print("用户{0}抢红包:{1}".format(i,res))
if __name__ == '__main__':
    # t1 = Thread(target=draw,args=('./data.txt',))
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    for i in range(0,1):
        # give_packet()
        # time.sleep(3)
        packet_id = str(
            sql.read_mysql(sql='select order_no from activity.rp_give_red_packet order by created_at desc')[0])
        print(packet_id)
        time.sleep(1)
        p = ThreadPoolExecutor(5)
        p.submit(draw,'./data_1.txt')
        p.shutdown(wait=True)
        time.sleep(3)
        amount = sql.read_mysql(sql='select draw_amount from activity.rp_give_red_packet where order_no = {}'.format(packet_id))
        draw_sum = sql.read_mysql(sql='select sum(amount) from activity.rp_draw_red_packet where order_no = {}'.format(packet_id))
        sum = sql.read_mysql(sql='select count(*) from activity.rp_draw_red_packet where order_no = {}'.format(packet_id))
        sum_rp = sql.read_mysql(sql='select draw_count from activity.rp_give_red_packet where order_no = {}'.format(packet_id))
        print("用户红包合计已抢数量{0}，用户领取总金额{1},发红包已抢个数{2},发红包领取总金额{3}".format(sum,draw_sum,sum_rp,amount))
