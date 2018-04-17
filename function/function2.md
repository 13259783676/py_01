#### 1.自定义函数
```
def my_abs(n):
    if not isinstance(n,(int,float)):
        raise TypeError('类型错误')
    if n >= 0:
        return n
    else:
        return -n

num = int(input('input:'))
print(my_abs(num))
```

#### 2.空函数
果想定义一个什么事也不做的空函数，可以用pass语句
```
>>> def none_f():
>>>    pass
```

#### 3.多个返回值
```
def muti_return(x,y,z):
return x+1,y+1,z+1
print(muti_return(1,2,3))
```

#### 4.默认参数
```
def default_params(x,y=2):
    if x <= 0:
        return -x,y
    else:
        pass

print(default_params(-4,3))
print(default_params(-4))
```

#### 5.可变参数
```
def pow_sum(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num*num
    return sum

numbers = range(10)
print(pow_sum(*numbers))
```
#### 6.关键字参数
```
def key_params(name,age,**job):
    print('name:',name,'age:',age,'other:',job)
key_params('lion',20)
---------------------
name: lion age: 20 other: {}
```
```
key_params('lion',20,addr='xian',sex='男')
name: lion age: 20 other: {'addr': 'xian', 'sex': '男'}
```

### 参数小结:
- *args是可变参数，args接收的是一个tuple
- **kw是关键字参数，kw接收的是一个dict
- 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过* args传入：func(*(1, 2, 3))
- 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过** kw传入：func(**{'a': 1, 'b': 2})
