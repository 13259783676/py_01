#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

import os

if os.name == 'nt':
    print('windows')
else:
    print('not is windows')

#系统变量
print(os.environ)
print('path', os.environ.get('PATH'))

#操作文件和路径

#查看当前目录的绝对路径
path = os.path.abspath('.')
print(path)
#在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
new_path = os.path.join(path, 'testdir')
print(new_path)
#然后创建一个目录
os.mkdir(new_path)
#删掉一个目录
os.rmdir(new_path)