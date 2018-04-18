# coding=utf-8
# description：继承和多态
_author_ = 'Kai,Chen'
_time_ = '2018/4/18'


# 继承
class Animals(object):
    def run(self):
        print(self.name, 'running')


class Dog(Animals):
    def __init__(self, name):
        self.name = name


class Cat(Animals):
    def __init__(self, name):
        self.name = name


class Fish(Animals):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name,'can`t running')
        self.swimming()

    def swimming(self):
        print(self.name,'swimming')


dog1 = Dog('dog1')
dog1.run()

cat1 = Cat('cat1')
cat1.run()

fish1 = Fish('fish1')
fish1.run()

print(isinstance(dog1,Animals))
print(isinstance(dog1,Dog))
print(isinstance(dog1,object))
print(isinstance(dog1,Cat))