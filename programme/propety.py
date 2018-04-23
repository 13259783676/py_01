#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/23'

#使用@property
class Student(object):


    def get_grade(self):
        return self.grade

    def set_grade(self,value):
        if not isinstance(value,int):
            raise ValueError('参数错误')
        if value > 100 or value <0:
            raise ValueError('参数错误')
        self.grade = value

stu = Student()
stu.set_grade(50)
print(stu.get_grade())