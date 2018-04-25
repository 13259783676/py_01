#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

import hashlib

#md5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


md5_name = hashlib.md5()
md5_name.update('13012345678'.encode('utf-8'))
print(md5_name.hexdigest())

