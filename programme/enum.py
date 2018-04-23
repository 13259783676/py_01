#coding=utf-8
#description：枚举
_author_ = 'Kai,Chen'
_time_ = '2018/4/23'

from enum import Enum

month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#可以直接使用Month.Jan来引用一个常量
