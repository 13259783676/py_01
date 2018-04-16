#coding=utf-8

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