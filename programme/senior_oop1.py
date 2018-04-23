#coding=utf-8
#description：高级面向对象编程：使用__slots__
_author_ = 'Kai,Chen'
_time_ = '2018/4/18'

#可以随便添加属性
class Student(object):
    pass

s = Student()
s.name = 'zhangsan'
s.age = 20
s.grade = 60
print(s.name)
print(s.age)
print(s.grade)



#使用__slots__
class Person(object):
    #规定本类的属性，仅在本类中有用，在子类中没有作用
    __slots__ = ('name','age','job')

class Teacher(Person):
    pass

t1 = Teacher()
t1.subject = 'ShanXi English'
t1.name = '陈老师'
print(t1.subject,t1.name)




