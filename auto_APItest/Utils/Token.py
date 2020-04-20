# -*- coding: utf-8 -*- 
# @Create_Time : 2020/4/11 18:32 
# @Author : tester_ye 
# @File : Token.py

import requests
from Config import Config
from Utils import Log
import json

class Token:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_token(self):

        headers = {
            "Content-Type":"application/x-www-form-urlencoded",
            "X-SITE-ID":"127"
        }

        url = self.config.login_host
        body = json.loads(self.config.login_info)
        print(type(body))
        response = requests.post(url=url,data=body,headers=headers)
        res_json = response.json()

        print(response.text)
        if response.status_code == 200:
            token = res_json["result"]["token"]
            self.log.debug('登录成功token为:{0}'.format(token))
            return token
        else:
            self.log.error('登录失败错误信息：'+ response)

if __name__ == '__main__':
    t = Token()
    t.get_token()