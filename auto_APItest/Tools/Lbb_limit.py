# -*- coding: utf-8 -*- 
# @Create_Time : 2020/6/12 14:01 
# @Author : tester_ye 
# @File : Lbb_limit.py

from concurrent.futures import ThreadPoolExecutor
import requests
from Config import Config

class Lbb:


    config = Config.Config()
    @classmethod
    def test_jion(self):
        headers = {
            'Authorization':self.config.token,
            'X-SITE-ID':'127'
        }
        url = self.config.activity_front_host + '/api-v2/activity/lbb/JoinActivity'
        data = {
            'activity_id':'2056',
            'amount':'14',
            'goods_id':'13'
        }
        response = requests.post(url=url,headers=headers,data=data)
        print(response.text)

if __name__ == '__main__':
    lb = Lbb.test_jion
    excuter = ThreadPoolExecutor(5)
    for i in range(100):
        excuter.submit(lb, )
        excuter.submit(lb, )
        excuter.submit(lb, )
        excuter.submit(lb, )
        excuter.submit(lb, )

