#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

import re

#强烈建议使用Python的r前缀，就不用考虑转义的问题了
print(re.match(r'\d{3}','12'))


#切分字符串
print('a b    c'.split(' '))

print(re.split(r'\s+','a b    c'))

