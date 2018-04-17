#### 1.abs() 求绝对值
```
>>> abs(-1.15)
>>> abs(-3e10)
```
#### 2.all() 可迭代
如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False
```
>>> list1=[]
>>> all(list1)
True

>>> list1=['dog','','tigger']
>>> all(list1)
False

>>> list1=[0,'cat','tigger']
>>> all(list1)
False

>>>list1=[None,'cat','tigger']
>>> all(list1)
False
```
#### 3.any()
与all()相反,如果当iterable所有的值都是0、''或False时，那么结果为False，如果所有元素中有一个值非0、''或False，那么结果就为True

#### 4.bool()
除了bool(0)返回Fasle，其他返回True

#### 5.divmod()
divmod()把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
```
>>> divmod(5,2)
(2, 1)
```
#### 6.dir()
返回当前范围内的变量，方法和定义的类型列表

#### 7.enumerate()
将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
```
>>> list2 = ['dog','cat','lion']
list(enumerate(list2))
[(0, 'dog'), (1, 'cat'), (2, 'lion')]
```
与循环使用
```
>>> for i,e in enumerate(list2):
    print(i,e)
0 dog
1 cat
2 lion
```

#### 8.file()
用于创建一个 file 对象，它有一个别名叫 open()
file(name[, mode[, buffering]])
- name -- 文件名
- mode -- 打开模式
- buffering -- 0 表示不缓冲,如果为 1 表示进行行缓冲，大于 1 为缓冲区大小。
```
f = open('E:\python_workspace\demo\py_01\function\test.py','r')
f.read()
```

#### 9.filter()
用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
filter(function, iterable)
- function -- 判断函数
- iterable -- 可迭代对象
```
>>>def is_odd(n):
    return n%2 == 1
>>>list3 = filter(is_odd,range(10))
>>>for e in list3:
     print(e)
1
3
5
7
9
```
python2fileter()返回时list，python3返回一个filter类，实现了__iter__和__next__方法,节约内存

#### 10.format()
```
>>> "{1} {0}".format("hello","world")
world hello
```

#### 11.getattr()
返回一个对象属性值
getattr(object, name[, default])
- object -- 对象
- name -- 字符串，对象属性
- default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError

#### 12.hasattr()
函数用于判断对象是否包含对应的属性
hasattr(object, name)
- object -- 对象
- name -- 字符串，属性名
如果对象有该属性返回 True，否则返回 False

#### 13.hash()
用于获取取一个对象（字符串或者数值等）的哈希值
hash(object)

#### 14.hex()
函数用于将10进制整数转换成16进制(字符串)

#### 15. id()
id() 函数用于获取对象的内存地址
id([object])
```
>>> obj1 = 'aaaa'
>>> id(obj1)
31885888
```

#### 16.oct()
函数用于将一个整数转换成8进制字符串

#### 17.pow()
返回 x的y次方 的值
```
>>> math.pow(2,3)
8.0
```

#### 18.reverse()
用于反向列表中元素
```
>>> list5 = [1,2,3,4,5]
>>> list5.reverse()
[5, 4, 3, 2, 1]
```

#### 19.round()
四舍五入
```
>>> round(80.23456, 2)
80.23
```

#### 20.setattr()
setattr 函数对应函数 getatt()，用于设置属性值，该属性必须存在
setattr(object, name, value)
- object -- 对象
- name -- 字符串，对象属性
- value -- 属性值



