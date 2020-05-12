# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/12 10:23 
# @Author : tester_ye 
# @File : jiaoyi.py
import random
import requests
import time
from Datas import Constans

num = round(random.uniform(40000,8),8)
a = random.randint(1,10)

headers = {
    'X-SITE-ID':'127',
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjEwMDMyNzcsIkxvZ2luVmVyaWZ5IjoxLCJleHAiOjE1ODkyOTA0MzJ9.MRrEj60cK-qNHkPEk8HHCiXvSYBIIQ4J19AMHmvNfy0'
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
        response = requests.post(url=url,headers=headers,data=data)
        print(response.json())
        print(Constans.STRESS_LIST)

if __name__ == '__main__':
    #设置参数num = 循环次数默认100次
    xiadan()
