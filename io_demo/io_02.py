#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

from io import StringIO
from io import BytesIO

#StringIO
f = StringIO()
f.write('666')
f.write(' ')
f.write('999')
print(f.getvalue())

#BytesIO
f1 = BytesIO()
f1.write('中国'.encode('utf-8'))
print(f1.getvalue())