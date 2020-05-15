# -*- coding: utf-8 -*- 
# @Create_Time : 2020/5/8 12:07 
# @Author : tester_ye 
# @File : Thread_te.py
import threading
import time

class myThread(threading.Thread,):

    def __init__(self,threadID,threadName,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.counter = counter

    def run(self,data):
        print("thread {} start----".format(self.threadName))
        data
        print()