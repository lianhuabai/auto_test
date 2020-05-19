# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/19 10:26 
# @Author : tester_ye 
# @File : Vote.py
#投票上币

from Utils import Read_sql

user_id = 1003277 #用户id
activity_id = 1400 #活动id
currency_id = 78 #项目方id

sql = Read_sql.SQL()


x = sql.read_mysql(sql='select total_ticket from activity.vc_option_log where uid = {0} and activity_id = {1} and currency_id = {2} order by created_at desc limit 1 '.format(user_id,activity_id,currency_id)) #用户投票总数
y = sql.read_mysql(sql='select ticket from activity.vc_currency where activity_id = {0} and id = {1}'.format(activity_id,currency_id)) #项目投票总数
z = float(sql.read_mysql(sql='select reward_amount from activity.vc_currency where activity_id = {0} and id = {1}'.format(activity_id,currency_id))) #项目奖励总数
a = float(sql.read_mysql(sql='select enjoy_percent from activity.vc_vote_currency where id = {0}'.format(activity_id))) #奖励折扣率
b = float(sql.read_mysql(sql='select reward_cny_amount from activity.vc_currency where activity_id = {0} and id = {1}'.format(activity_id,currency_id))) #奖励币种单价
d = float(sql.read_mysql(sql='select amount from activity.vc_vote_currency where id = {0}'.format(activity_id))) #每票所需币种数量
c = float(sql.read_mysql(sql='select cny_amount from activity.vc_vote_currency where id = {0}'.format(activity_id))) #投票币种单价
# test = read_sql.read_mysql(sql='select cancel from activity.vc_vote_currency where id = 1384')

'''
用户可兑换奖励数量
'''
def reward_function(x,y,z,a,b,c):
    reward = (((x/y)*z*(b/c))/a)/b
    return reward

'''
剩余投票币种数量直接解冻
'''
def return_function(x,y,z,a,b,c,d):
    s = reward_function(x,y,z,a,b,c)
    return_f = ((x*d*c)-(s*b))/c
    return return_f

if __name__ == '__main__':
    print(x,'用户总票数')
    print(y,'项目总票数')
    print(z,'项目奖励总数')
    print(a,'奖励折扣率')
    print(b,'奖励币种价格')
    print(c,'每票需要币种单价')
    print(d,'每票所需币种数量 \n')
    print(reward_function(x,y,z,a,b,c),'用户可兑换奖励数量')
    print(return_function(x,y,z,a,b,c,d),'剩余直接解冻数量')
