#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
import unittest
from common.log import MyLog as Log
import HTMLTestRunner
from common.config import data_path,test_case_path,Config
from common.my_email import Email

class AllTest:
    def __init__(self):
        # global log, logger, resultPath, on_off
        # log = Log.get_log()
        # logger = log.get_logger()
        # resultPath = log.get_report_path()
        # on_off = localReadConfig.get_email("on_off")
        # self.caseListFile = os.path.join(readConfig.proDir, "caselist.txt")
        # self.caseFile = os.path.join(readConfig.proDir, "testCase")
        # # self.caseFile = None
        # self.caseList = []
        # self.email = MyEmail.get_email()
        global log,logger,result_path,on_off
        log=Log.get_log()
        logger=log.get_logger()
        result_path=log.get_report_path()
        c=Config().get('email')
        on_off=c.get('on_off')
        self.case_list_file=os.path.join(data_path, "case_list.txt")
        self.case_file = test_case_path
        self.case_list = []
        self.email=Email()
    def set_case_list(self):
        """
        set case list
        :return:
        """
        fb = open(self.case_list_file)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):
                self.case_list.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        """
        set case suite
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []

        for case in self.case_list:
            case_name = case.split("/")[-1]
            print(case_name+".py")
            discover = unittest.defaultTestLoader.discover(self.case_file, pattern=case_name + '.py', top_level_dir=None)
            suite_module.append(discover)

        if len(suite_module) > 0:

            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite

    def run(self):
        """
        run test
        :return:
        """
        try:
            suit = self.set_case_suite()
            if suit is not None:
                logger.info("********TEST START********")
                fp = open(result_path, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
                runner.run(suit)
            else:
                logger.info("Have no case to test.")
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("*********TEST END*********")
            fp.close()
            # 邮件发送测试报告
            if on_off == 'on':
                self.email.send_email(result_path)
                logger.info('邮件已成功发送给!!')
            elif on_off == 'off':
                logger.info("Doesn't send report email to developer.")
            else:
                logger.info("Unknow state.")


if __name__ == '__main__':
    obj = AllTest()
    obj.run()