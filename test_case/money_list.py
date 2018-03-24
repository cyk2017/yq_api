#!/usr/bin/env python
#-*- coding:utf-8 -*-
from common.my_http import My_http

class Money_list(My_http):

    def money_list(self,date_index):
        '''金币流水查询'''
        money_list_url=self.host+'/api/user/queryHuoyanWalletList/{0}/1'.format(date_index)
        money_list = self.session.get(money_list_url, headers=self.headers, params=self.params, verify=False)
        print(self.headers)
        return money_list

if __name__=='__main__':
    for date_index in (7,14,30,90):
        r=Money_list().money_list(date_index)
        print(r.json()['memberHuoyanWallets'])