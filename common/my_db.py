#!/usr/bin/env python
#-*- coding:utf-8 -*-
import pymysql
from common.config import Config
from common.log import MyLog as Log

class My_db:
    '''
    mysql数据库操作类
    '''

    def __init__(self):
        global localhost,db_user,db_password,test_db
        localhost=Config().get('db')['localhost']
        db_user=Config().get('db')['db_user']
        db_password=Config().get('db')['db_password']
        test_db=Config().get('db')['test_db']
        self.localhost=localhost
        self.db_user=db_user
        self.db_password=db_password
        self.test_db=test_db
        self.log = Log.get_log()
        self.logger = self.log.get_logger()

    def sql(self,sql):
        '''
        执行SQL语句，并返回查询结果
        :return:
        '''
        #打开数据库连接
        db=pymysql.connect(self.localhost,self.db_user,self.db_password,self.test_db)
        #使用cursor()方法创建游标对象cursor
        cursor = db.cursor()
        # 使用execute()方法执行sql查询
        sql_result=[]
        try:
            cursor.execute(sql)
            sql_result = cursor.fetchall()
        except Exception as e:
            self.logger.error('数据查询出错！')
        if sql_result==():
            self.logger.error('无法查询到该数据。')
            return None
        elif sql_result[0][0]==None:
            return [(0,), ]
        else:
            return sql_result #返回值为一个list

    def get_member_id(self,user_name):
        member_id_sql="SELECT id FROM member WHERE nick_name='{0}'".format(user_name)
        result=My_db().sql(member_id_sql)
        if result==None:
            pass
        else:
            return result[0][0]


if __name__=='__main__':
    # member_id=2396
    # w='SELECT SUM(happen_amount) FROM member_huoyan_wallet_log WHERE member_id={0} AND wallet_op_type=1 AND DATE_SUB(CURDATE(), INTERVAL 90 DAY) <= DATE(create_time)'
    # sql=w.format(member_id)
    #r=My_db().sql('SELECT SUM(happen_amount) FROM member_wallet_log WHERE member_id=2396 AND wallet_op_type=1 AND DATE_SUB(CURDATE(), INTERVAL 90 DAY) <= DATE(create_time)')
    #r=My_db().sql("SELECT id FROM member WHERE nick_name='qwert146'")
    sql='SELECT lhcount FROM tj_game_league_score WHERE jcob_member_id={0} AND league_id=0 AND game_id={1}'
    r=My_db().sql('SELECT lhcount FROM tj_game_league_score WHERE jcob_member_id={0} AND league_id=0 AND game_id={1}')
    #print(sql)
    print(r[0][0])#返回值为一个list，list里面参数为tuple