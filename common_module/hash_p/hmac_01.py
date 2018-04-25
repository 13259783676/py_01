#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

import hmac

message = b'keys'
key = b'secret'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())
