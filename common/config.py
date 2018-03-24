#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os
from common.file_reader import YamlReader

base_path=os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '\..')
config_file=base_path+'\config\config.yml'
url_file=base_path+'\config\\ttyq_url.yml'
data_path=base_path+'\data\\'
log_path=base_path+'\log\\'
report_path=base_path+'\\report\\'
test_case_path=base_path+'\\test_case\\'

class Config():
    def __init__(self,config=config_file):
        self.config=YamlReader(config).data

    def get(self,element,index=0):
        return self.config[index].get(element)

