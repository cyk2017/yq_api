#!/usr/bin/env python
#-*- coding:utf-8 -*-
from common.my_http import My_http

class Post(My_http):
    '''发布帖子接口'''

    def post(self, title, content, clubId):
        '''发帖，title：帖子标题。content：帖子内容。clubid:聊吧id。'''
        post_url = self.host + '/api/user/jcob/savePost?'
        post_json = {
            'title': title,
            'content': content,
            'clubId': clubId
        }
        post = self.session.post(post_url, headers=self.headers, params=self.params, json=post_json, verify=False)
        return post


if __name__ == '__main__':
    title = '12月份了！'
    content = '额企鹅企鹅企鹅而且而且额请问请问我去额额外额企鹅其味无穷额闻气味王企鹅无群二无群二问问群二无群二请问请问我去恶趣味而且'
    clubid = 101
    r = Post().post(title, content, clubid)
    print(r.status_code)
    print(r.json())