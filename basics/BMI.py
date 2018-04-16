#coding=utf-8

h=input('enter high(m)\n')
high=float(h)
w=input('enter weight(kg)\n')
weight=float(w)
if high>5:
    high=high/100
print(high)
bmi=weight/(high*high)
print('bmi:',bmi)
if bmi>32:
    print('过度肥胖')
elif bmi>28:
    print('肥胖')
elif bmi>25:
    print('过重')
elif bmi>18.5:
    print('正常')
else:
    print('过轻')
