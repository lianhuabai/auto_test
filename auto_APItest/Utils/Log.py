# -*- coding: utf-8 -*- 
# @Create_Time : 2020/4/11 18:38 
# @Author : tester_ye 
# @File : Log.py

import logging
import os
import time

LEVELS = {
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'

def create_file(file):
    path = file[0:file.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(file):
        fd = open(file,mode='w',encoding='utf-8')
        fd.close()
    else:
        pass

def set_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)

def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)

def get_current_time():
    return time.strftime(MyLog.date,time.localtime(time.time()))




class MyLog:
    path = os.path.dirname(os.path.dirname(os.path(__file__)))
    log_file = path+'/Logs/log.log'
    err_file = path+'/Logs/err.log'
    logger.setLevel(LEVELS.get(level,logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H-%M-%S'

    handler = logging.FileHandler(log_file,encoding='utf-8')
    err_handler = logging.FileHandler(err_file,encoding='utf-8')

    @staticmethod
    def debug(log_msg):
        set_handler('debug')
        logger.debug("[DEBUG" + get_current_time() + "]" + log_msg)
        remove_handler('debug')

    @staticmethod
    def debug(log_msg):
        set_handler('warning')
        logger.debug("[WARNING" + get_current_time() + "]" + log_msg)
        remove_handler('WARNING')

    @staticmethod
    def debug(log_msg):
        set_handler('error')
        logger.debug("[ERROR" + get_current_time() + "]" + log_msg)
        remove_handler('error')

    @staticmethod
    def debug(log_msg):
        set_handler('info')
        logger.debug("[INFOR" + get_current_time() + "]" + log_msg)
        remove_handler('info')

    @staticmethod
    def debug(log_msg):
        set_handler('critical')
        logger.debug("[CRITICAL" + get_current_time() + "]" + log_msg)
        remove_handler('critical')