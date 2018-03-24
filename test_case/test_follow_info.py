#!/usr/bin/env python
#-*- coding:utf-8 -*-
from unittest import TestCase
from common.config import Config,data_path,url_file
from common.file_reader import ExcelReader
import paramunittest
from common.my_http import My_http
from common.log import MyLog
from common.get_token import Get_token

excel=data_path+'case.xls'
follow_info_xls=ExcelReader(excel,'follow_info').data
My_http=My_http()
@paramunittest.parametrized(*follow_info_xls)
class Follow_info(TestCase):
    '''
    我的关注接口测试
    '''
    def setParameters(self, case_name, method, token,focusType,summaryType,needCache,result,code,success,msg):
        '''
        设置params
        :param case_name:
        :param method:
        :param token:
        :param date_index:
        :param code:
        :param msg:
        :return:
        '''
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.focusType = focusType
        self.summaryType = summaryType
        self.needCache = needCache
        self.result = str(result)
        self.code = str(code)
        self.success=success
        self.msg=msg
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

    def test_follow_info(self):
        # 设置url
        follow_info = Config(url_file).get('follow_info')
        self.url=follow_info
        My_http.set_url(self.url)
        print('第一步：设置url:' + self.url)
        if self.token=='0':
            token=Get_token().get_token()
        elif self.token == '1':
            token = None

        # 设置headers
        headers = Config().get('headers')
        headers['jcobToken']=token
        My_http.set_headers(headers)
        print('第二步：设置header（token等）')
        print(headers)

        # 设置params
        params = Config().get('params')
        params['focusType']=self.focusType
        params['summaryType']=self.summaryType
        params['needCache']=self.needCache
        My_http.set_params(params)
        print('第三步：设置params')
        print(params)


        # 发送请求
        self.return_json = My_http.get()
        print(self.return_json.json())
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第四步：发送请求\n\t\t请求方法：" + method)

        # 校验结果
        self.check_result()
        print('第五步：检查结果')

    def tearDown(self):
        '''

        :return:
        '''
        #self.log.build_case_line(self.case_name, str(self.info['success']))
        print("测试结束，输出log完结\n\n")

    def check_result(self):
        '''
        检查测试结果
        :return:
        '''
        self.info = self.return_json.json()
        # show return message
        # common.show_return_msg(self.return_json)

        if self.result == '0':
            # email = common.get_value_from_return_json(self.info, 'member', 'email')
            # self.assertEqual(self.info['code'], self.code)
            print('==================')
            self.assertEqual(self.return_json.status_code, int(self.code))
            self.assertEqual(str(self.info['success']),self.success)
            # self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['errorCode'], self.code)
            self.assertEqual(self.info['errorMsg'], self.msg)