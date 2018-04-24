#### 1.错误处理
- 内置异常处理
```
try:
    print('try')
    r = 10/0
    print('result',r)
except ZeroDivisionError as e:
    print('except',e)
finally:
    print('finally')
print('end')
```

- 自定义异常处理
```
try:
    print('try')
    num=int(input('input:'))
    if num <= 0:
        raise DivisorIs0('<= 0')
    print(10/num)
except DivisorIs0 as e:
    print('except',e)
finally:
    print('finally')
print('end')
```

#### 2.调试
- 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
- 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。
-