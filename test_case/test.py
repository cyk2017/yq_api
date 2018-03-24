#!/usr/bin/env python
#-*- coding:utf-8 -*-
import requests

from common.get_token import Get_token
class My_http():
    '''http请求父类'''

    #session=requests.session()
    def haha(self):
        host = 'http://app-daily.ttyingqiu.com'
        params = {
            'agentId': '2335034',
            'appVersion': '4.9.3',
            'platform': 'win32',
            'version':'',
            # 'templateId':1374
        }
        #token = Get_token().get_token()
        agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1'
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'User-Agent': agent,
            'deviceUuid': '123456',
            'Content-Type': 'application/json;charset=UTF-8',
            'jcobToken': '3e69e3a930bce3ee1bd2fd0a602b39ab'
        }
        data = {'gameType': "4075", 'dateIndex': 7, 'qiuFlag': 1}
        test_url='http://app-daily.ttyingqiu.com/api/formalExpert/scoreInfo/2387?'
        #print(token)
        print(headers)
        print(params)
        print(data)
        test_list = requests.post(url=test_url, headers=headers, params=params,data=data,verify=False)
        return test_list

if __name__=='__main__':
    r=My_http().haha()
    print(r.json())




