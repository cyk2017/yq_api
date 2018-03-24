#!/usr/bin/env python
#-*- coding:utf-8 -*-
from unittest import TestCase
import paramunittest
from common.config import Config,data_path,url_file
from common.log import MyLog
from common.file_reader import ExcelReader
from common.my_http import My_http

excel=data_path+'/case.xls'
login_xls=ExcelReader(excel,'login').data
My_http=My_http()
@paramunittest.parametrized(*login_xls)
class Login(TestCase):
    def setParameters(self,case_name,method,account,password,result,code,msg):
        '''
        设置params
        :param case_name:
        :param method:
        :param token:
        :param account:
        :param password:
        :param code:
        :param msg:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        #self.token = str(token)
        self.account = str(account)
        self.password = str(password)
        self.result = str(result)
        self.code = str(code)
        self.msg = str(msg)
        self.return_json = None
        self.info = None

    def description(self):
        '''
        测试描述
        :return:
        '''
        self.case_name

    def setUp(self):
        '''

        :return:
        '''
        self.log=MyLog.get_log()
        self.logger=self.log.get_logger()
        print(self.case_name+'-测试开始前准备')

    def test_login(self):
        '''
        测试内容
        :return:
        '''
        #设置url
        self.url=Config(url_file).get('login')
        My_http.set_url(self.url)
        print('第一步：设置url:'+self.url)
        #登录不需要token
        # if self.token=='0':
        #     token=Config().get('')
        # elif self.token == '1':
        #     token = None

        #设置headers
        headers=Config().get('headers')
        #headers['jcobToken']=token
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
            'account':self.account,
            'password':self.password
        }
        My_http.set_data(data)
        print(data)
        print('第四步：设置请求数据')

        #发送请求
        self.return_json=My_http.postWithJson()
        print(self.return_json.json())
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第五步：发送请求\n\t\t请求方法：" + method)

        #校验结果
        self.check_result()
        print('第六步：检查结果')

    def tearDown(self):
        '''

        :return:
        '''
        # info=self.info
        # if info['token'] == 0:
        #     # # get uer token
        #     # token_u = common.get_value_from_return_json(info, 'member', 'token')
        #     # # set user token to config file
        #     # localReadConfig.set_headers("TOKEN_U", token_u)
        #     pass
        # else:
        #     pass
        self.log.build_case_line(self.case_name, str(self.info['success']))
        print("测试结束，输出log完结\n\n")

    def check_result(self):
        """
        check test result
        :return:
        """
        self.info = self.return_json.json()
        # show return message
        #common.show_return_msg(self.return_json)

        if self.result == '0':
            #email = common.get_value_from_return_json(self.info, 'member', 'email')
            #self.assertEqual(self.info['code'], self.code)
            self.assertEqual(str(self.info['success']), self.msg)
            #self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['errorCode'], self.code)
            self.assertEqual(self.info['errorMsg'], self.msg)