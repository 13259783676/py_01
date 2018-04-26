# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

import psutil

# 获取CPU信息
# CPU逻辑数量
print(psutil.cpu_count())

print(psutil.cpu_count(logical=False))

