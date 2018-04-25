#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

import json

class Student(object):
    def __init__(self,name,grade,age):
        self.name = name
        self.grade = grade
        self.age = age
    def __str__(self):
        return '(Student: %s, %d, %d)' % (self.name, self.grade, self.age)
class Clazz(object):
    def __init__(self,levelName,className,*Students):
        self.levelName = levelName
        self.className = className
        self.Students = Students

stu1 = Student('bob',89,20)
stu2 = Student('bill',72,20)
students = [stu1,stu2]

cla = Clazz('一年级', '一班', students)

