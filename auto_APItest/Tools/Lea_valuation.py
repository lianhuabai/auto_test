# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/6 13:07 
# @Author : tester_ye 
# @File : Lea_valuation.py

'''
交易所币种各交易区价格折合最高价
小额资产兑换，折算
'''

from Utils import Requests
import json
import decimal

# from Utils import Read_sql
#
# sql = 'select `activity_name` from activity.activities where `type` = 22'
#
# sq = Read_sql.SQL()
#
# print(sq.read_mysql(sql = sql))
# print(type(sq.read_mysql(sql = sql)))

request = Requests.Request()
headers = {
    "X-SITE-ID":"127"
}
r = request.get(url='http://47.97.206.151:8883/api/v1/exchangeTickers',headers=headers,data=None)
# r = request.get(url='http://www.baidu.com',headers=None,data=None)
r_json = json.loads(r['response_body'])
tickers = r_json['result']['ticker']
print(tickers)

#获取各交易区基准币种兑换CNT价格
def convert():
    symbols = {}
    for i in tickers:
        symbols_list = ['ETH_CNT', 'BTC_CNT', 'USDT_CNT']
        if i['symbol'] in symbols_list:
            symbols[i['symbol']] = i['last']

    return(symbols)

#获取兑换币种所有的交易对以及价格
def exchange(fromasset):
    len_fromasset = len(fromasset)
    symbol = {}
    for i in tickers:
        tickter = (i['symbol'])
        tickter_asset = tickter[0:len_fromasset]

        if fromasset == tickter_asset:
            symbol[i['symbol']] = i['last']
    return(symbol)

#价格折算
class Lae:
    #币种所有交易对及价格
    # symbol = exchange()

    # 交易区基础交易币兑换CNT价格
    # 交易区基础币种折算CNT价格

    symbols = convert()
    BTC_CNT = decimal.Decimal(symbols['BTC_CNT'])
    ETH_CNT = decimal.Decimal(symbols['ETH_CNT'])
    USDT_CNT = decimal.Decimal(symbols['USDT_CNT'])

    @classmethod
    def asset_exchange(self,fromasset):

        price = {}
        symbol = exchange(fromasset)
        # print(symbol)
        for sym,pri in symbol.items():
            base = sym[sym.rfind('_') + 1:len(sym)]

            if base == 'CNT':
                price[sym] = str(pri)
            elif base == 'BTC':
                price[sym] = str(self.BTC_CNT*decimal.Decimal(pri))
            elif base == 'ETH':
                price[sym] = str(self.ETH_CNT*decimal.Decimal(pri))
            elif base == 'USDT':
                price[sym] = str(self.USDT_CNT*decimal.Decimal(pri))

        print("兑换币种{0}的价格为:{1}".format(sym,pri))
        print("兑换币种在各交易区折算CNT最高价为:{0}".format(price[max(price, key=price.get)]))
        #返回兑换币种各个交易区最大CNT价格
        return (price[max(price, key=price.get)])

    # 兑换目标币种CNT价格
    @classmethod
    def exchange_cnt(self,to_ex_asset):
        toasset = to_ex_asset+"_CNT"
        for i in tickers:
            if i['symbol'] == toasset:
                exchange_cnt_price = i['last']
        #返回兑换币种CNT价格
        return (decimal.Decimal(exchange_cnt_price))


    @classmethod
    def exchange_price(self,from_asset,toasset,num,deel_fee):
        '''
        :data toasset: 兑换币种
        :data valuation: 估值币种
        :return:
        '''
        from_asset_price = decimal.Decimal(self.asset_exchange(from_asset))
        to_asset_price = self.exchange_cnt(toasset)
        num_dec = decimal.Decimal(num)
        deel_fe = decimal.Decimal(deel_fee)

        # 估值交易对估值
        valuation_price = num_dec*from_asset_price/self.BTC_CNT
        # 兑换交易对估值
        exchange_price = num_dec*from_asset_price/to_asset_price
        #折扣扣除
        deel = exchange_price*deel_fe

        print("{0}的BTC估值为:{1}".format(from_asset,round(valuation_price,8)))
        print("{0}可兑换{1}个{2}".format(from_asset,round(exchange_price,8),toasset))
        print("预计扣除手续费{0}{1}".format(round(deel,8),toasset))


if __name__ == '__main__':
    l = Lae()
    l.exchange_price('VOLLAR','ZT',1780.55243487,0.5555)