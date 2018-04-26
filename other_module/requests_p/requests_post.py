# -*- coding: utf-8 -*-
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/26'

import requests

# post模拟登陆
r = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(r.status_code)
print('---------------------------')

# post获得数据
data = {
    "categoryCode":"010201",
    "keyword":""
}
r2 = requests.post('', json=data)
print(r2)
print('r2_status:%s, r2_result:%s'%(r2.status_code, r2.reason))
print(r2.text)
print(r2.json())