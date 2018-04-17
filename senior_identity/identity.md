高级特性

#### 1.切片
L = ['dog', 'cat', 'lion', 'donkey', 'duck']
取前3个元素
```
L[0:3]
L[:3]
['dog', 'cat', 'lion']
```
取倒数第一个元素（倒数第一个元素索引为-1）
```
L[-1:]
['duck']
```

#### 2.迭代
```
d = {'cat':'10','lion':200,'duck':50}
for key in d:
    print(key)
    print(d[key])
cat
10
lion
200
duck
50
```
