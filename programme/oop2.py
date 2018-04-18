#coding=utf-8
#description：访问限制
_author_ = 'Kai,Chen'
_time_ = '2018/4/18'


class Student(object):

    def __init__(self, name, grade):
        if not isinstance(grade,(int,float)):
            raise TypeError('grade 类型错误')
        self.__name = name
        self.__grade = grade

    def print_grade(self):
        print(self.__name,self.__grade)

    def get_name(self):
        return self.__name

stu1 = Student('张三',20)
print(stu1.get_name())


