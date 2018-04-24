#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

import logging

class DivisorIs0(Exception):
    def __init__(self,msg):
        self.msg = msg


try:
    print('try')
    r = 10/0
    print('result',r)
except ZeroDivisionError as e:
    print('except',e)
finally:
    print('finally')
print('end')

#自定义异常处理
try:
    print('try')
    num=int(input('input:'))
    if num <= 0:
        raise DivisorIs0('<= 0')
    print(10/num)
except DivisorIs0 as e:
    logging.exception(e)
    print('except',e)
finally:
    print('finally')
print('end')

