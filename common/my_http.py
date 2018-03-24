#!/usr/bin/env python
#-*- coding:utf-8 -*-
# import requests
# from common.config import Config
# from common.get_token import Get_token
# class My_http():
#     '''http请求父类'''
#     host=Config().get('host')
#     params=Config().get('params')
#     token=Get_token().get_token()
#     agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'
#     headers={
#         'Accept': 'application/json, text/plain, */*',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Accept-Language': 'zh-CN,zh;q=0.9',
#         'User-Agent': agent,
#         'deviceUuid': '123456',
#         'jcob_token':token
#     }
#     session=requests.session()
#     def __init__(self,host=host,headers=headers,params=params,session=session):
#         self.host=host
#         self.headers=headers
#         self.params=params
#         self.session=session

import requests
from common.config import Config,data_path
from common.log import MyLog as Log


class My_http:

    def __init__(self):
        global scheme,host,port,timeout
        scheme=Config().get('scheme')
        host=Config().get('host')
        port=Config().get('port')
        timeout=Config().get('timeout')
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = scheme + '://' + host + url
        print(self.url)

    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_files(self, filename):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = data_path + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

            # defined http get method

    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except Exception as e:
            self.logger.error("get请求出错", e)
            return None

            # defined http post method
            # include get params and post data
            # uninclude upload file

    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data,
                                     timeout=float(timeout))
            # response.raise_for_status()
            return response
        except Exception as e:
            self.logger.error("post请求出错",e)
            return None

            # defined http post method
            # include upload file

    def postWithFile(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files,
                                     timeout=float(timeout))
            return response
        except Exception as e:
            self.logger.error("post请求出错", e)
            return None

            # defined http post method
            # for json

    def postWithJson(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params,json=self.data, timeout=float(timeout))
            return response
        except Exception as e:
            self.logger.error("post请求出错", e)
            return None

if __name__ == "__main__":
    My_http().set_url('/api/login/?')
    My_http().post()
