#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/24'

def foo(s):
    n = int(s)
    assert n!=0,'n is 0'
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

main()