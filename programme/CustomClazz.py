#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/23'

#定制类
class Student(object):

    def __init__(self,name):
        self.name = name
    def __str__(self):
        return '(name:%s)' %self.name

print(Student('爱似币'))

#__iter__(斐波那契数列)
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值
for a in Fib():
    print(a)

#__getitem__
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a ,b = b, a+b
        return a
f = Fib2()
print(f[4])

#__getattr__
class Teacher(object):
    def __getattr__(self, attr):
        if attr == 'name':
            return '陈老师1'

tea = Teacher()
tea.name = '陈老师'
print(tea.name)
print(tea.__getattr__('name'))


#__call__
class Dog(object):
    def __init__(self, name):
        self.name = name
    def __set_name__(self, name):
        self.name = name
    def __call__(self):
        print('这是一只狗，叫%s'%self.name)
dog = Dog('大黄')
dog.__call__()
