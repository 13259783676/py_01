#coding=utf-8

def my_abs(n):
    if not isinstance(n,(int,float)):
        raise TypeError('类型错误')
    if n >= 0:
        return n
    else:
        return -n

# num = input('input:')
print(my_abs(-99))

def none_f():
    pass

print(none_f())

def muti_return(x,y,z):
    return x+1,y+1,z+1

print(muti_return(1,2,3))

def default_params(x,y=2):
    if x <= 0:
        return -x,y
    else:
        pass

print(default_params(-4,3))
print(default_params(-4))

#平方和
def pow_sum(*numbers):
    sum = 0
    for num in numbers:
        sum = sum + num*num
    return sum

numbers = range(10)
print(pow_sum(*numbers))

def key_params(name,age,**other):
    print('name:',name,'age:',age,'other:',other)

key_params('lion',20)
key_params('lion',20,addr='xian',sex='男')


def recursion(n):
    if n == 1:
        return 1
    return n * recursion(n - 1)
print(recursion(10))


