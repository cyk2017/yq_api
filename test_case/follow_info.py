#!/usr/bin/env python
#-*- coding:utf-8 -*-
from common.my_http import My_http

class Follow_info(My_http):
    '''我的关注'''
    def follow_expert(self):
        '''关注的人'''
        follow_expert_url=self.host+'/api/follow/queryFollowInfo?'
        follow_expert=self.session.get(follow_expert_url,headers=self.headers, params=self.params, verify=False)
        return follow_expert
    def test(self):
        pass
if __name__=='__main__':
    r=Follow_info().follow_expert()
    print(r.json()['success'])