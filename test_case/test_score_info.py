#!/usr/bin/env python
#-*- coding:utf-8 -*-
from unittest import TestCase
from common.config import Config,data_path,url_file
from common.file_reader import ExcelReader
import paramunittest
from common.my_http import My_http
from common.my_db import My_db
from common.log import MyLog
from common.get_token import Get_token

excel=data_path+'case.xls'
score_info_xls=ExcelReader(excel,'score_info').data
My_http=My_http()
My_db=My_db()

@paramunittest.parametrized(*score_info_xls)
class Score_info(TestCase):
    '''
    专家、红人主页战绩接口测试
    '''
    def setParameters(self, case_name, method, token,member_id,result,code,dateIndex,gameType,qiuFlag,SQL):
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
        user_member_id=My_db.sql(member_id)[1][0]
        self.case_name = str(case_name)
        self.method = str(method)
        self.token = str(token)
        self.member_id=user_member_id
        self.result = str(result)
        self.code = str(code)
        self.dateIndex=str(dateIndex)
        self.gameType = gameType
        self.qiuFlag=qiuFlag
        self.sql_result=My_db.sql(SQL.format(self.member_id,gameType))
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

    def test_score_info(self):
        # 设置url
        score_info = Config(url_file).get('score_info')
        self.url=score_info.format(self.member_id)
        My_http.set_url(self.url)
        print('第一步：设置url:' + self.url)
        if self.token=='0':
            token=Get_token().get_token()
        elif self.token == '1':
            token = None

        # 设置headers
        headers = Config().get('headers')
        headers['jcobToken']=token
        headers['Content-Type'] = 'application/json;charset=UTF-8'
        My_http.set_headers(headers)
        print('第二步：设置header（token等）')
        print(headers)

        # 设置params
        params = Config().get('params')
        My_http.set_params(params)
        print('第三步：设置params')
        print(params)

        #设置data
        data={'dateIndex': self.dateIndex,
              'gameType':self.gameType,
              'qiuFlag':self.qiuFlag}
        My_http.set_data(data)
        print(data)
        print('第四步：设置data')

        # 发送请求
        self.return_json = My_http.postWithJson()
        print(self.return_json.json())
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]
        print("第五步：发送请求\n\t\t请求方法：" + method)

        # 校验结果
        self.check_result()
        print('第六步：检查结果')

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
            self.assertEqual(self.info['scoreDayRecord']['d7ReturnRatio'],float(self.sql_result[0][0]))
            self.assertEqual(self.info['scoreDayRecord']['d7WinRatio'], float(self.sql_result[0][1]))
            self.assertEqual(self.info['scoreDayRecord']['d15ReturnRatio'], float(self.sql_result[0][2]))
            self.assertEqual(self.info['scoreDayRecord']['d15WinRatio'], float(self.sql_result[0][3]))
            self.assertEqual(self.info['scoreDayRecord']['d30WinRatio'], float(self.sql_result[0][4]))
            self.assertEqual(self.info['scoreDayRecord']['d30ReturnRatio'], float(self.sql_result[0][5]))
            self.assertEqual(self.info['scoreDayRecord']['lhcount'], float(self.sql_result[0][6]))
            # self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['errorCode'], self.code)
            self.assertEqual(self.info['errorMsg'], self.msg)