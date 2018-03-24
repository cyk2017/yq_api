#!/usr/bin/env python
#-*- coding:utf-8 -*-
from common.my_http import My_http


class Change_password(My_http):
    '''修改密码'''
    def send_message(self,phone):
        '''发送验证码接口'''
        send_message_url=self.host+'/api/uc/modify/changePassword/sendMessage?'
        send_message_json={
            'phone':phone
        }
        send_message=self.session.post(send_message_url, headers=self.headers,json=send_message_json,params=self.params, verify=False)
        return send_message
