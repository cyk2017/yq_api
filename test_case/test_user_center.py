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
user_center_xls=ExcelReader(excel,'user_center').data#读取测试用例
user_name=Config().get('account')
My_db=My_db()
My_http=My_http()
member_id=My_db.get_member_id(user_name)
@paramunittest.parametrized(*user_center_xls)#循环执行用例

class User_center(TestCase):
    '''
    资讯查询接口
    '''
    def setParameters(self,case_name,method,token,result,code,success,msg,account,attentionOtherCount_attentionMeCount,ableBalance,huoyanWallet):#输入接口参数
        '''
        设置params
        :return:
        '''
        self.case_name=str(case_name)
        self.method=str(method)
        self.token = str(token)
        self.result=str(result)
        self.code=str(code)
        self.success=str(success)
        self.msg=str(msg)
        self.account=My_db.sql(account.format(member_id))
        self.attentionOtherCount_attentionMeCount=My_db.sql(attentionOtherCount_attentionMeCount.format(member_id))
        self.ableBalance=My_db.sql(ableBalance.format(member_id))
        self.huoyanWallet=My_db.sql(huoyanWallet.format(member_id))
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

    def test_user_center(self):
        # 设置url
        wallet_list = Config(url_file).get('user_center')
        self.url = wallet_list
        My_http.set_url(self.url)
        print('第一步：设置url:' + self.url)
        if self.token == '0':
            token = Get_token().get_token()
        elif self.token == '1':
            token = None

        #设置headers
        headers = Config().get('headers')
        headers['jcobToken'] = token #在headers中添加token
        My_http.set_headers(headers)
        print('第二步：设置header（token等）')
        print(headers)

        #设置params
        params = Config().get('params')
        My_http.set_params(params)
        print('第三步：设置params')
        print(params)

        # 发送请求
        self.return_json = My_http.get()
        print(self.return_json.json())
        method = str(self.return_json.request)[
                 int(str(self.return_json.request).find('[')) + 1:int(str(self.return_json.request).find(']'))]#读取请求类型
        print("第四步：发送请求\n\t\t请求方法：" + method)

        # 校验结果
        self.check_result()
        print('第五步：检查结果')

    def tearDown(self):
        '''

        :return:
        '''
        self.log.build_case_line(self.case_name, str(self.info['success']))
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
            self.assertEqual(str(self.info['success']), self.success)#比较接口返回值与预计返回结果是否一致
            self.assertEqual(self.info['userInfo']['account'],self.account[0][0])
            self.assertEqual(self.info['attentionOtherCount'],self.attentionOtherCount_attentionMeCount[0][0])
            self.assertEqual(self.info['attentionMeCount'], self.attentionOtherCount_attentionMeCount[0][1])
            self.assertEqual(self.info['ableBalance'], float(self.ableBalance[0][0]))
            self.assertEqual(self.info['huoyanWallet'], float(self.huoyanWallet[0][0]))
            # self.assertEqual(email, self.email)

        if self.result == '1':
            self.assertEqual(self.info['errorCode'], self.code)
            self.assertEqual(self.info['errorMsg'], self.msg)