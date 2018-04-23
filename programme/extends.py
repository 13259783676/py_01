# coding=utf-8
# description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/23'


# 继承
class Animal(object):
    pass


class Mammal(Animal):
    pass


class cat(Mammal):
    pass


class dog(Mammal):
    pass


class Bird(object):
    pass


class Parrot(Bird):
    pass


class Ostrich(Bird,Mammal):
    pass
