# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/21 17:23 
# @Author : tester_ye 
# @File : Phone_num.py
import random

class Phoen_num:

    def __init__(self):
        pass
    def create_phone(self):
        second = [3,4,5,7,8][random.randint(0,4)]
        third = {
            3: random.randint(0,9),
            4: [5,7,9][random.randint(0,2)],
            5: [i for i in range(10) if 1 != 4][random.randint(0,8)],
            7: [i for i in range(10) if i not in [4,9]][random.randint(0, 7)],
            8: random.randint(0,9),
        }[second]
        suffix = random.randint(9999999,100000000)
        return int('1{}{}{}'.format(second,third,suffix))

if __name__ == '__main__':
    ph = Phoen_num()
    with open('./data_4.txt', 'w', encoding='utf-8')as f:
        for i in range(0,2000):
            phone = str(ph.create_phone())
            f.write( phone+ '\n')