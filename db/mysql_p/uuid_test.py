# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

import uuid

uid = uuid.uuid1().__str__()
print(uid)
uid = uid.replace("-",'')
print(uid)
