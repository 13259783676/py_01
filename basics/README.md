#### 1.输出print()
```
>>> print('hello, world')
hello, world

>>> print('The quick brown fox', 'jumps over', 'the lazy dog')
The quick brown fox jumps over the lazy dog
```
print()会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来的

#### 2.输入input()
```
name = input()
print('hello,', name)
```
input()中还可以带参数，作为提示语
```
name = input('Please enter')
print('hello,', name)
```

#### 3.退出
用```exit()```退出Python

#### 运行.py文件
```
C:\work> python hello.py
Hello, world!
```

#### 4.语法
1. #开头的语句是注释
2. 其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块
3. 使用==4个空格==的缩进


#### 5.数据类型
##### 1. 整数
 Python可以处理任意大小的整数，当然包括负整数
 (16位进制的书用0x前缀+数表示)
##### 2. 浮点数
1.23x109就是1.23e9

##### 3. 字符串
注意转义
```
name='I\'m \"ok\"!'
print(name)
```

关于多行字符
```
print(' 1\n'
      '2\n'
      '3\n')
```

python ```提供换行
```
print('''line1
line2
line3''')
```

##### 4. 布尔值
在Python中，可以直接用True、False表示布尔值
if-else:
```
if age >= 18:
    print('adult')
else:
    print('teen')
```
```
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
```

##### 5.空值
空值是Python里一个==特殊==的值，用==None==表示

##### 6.变量
变量名必须是大小写英文、数字和_的组合，且不能用数字开头

##### 6.常量
通常用全部大写的变量名表示常量
```
PI = 3.14159265359
```
/除法计算结果是浮点数
```
>>> 10 / 3
3.3333333333333335
```

还有一种除法是//，称为地板除
```
>>> 10 // 3
3
```

##### 7.编码
ord()  chr()
encode()  decode()
```
>>> ord('中')
20013
>>> chr(20013)
中
>>> '中国'.encode('utf-8')
b'\xe4\xb8\xad\xe5\x9b\xbd'
>>> b'\xe4\xb8\xad\xe5\x9b\xbd'.decode()
中国
```

#### 6.list
Python内置的一种数据类型是列表：list,是一种有序的集合，可以随时添加和删除其中的元素
元素使用-1获取最后一个元素
```
>>> list=['duck','lion','monky']
['tiger', 'lion', 'monky']
>>> list[-1]
monky
```
len() 获取长度
```
>>> len(list)
3
```
appen(e)
向集合末尾插入一个元素
```
>>> list=['duck','lion','monky']
['tiger', 'lion', 'monky']
>>> list.append('donkey')
['tiger', 'lion', 'monky','donkey']
```
insert(index,e) 将元素插入到指定位置(指定索引位置，第一个参数不能为空)
```
>>> list=['duck','lion','monky']
['tiger', 'lion', 'monky']
>>> list.insert(1,'dog')
['lion', 'dog', 'monky', 'donkey']
```
pop()/pop)(index) 删除 末尾/指定索引 元素
```
>>> list=['duck','lion','monky']
['tiger', 'lion', 'monky']
>>> list.pop(1)
['duck', 'monky']
```
二维集合
```
>>> s = ['python', 'java', ['asp', 'php'], 'scheme']
```
等价于
```
>>> p = ['asp', 'php']
>>> s = ['python', 'java', p, 'scheme']
```

#### 7.tuple
tuple和list非常类似，但是tuple一旦初始化就不能修改
```
>>> tuple=('mokey','duck','dog')
('mokey', 'duck', 'dog')
```
#### 8.循环
1. for x in ...
把每个元素代入变量x
```
>>> animals=['dog','cat','donkey']
>>> for animal in animals:
>>> print(animal)
dog
cat
donkey
```
```
>>>for num in range(100):
    print(num)
0
1
....
99
```

#### 9.dict(map)
```
>>>d={'Michael': 95, 'Bob': 75, 'Tracy': 85}
>>>d['Michael']
```
pop(key)删除对应key的元素

#### 10.set
在set中，没有重复的key
```
>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
```
add(key) 添加元素（可以重复添加，但不会有效果）
