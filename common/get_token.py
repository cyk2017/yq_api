#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
from common.config import Config
class Get_token:
    '''获取用户token'''
    def __init__(self,):
        self.headers=Config().get('headers')
        self.params=Config().get('params')
        self.account=Config().get('account')
        self.password=Config().get('password')
    def get_token(self):
        login_url='http://app-daily.ttyingqiu.com/api/login/?'

        login_json={
            "account":self.account,
            "password" : self.password
        }
        print(self.headers)
        print(self.params)
        login=requests.post(login_url,headers=self.headers,params=self.params,json=login_json,verify=False)
        print(login.json())
        return login.json()['token']


if __name__=='__main__':
    r=Get_token().get_token()
    print(r)