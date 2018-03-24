#!/usr/bin/env python
#-*- coding:utf-8 -*-
# from common.my_http import My_http
# class Login(My_http):
#
#     def login(self,name,password):
#         login_url=self.host+'/api/login/?'
#         login_json={
#             "account":name,
#             "password" : password
#         }
#         login=self.session.post(login_url,headers=self.headers,params=self.params,json=login_json,verify=False)
#         return login
#
# if __name__=='__main__':
#     r=Login().login("qwerty146","trbHwtMf9lvEV6fcOP9EdG+Gj4Atmi6A24s/4ZdnKixomhsttMB8NNUqqIdkw8etwPmUGkUOVrjuCgUR4xy1cWXJXyAoTLVkrWYoWETl4AtZ6onTFwNeu7Dg/dROU8T2qGZyzg4Y5OChNSYHCn0LbTZiCaYN5YpI9utogGxWYWQ=")
#     print(r.json())

import requests
class Login():

    def login(self):
        login_url='http://app-daily.ttyingqiu.com/api/login/?'
        login_params={
            'agentId':'2335034',
            'appVersion':'4.9.0',
            'platform':'win32',
            'version':None
        }
        agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
        login_headers={'deviceUuid': '123456',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept': 'application/json, text/plain, */*',
                       'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
                       'Accept-Language': 'zh-CN,zh;q=0.9'
                       }
        login_json={
            "account":'qwerty146',
            "password" : 'trbHwtMf9lvEV6fcOP9EdG+Gj4Atmi6A24s/4ZdnKixomhsttMB8NNUqqIdkw8etwPmUGkUOVrjuCgUR4xy1cWXJXyAoTLVkrWYoWETl4AtZ6onTFwNeu7Dg/dROU8T2qGZyzg4Y5OChNSYHCn0LbTZiCaYN5YpI9utogGxWYWQ='
        }
        session=requests.session()
        login=requests.post(login_url,headers=login_headers,params=login_params,json=login_json,verify=False)
        return login

r=Login().login()
print(r.status_code)