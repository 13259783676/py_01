# coding=utf-8
# description：
_author_ = 'kai,chen'
_time_ = '2018/4/25'

import requests

# 使用reuqests
r = requests.get('https://www.baidu.com/')
print(r.status_code, r.reason)
print(r.encoding)
print(r.content)
print('----------------------------------')

# 返回json
r1 = requests.get(
    'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3d%202151330&format=json')
print(type(r1))
print('status:%s, result:%s' % (r1.status_code, r1.reason))
print(r1.json())
print('---------------------------------')

r2 = requests.get('')
print(r2)
print('status:%s, result:%s' % (r2.status_code, r2.reason))
print('r2编码:%s' % r2.encoding)
print('r2-url:%s' % r2.url)
print(r2.json())
