#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from common.file_reader import YamlReader

class Config:
    def __init__(self,config=r'D:\Program Files (x86)\pycharm\ttyq_api_daily\config\qq.yml'):
        self.config=YamlReader(config).data

    def get(self,element,index=0):
        return self.config[index].get(element)


if __name__=='__main__':
    r=Config().get('headers')
    r['我']=30
    print(r)