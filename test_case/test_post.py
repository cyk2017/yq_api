#!/usr/bin/env python
#-*- coding:utf-8 -*-
import paramunittest
from unittest import TestCase
from common.get_token import Get_token
from common.my_http import My_http
from common.config import Config,data_path,url_file
from common.file_reader import ExcelReader
from common.log import MyLog

My_http=My_http()
excel=data_path+'case.xls'
post_xls=ExcelReader(excel,'post').data
@paramunittest.parametrized(*post_xls)
class Post(TestCase):
    '''
    发布帖子接口验证
    '''
    def setParameters(self, case_name, method, token,title,content,clubId,result,success,msg):
        '''
        设置params
        :param case_name:
        :param method:
        :param token:
        :param clubId:
        :param code:
        :param msg:
        :param content:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.clubId=clubId
        self.content=content
        self.title=title
        self.result = str(result)
        self.success=success
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def description(self):
        '''
        测试用例描述
        :return:
        '''
        self.case_name

    def setUp(self):
        '''

        :return:
        '''
        self.log = MyLog.get_log()
        self.logger = self.log.get_logger()
        print(self.case_name + '-测试开始前准备')

    def test_post(self):
        '''
        发帖接口测试
        :return:
        '''
        # 设置url
        self.url = Config(url_file).get('post')
        My_http.set_url(self.url)
        print('第一步：设置url:' + self.url)
        if self.token == '0':
            token = Get_token().get_token()
        elif self.token == '1':
            token = None

        #设置headers
        headers = Config().get('headers')
        headers['jcobToken'] = token
        My_http.set_headers(headers)
        print(headers)
        print('第二步：设置header（token等）')

        #设置params
        params=Config().get('params')
        My_http.set_params(params)
        print(params)
        print('第三步：设置params')

        #设置data
        data={
            'title':self.title,
            'content':self.content,
            'clubId':self.clubId
        }
        My_http.set_data(data)
        print(data)
        print('第四步：设置data')

        # 发送请求
        self.return_json = My_http.postWithJson()
        print(self.return_json.json())
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第五步：发送请求\n\t\t请求方法：" + method)

        #检查结果
        self.check_result()

    def tearDown(self):
        '''

        :return:
        '''
        self.log.build_case_line(self.case_name, str(self.info['isSuccess']))
        print("测试结束，输出log完结\n\n")

    def check_result(self):
        '''
        检查返回结果
        :return:
        '''
        self.info=self.return_json.json()
        if self.result == '0':

            self.assertEqual(str(self.info['isSuccess']), self.success)
            self.assertEqual(str(self.info['msg']),self.msg)
            # self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['isSuccess'], self.success)
            self.assertEqual(self.info['msg'], self.msg)