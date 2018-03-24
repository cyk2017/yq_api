#!/usr/bin/env python
#-*- coding:utf-8 -*-
from common.my_http import My_http

class Plan_check(My_http):
    '''查询发布的推荐'''
    def plan_check(self, exportId, dateIndex,race_type):
        '''查询发布的推荐'''
        plan_check_url = self.host + '/api/expertHome/plan/1?'
        plan_check_json = {
            'searchIndex': 10,
            'exportId': exportId,
            'raceTypeId': race_type,  # 竞足是1，竞篮是2.
            'dateIndex': dateIndex,  # 查询天数7表示一周，14表示两周，30表示一个月
            'gameType': 407  # 玩法
        }
        plan_check = self.session.post(plan_check_url, headers=self.headers, params=self.params, json=plan_check_json,
                                       verify=False)
        return plan_check


if __name__ == '__main__':
    exportId = 2548  # 2452#2396
    # 查询的结果与token无关，与传入的exportId有关
    dateIndex = 30
    race_type=1
    r = Plan_check().plan_check(exportId, dateIndex,race_type)
    print(r.status_code)
    print(r.json())