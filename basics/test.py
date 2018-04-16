# coding=utf-8


name = 'I\'m \"ok\"!'
print('1\n'
      '2\n'
      '3\n')

print('''line1
line2
line3''')

print(r'''hello,
world''')

print(not False)

age=18
if age >= 18:
    print('adult')
else:
    print('teen')

x=10
x=x+2
print(x)

print(10/3)
print(10//3)
print(10%3)

print(ord('中'))
print(chr(20013))

print('中国'.encode('utf-8'))
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode())

list=['duck','lion','monky']
list[0]='tiger'
print(list)
print(list[-1])

print(len(list))

list.pop(0)
print(list)

list.append('donkey')
print(list)

list.insert(1,'dog')
print(list)

list=['duck','lion','monky']
list.pop(1)
print(list)

