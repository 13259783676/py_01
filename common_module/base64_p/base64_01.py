#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

import base64

site1='https://www.baidu.com/'
print(site1)


b_en=base64.b64encode(b'binary\x00string')
print(b_en)
b_de=base64.b64decode(b_en)
print(b_en)