#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

import pickle
d = dict(name='Bob', age=20, score=88)
print(d)
pickle.dumps(d)

#写
f = open('pickle/foo.txt','wb')
pickle.dump(d,f)
f.close()

#读
f1 = open('pickle/foo.txt','rb')
d1 = pickle.load(f1)
f1.close()
print(d1)


