#coding=utf-8
#description：
_author_ = 'Kai,Chen'
_time_ = '2018/4/25'

from multiprocessing import Process
import os

print("process (%s) start ...." % os.getppid())

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')