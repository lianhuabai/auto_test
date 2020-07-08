# -*- coding: utf-8 -*- 
# @Create_Time : 2020/6/6 16:39 
# @Author : tester_ye 
# @File : Otc_check.py

from concurrent.futures import ThreadPoolExecutor
import requests

url = 'http://47.97.206.151:8887/otc-web/api/v1/user/check'
headers = {
    'X-SITE-ID':'127',
    'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySWQiOjE3MTAwMDUsIkxvZ2luVmVyaWZ5IjoxLCJleHAiOjE1OTE0NzcyMzB9.8E3t3yUehak-jrcamCMN6hvp57x8MMo7E2ugfTIgXek'
}

def otc_check():
    for i in range(400):
        r = requests.get(url=url,headers=headers)
        print(r.json())

if __name__ == '__main__':
    t = ThreadPoolExecutor(6)
    t.submit(otc_check,)
    t.submit(otc_check,)
    t.submit(otc_check,)
    t.submit(otc_check,)
    t.submit(otc_check, )
    t.submit(otc_check, )
