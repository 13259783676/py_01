#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

import itertools

#无限迭代
natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#     if n >=100:
#         break

#cycle()会把传入的一个序列无限重复下去
ce = itertools.cycle('ABC')
# for n in ce:
#     print(n)

#repeat()
rt = itertools.repeat('ABC',3)
for n in rt:
    print(n)

#takewhile()
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x:x<99,natuals)
for n in ns:
    print(n)