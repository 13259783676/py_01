#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

from collections import *

#namedtuple
point=namedtuple('point',['x','y'])
p=point(1,2)
print(p.x)

#deque
dq=deque(['a', 'b', 'c'])
dq.append('d')
dq.appendleft('0')

#defaultdict
dd = defaultdict(lambda : 'N/A')
dd['name']='bill'
print(dd['name'])
print(dd['grade'])

#OrderedDict
d=dict([('a',1), ('b',2), ('c',3)])
print(d)

#Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch]+1
print(c)


