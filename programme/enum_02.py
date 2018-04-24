#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

from enum import Enum , unique

class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

for name, member in Weekday.__members__.items():
    print(name, '=>', member)