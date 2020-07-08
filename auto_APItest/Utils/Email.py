# -*- coding: utf-8 -*- 
# @Create_Time : 2019/4/14 14:38
# @Author : tester_ye 
# @File : Email.py

'''
python的smtplib封装了smtp协议
'''
import time
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from Datas import Constans
from Utils import Log
from Config.Config import Config

class SendMail:

    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def send_mail(self):
        #读取配置文件，邮件发送者地址，接收者地址
        sender = self.config.sender
        receiver = self.config.receiver
        smtpserver = self.config.smtpserver
        username = self.config.username
        password = self.config.password
        result = Constans.RESULT_LIST
        stress = Constans.STRESS_LIST

        #实例化附件邮件
        message = MIMEMultipart()
        #设置邮件的三个头部信息，From、To、Subject
        message['From'] = Header(sender,'utf-8')
        message['To'] = Header(receiver,'utf-8')
        date = time.strftime("-%Y-%m-%d %H-%M-%S",time.localtime(time.time()))
        title = date + '测试报告'
        message['Subject'] = Header(title,'utf-8')

        #邮件正文内容,MIMEText参数，文本内容、文本格式、编码方式
        body = '自动化测试报告:\n 接口也响应时间:{0} \n 测试结果: {1}\n'.format(stress,result)
        message.attach(MIMEText(body, 'plain', 'utf-8'))

        try:
            #windows
            # smtp = smtplib.SMTP()
            # smtp.connect(smtpserver)
            #linux
            smtp = smtplib.SMTP_SSL(smtpserver)
            smtp.ehlo(smtpserver)
            smtp.login(username,password)
            smtp.sendmail(sender,receiver,message.as_string())
        except smtplib.SMTPException as e:
            self.log.error("邮件发送失败" + str(e))

        else:
            self.log.info("邮件发送成功")

        finally:
            smtp.quit()

# if __name__ == '__main__':
#     sdm = SendMail()
#     sdm.send_mail()