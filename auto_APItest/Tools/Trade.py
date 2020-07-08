# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/12 10:23 
# @Author : tester_ye 
# @File : Trade.py
import random
import requests
import time
from Datas import Constans
from Utils import Requests

num = round(random.uniform(40000,8),8)
a = random.randint(1,10)
re = Requests.Request()

headers = {
    'X-SITE-ID':'127',
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjEwMDMzNDYsIkxvZ2luVmVyaWZ5IjoxLCJleHAiOjE1ODkzODA3OTh9.9_-E03GXdzXNNkWyWMLXSD-9pYSWftKlpDhAgSxMQ6A'
}
url = 'http://47.97.206.151:8883/api/v1/user/trade/limit'
data = {
    'market':'BTC_CNT',
    'side':2,
    'amount':a,
    'price':num
}
def xiadan(num = 2):
    for i in range(num):
        time.sleep(2)
        response = re.post(url=url,headers=headers,data=data)
        print(response)
        print(Constans.STRESS_LIST)
        print(type(data))

if __name__ == '__main__':
    #设置参数num = 循环次数默认100次
    xiadan()
