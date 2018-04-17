#coding=utf-8

def add_list():
    L = []
    n = 1
    while n < 99:
        L.append(n)
        n = n+2
    return L
list = add_list()
print(list)

L = ['dog', 'cat', 'lion', 'donkey', 'duck']
print(L[0:3])
print(L[:3])
print(L[-1:])


d = {'cat':'10','lion':200,'duck':50}
for key in d:
    print(key)
    print(d[key])

g = (x * x for x in range(10))
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
