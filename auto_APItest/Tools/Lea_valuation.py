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
from Datas import Constans

request = Requests.Request()
headers = {
    "X-SITE-ID":"127"
}
r = request.get(url='http://47.97.206.151:8883/api/v1/exchangeTickers',headers=headers,data=None)
r_json = json.loads(r['response_body'])
tickers = r_json['result']['ticker']
print(tickers)
print(Constans.STRESS_LIST)

#获取指定交易对最新价格
def convert(symbol):
    '''
    :param symbol: 交易对
    :return:
    '''
    symbols = {}
    for i in tickers:
        if i['symbol'] == symbol:
            symbols[i['symbol']] = i['last']
    return(decimal.Decimal(symbols[symbol]))

#获取兑换币种所有的交易对以及价格
def exchange(fromasset):
    '''
    :param fromasset: 兑换币种
    :return:币种所有交易对以及价格dict
    '''
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

    @classmethod
    def asset_exchange(self,fromasset,lea_base):
        '''
        兑换币种所有交易对最高价
        :param fromasset: 兑换币种
        :param lea_base: 估值/兑换币种基准币种
        :return:
        '''

        price = {}
        symbol = exchange(fromasset)
        # print(symbol)
        dec = decimal.Decimal
        for sym,pri in symbol.items():
            base = sym[sym.rfind('_') + 1:len(sym)]
            #交易对属于各个交易区的价格折算存入price
            if lea_base == 'CNT':
                if base == 'CNT':
                    price[sym] = dec(pri)
                elif base == 'BTC':
                    price[sym] = convert('BTC_CNT')*dec(pri)
                elif base == 'ETH':
                    price[sym] = convert('ETH_CNT')*dec(pri)
                elif base == 'USDT':
                    price[sym] = convert('USDT_CNT')*dec(pri)
            elif lea_base == 'USDT':
                if base == 'CNT':
                    price[sym] = dec(pri)/convert('USDT_CNT')
                elif base == 'BTC':
                    price[sym] = convert('BTC_USDT')*dec(pri)
                elif base == 'ETH':
                    price[sym] = convert('ETH_USDT')*dec(pri)
                elif base == 'USDT':
                    price[sym] = dec(pri)
            elif lea_base == 'ETH':
                if base == 'ETH':
                    price[sym] = dec(pri)
                elif base == 'BTC':
                    price[sym] = convert('BTC_ETH')*dec(pri)
                elif base == 'USDT':
                    price[sym] = dec(pri)/convert('ETH_USDT')
                elif base == 'CNT':
                    price[sym] = dec(pri)/convert('ETH_CNT')
            elif lea_base == 'BTC':
                if base == 'BTC':
                    price[sym] = dec(pri)
                elif base == 'CNT':
                    price[sym] = dec(pri)/convert('BTC_CNT')
                elif base == 'USDT':
                    price[sym] = dec(pri)/convert('BTC_USDT')
                elif base == 'ETH':
                    price[sym] = dec(pri)/convert('BTC_ETH')

        print("兑换币种{0}的价格为:{1}".format(fromasset,symbol))
        print("兑换币种在各交易区折算{0}最高价为:{1}".format(lea_base,price[max(price, key=price.get)]))
        #返回兑换币种各个交易区最大CNT价格
        return (price[max(price, key=price.get)])


    @classmethod
    def exchange_price(self,from_asset,toasset,num,deel_fee,lea_asset,lea_base):
        '''
        :param from_asset: 待兑换币种
        :param toasset: 兑换交易对
        :param num: 数量
        :param deel_fee: 手续费
        :param lea_asset: 估值交易对
        :return:
        '''
        try:
            #待兑换币种最高价格
            from_asset_price = decimal.Decimal(self.asset_exchange(from_asset,lea_base))
            # 兑换币种交易对价格
            to_asset_price = convert(toasset)
            num_dec = decimal.Decimal(num)
            deel_fe = decimal.Decimal(deel_fee)
        except Exception as e:
            print(e)
            raise

        # 估值交易对估值
        print("估值交易对为:{0}价格为:{1}".format(lea_asset,convert(lea_asset)))
        try:
            #估值
            valuation_price =num_dec*from_asset_price/convert(lea_asset)
            # 兑换交易对数量
            exchange_price = num_dec*from_asset_price/to_asset_price
            #折扣扣除
            deel = exchange_price*deel_fe
        except Exception as e:
            print(e)
            raise
        to_symbol = toasset[0:toasset.rfind('_')]
        print("兑换币种{0}的价格为:{1}".format(toasset,convert(toasset)))
        print("{0}的BTC估值为:{1}".format(from_asset,round(valuation_price,8)))
        print("{0}可兑换{1}个{2}".format(from_asset,round(exchange_price,8),to_symbol))
        print("预计扣除手续费{0}{1}".format(round(deel,8),to_symbol))

if __name__ == '__main__':
    Lae.exchange_price('ETH','ZT_USDT',0.3333,0.5555,'BTC_USDT','USDT')