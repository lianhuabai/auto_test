# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/11 18:38
# @Author : tester_ye 
# @File : Log.py

import logging
import os
import time

# 获取当前脚本文件父类的绝对路径（项目主目录）
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_file = path + '/Logs/log.log'
err_file = path + '/Logs/err.log'
date = '%Y-%m-%d %H-%M-%S'

LEVELS = {
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.CRITICAL
}
#初始化日志对象logger
logger = logging.getLogger()
level = 'default'

# 实例化日志信息输出到磁盘文件上的流，指定文件路劲和编码
handler = logging.FileHandler(log_file, encoding='utf-8')
err_handler = logging.FileHandler(err_file, encoding='utf-8')

def create_file(file):
    #路劲从右查询第一个/位置切片，获取log所在文件的路劲
    path = file[0:file.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(file):
        fd = open(file,mode='w',encoding='utf-8')
        fd.close()
    else:
        pass
#为logger添加写入对应的handler
def add_handler(levels):
    if levels == 'error':
        logger.addHandler(err_handler)
    logger.addHandler(handler)

#调用log记录日志后移除logger中的handler，防止出现重复日志信息
def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(err_handler)
    logger.removeHandler(handler)
#获取当前时间
def get_current_time():
    return time.strftime(date,time.localtime(time.time()))


class MyLog:

    #设置日志等级，设置默认日志等级notset所有等级
    logger.setLevel(LEVELS.get('debug',logging.NOTSET))
    #创建日志文件
    create_file(log_file)
    create_file(err_file)

    @staticmethod
    def debug(log_msg):
        '''
        添加写入日志的流
        添加等级为debug的日志
        移除日志流
        :param log_msg:
        :return:
        '''
        add_handler('debug')
        logger.debug("[DEBUG" + get_current_time() + "]" + log_msg)
        remove_handler('debug')

    @staticmethod
    def warning(log_msg):
        add_handler('warning')
        logger.warning("[WARNING" + get_current_time() + "]" + log_msg)
        remove_handler('WARNING')

    @staticmethod
    def error(log_msg):
        add_handler('error')
        logger.error("[ERROR" + get_current_time() + "]" + log_msg)
        remove_handler('error')

    @staticmethod
    def info(log_msg):
        add_handler('info')
        logger.info("[INFO" + get_current_time() + "]" + log_msg)
        remove_handler('info')

    @staticmethod
    def critical(log_msg):
        add_handler('critical')
        logger.critical("[CRITICAL" + get_current_time() + "]" + log_msg)
        remove_handler('critical')

# if __name__ == '__main__':
#     MyLog.debug("This is debug message")
#     MyLog.info("This is info message")
#     MyLog.error("This is error msessage")
#     MyLog.warning("This is warning message")
#     MyLog.critical("This is critical message")