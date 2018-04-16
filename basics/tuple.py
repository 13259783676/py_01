#coding=utf-8

t=('mokey','duck','dog')
print(t)

print(t.__len__())
print(t.__hash__())

s=input('enter age')
s=int(s)
if s>60:
    print('old')
elif s>18:
    print('adult')
else:
    print('child')