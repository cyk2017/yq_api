#!/usr/bin/env python
#-*- coding:utf-8 -*-
from common.my_http import My_http

class My_reply(My_http):
    '''我的评论接口'''

    def my_reply(self,date_index):
        '''我发表的'''
        my_reply_url = self.host +'/api/uc/msgReply/1?'
        my_reply_json={
            'dateIndex':date_index,
            'type':'true'
        }
        my_reply=self.session.post(my_reply_url,headers=self.headers,json=my_reply_json, params=self.params, verify=False)
        return my_reply

    def reply_me(self,date_index):
        '''回复我的'''
        reply_me_url = self.host + '/api/uc/msgReply/1?'
        reply_me_json={
            'dateIndex': date_index,
            'type': 'false'
        }
        reply_me = self.session.post(reply_me_url, headers=self.headers,json=reply_me_json,params=self.params, verify=False)
        return reply_me

if __name__=='__main__':
    r=My_reply().my_reply(30)
    print(r.json())
    q=My_reply().reply_me(90)
    print(q.json())