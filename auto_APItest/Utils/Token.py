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
        #读取数据类型为str，json.loads()转化为json字典
        headers = json.loads(self.config.login_headers)
        url = self.config.login_host
        body = json.loads(self.config.login_info)
        response = requests.post(url=url,data=body,headers=headers)
        res_json = response.json()

        print(response.text)
        if response.status_code == 200:
            token = res_json["result"]["token"]
            self.log.debug('登录成功token为:{0}'.format(token))
            self.config.set_config(self.config.TITLE,key='Authorizathion',value='Bearer '+token)
            return 'Bearer '+token

        else:
            self.log.error('登录失败错误信息：'+ response)

if __name__ == '__main__':
    t = Token()
    t.get_token()