#!/usr/bin/env python
#-*- coding:utf-8 -*-
from common.my_http import My_http

class Yq_column(My_http):
    '''盈球专栏'''
    def yq_column(self):
        '''盈球专栏查询接口'''
        yq_column_url=self.host+'/api/uc/column/myLook/1?'
        yq_column=self.session.get(yq_column_url,headers=self.headers, params=self.params, verify=False)
        return yq_column

if __name__=='__main__':
    r=Yq_column().yq_column()
    print(r.json())