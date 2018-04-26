# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

# 导入MySQL驱动:
import mysql.connector

# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='root', database='db')
cursor = conn.cursor()
# 创建user表:
# cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
