# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/7/27'

import pymysql, uuid

#创建连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='db', charset='utf8')
cursor = conn.cursor()

#查询
sql = "select * from emp"
cursor.execute(sql)
values = cursor.fetchall()
for item in values:
    print(item)
    print(type(item[1]))

