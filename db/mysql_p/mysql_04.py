# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/7/27'

import pymysql, uuid

conn = pymysql.connect(host='123.56.22.89', user='root', password='yierer333', database='zabbix', charset='utf8')
cursor = conn.cursor()

cursor.execute('select * from cpuandtcpdata WHERE zabbixdate = %s', 20180628)
values = cursor.fetchall()
print(values)

item = values[0]
print(item)
print(type(item[1]))


cursor.close()
