#coding=utf-8

#创建类
class Student(object):

    def __init__(self,name,grade):
        if not isinstance(grade,(int,float)):
            raise TypeError('成绩类型错误')
        self.name = name
        self.grade = grade

    def get_grade(self):
        if self.grade >= 90:
            print('A')
        elif self.grade >= 80:
            print('B')
        elif self.grade >= 60:
            print('C')
        else:
            print('D')



stu1 = Student('张三', 20)
stu2 = Student('李四', 80)
stu1.get_grade()
stu2.get_grade()


