#coding=utf-8
#description：枚举
_author_ = 'Kai,Chen'
_time_ = '2018/4/23'

from enum import Enum

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#可以直接使用Month.Jan来引用一个常量
for name,nn in Month.__members__.items():
    print(name,nn.value,'月')



