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
plan_center_xls=ExcelReader(excel,'plan_center').data
My_http=My_http()
@paramunittest.parametrized(*plan_center_xls)
class Plan_center(TestCase):
    '''
    推荐大厅接口测试
    '''
    def setParameters(self, case_name, method, token,result, code,amountMode,leagueId,notWinRefund,ownBuyAmount,playType,publishType,raceType,sortType,status):
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
        self.result = str(result)
        self.code = str(code)
        self.amountMode=str(amountMode)
        self.leagueId = list(leagueId)
        self.notWinRefund=notWinRefund
        self.ownBuyAmount=ownBuyAmount
        self.playType=str(playType)
        self.publishType=publishType
        self.raceType = raceType
        self.sortType = sortType
        self.status=status
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

    def test_wallet_list(self):
        # 设置url
        plan_center = Config(url_file).get('plan_center')
        self.url=plan_center
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
        My_http.set_params(params)
        print('第三步：设置params')
        print(params)


        #设置data
        data={'amountMode': self.amountMode,
              'leagueId': self.leagueId,
              'notWinRefund':self.notWinRefund,
              'ownBuyAmount':self.ownBuyAmount,
              'playType': self.playType,
              'publishType': self.publishType,
              'raceType':self.raceType,
              'sortType':self.sortType,
              'status':self.status}
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
            # self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['errorCode'], self.code)
            self.assertEqual(self.info['errorMsg'], self.msg)