#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

import itertools

#chain()
ch = itertools.chain('ABC','XYZ')
for n in ch:
    print(n)

#groupby()
for key,group in itertools.groupby('AAABBBCCDDD'):
    print(key, list(group))
