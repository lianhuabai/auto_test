# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/27 9:55
# @Author : tester_ye 
# @File : Mock.py

from flask import Flask,jsonify,request

mock_server = Flask(__name__)
mock_server.config['JSON_AS_ASCII'] = False

valuation = {
    "message":"OK",
    "code":0,
    "result":{
        "to_asset":"ZTB",
        "amount":"68.26819141",
        "price":"1.36536382哈哈哈",
        "limit_status":0}
}
@mock_server.route("/valuation",methods=['GET'])
def get_valuation():
    return jsonify(valuation)

if __name__ == '__main__':
    mock_server.run(host='127.0.0.1',port=7777,debug=True)

