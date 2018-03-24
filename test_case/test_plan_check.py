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
plan_check_xls=ExcelReader(excel,'plan_check').data
@paramunittest.parametrized(*plan_check_xls)
class Plan_check(TestCase):
    '''
    发布帖子接口验证
    '''
    def setParameters(self, case_name, method, token,search_index,exportId,race_typeId,date_index,game_type,result, code,success,msg):
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
        self.search_index=search_index
        self.exportId=exportId
        self.race_typeId=race_typeId
        self.date_index=date_index
        self.game_type=game_type
        self.result = str(result)
        self.code = str(code)
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

    def test_plan_check(self):
        '''
        发帖接口测试
        :return:
        '''
        # 设置url
        self.url = Config(url_file).get('plan_check')
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
            'searchIndex':self.search_index,
            'exportId':self.exportId,
            'raceTypeId':self.race_typeId,
            'dateIndex':self.date_index,
            'gameType':self.game_type
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
        #self.log.build_case_line(self.case_name, str(self.info['page']['needData']))
        print("测试结束，输出log完结\n\n")

    def check_result(self):
        '''
        检查返回结果
        :return:
        '''
        self.info=self.return_json.json()
        if self.result == '0':

            self.assertEqual(str(self.info['page']['needData']), self.success)
            #self.assertEqual(str(self.info['msg']),self.msg)
            # self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['errorCode'], self.code)
            self.assertEqual(self.info['errorMsg'], self.msg)