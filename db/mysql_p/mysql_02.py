# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

import pymysql, uuid

# 创建连接
conn = pymysql.connect(host='localhost', user='root', password='root', database='db', charset='utf8')
cursor = conn.cursor()

# 创建user表
cursor.execute('DROP TABLE  if exists user')
cursor.execute('create table user(id VARCHAR (40) PRIMARY KEY ,name VARCHAR (20),grade int(10))')

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into USER (id,name,grade) VALUES (%s,%s,%s)',
               [uuid.uuid1().__str__().replace("-", ''), 'bill', 78])
cursor.execute('insert into USER (id,name,grade) VALUES (%s,%s,%s)',
               [uuid.uuid1().__str__().replace("-", ''), 'bob', 90])
print(cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()


# 查询
cursor = conn.cursor()
print(cursor.rownumber)
cursor.execute('select * from USER WHERE name = %s',('bob'))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

