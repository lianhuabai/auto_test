# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/14 11:36 
# @Author : tester_ye 
# @File : st.py

class ST:
    __private = 30
    public = 40
    def __init__(self):
        pass
    def num(self):
        return ST.__private
    def __del__(self):
        classname = self.__class__.__name__
        print(classname)

if __name__ == '__main__':
    s = ST()
    print(s.public)
    print(s.num())