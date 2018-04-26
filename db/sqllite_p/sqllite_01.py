# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

import sqlite3, uuid

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')

cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS user')
cursor.execute('CREATE TABLE user(id VARCHAR(40) PRIMARY KEY, name VARCHAR(20), grade INT(3))')
# 继续执行一条SQL语句，插入一条记录:
uid = uuid.uuid1().__str__().replace("-", '')
cursor.execute('INSERT INTO user(id,name,grade) VALUES (\'001\', \'有意思\', 100)')
cursor.execute('INSERT INTO user(id,name,grade) VALUES (\'002\', \'bill\', 70)')
cursor.execute('INSERT INTO user(id,name,grade) VALUES (\'003\', \'bob\', 85)')
print(cursor.rowcount)
cursor.close()
conn.commit()
conn.close()



#查询
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM user WHERE  grade >= ?',('80',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()

