#coding=utf-8
import math

#abs()求绝对值
print(abs(-1.15))
print(abs(-3e10))

#all() 是否存在可迭代元素，存在0、''、None返回False（空的list返回True）
list1=[]
print(all(list1))
list1=['dog','','tigger']
print(all(list1))
list1=[0,'cat','tigger']
print(all(list1))
list1=[None,'cat','tigger']
print(all(list1))

#any()如果当iterable所有的值都是0、''或False时，那么结果为False,如果所有元素中有一个值非0、''或False，那么结果就为True
list1=[]
print(any(list1))
list1=['dog','','tigger']
print(any(list1))
list1=[0,'cat','tigger']
print(any(list1))
list1=[None,'cat','tigger']
print(any(list1))

#ascii()
print(ascii('a'))

#bin()
print(bin(11))

#bool()
print(bool(0))
print(bool(1))
print(bool('22'))

#bytearray()存在字符串时，必须制定编码格式
print(bytearray())
print(bytearray(1))
print(bytearray([1,2,3]))
print(bytearray('中国','utf-8'))

print(dir())

#divmod()把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
print(divmod(5,2))

#enumerate()将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
list2 = ['dog','cat','lion']
print(list(enumerate(list2)))
for i,e in enumerate(list2):
    print(i,e)

#file()用于创建一个 file 对象，它有一个别名叫 open()
# f = open('E:\python_workspace\demo\py_01\function\uuid_test.py','r')
# print(f.read())

#filter() 用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
def is_odd(n):
    return n%2 == 1


list3 = filter(is_odd,range(10))
for e in list3:
    print(e)

#format()
print("{1} {0}".format("hello","world"))

#hex() 10进制转成16进制(字符串)
print(hex(10))

#id()获取对象内存地址
obj1 = 'aaaa'
print(id(obj1))

#pow() x的y次方
print(math.pow(2,3))


#raw_input()
# a = input("input:")
# print(type(a))

#reverse()
list5 = [1,2,3,4,5]
list5.reverse()
print(list5)

#round()四舍五入
print(round(80.23456, 2))