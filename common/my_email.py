#!/usr/bin/env python
#-*- coding:utf-8 -*-
import yagmail
from common.config import Config
class Email:
    '''发送邮件'''
    def __init__(self):
        self.email=Config().get('email')
        self.user = self.email.get('user')
        self.password = self.email.get('password')
        self.host = self.email.get('host')
        self.receivers = self.email.get('receivers')  # 支持list
        self.subject = self.email.get('subject')
        self.contens =self.email.get('contens')
        #self.attachments =Config().get('attachments')
    #传入所需发送的报告
    def send_email(self,attachments):
        yag = yagmail.SMTP(user=self.user, password=self.password, host=self.host)
        yag.send(to=self.receivers,subject=self.subject,contents=self.contens,attachments=attachments)

if __name__=='__main__':
    Email().send_email('attachments')
