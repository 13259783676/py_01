#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

import json
d1 = dict(name='bill',age=20,grade=70,goon=True)
d2 = dict(name='james',age=19,grade=90,goon=True)
ds = [d1,d2]
print(json.dumps(ds))


