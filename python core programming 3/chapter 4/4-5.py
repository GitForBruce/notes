# -*- coding: utf-8 -*-

"""
threading 模块
方式二： 创建 Thread 的实例，传给它一个可调用的类实例

Notes:
当创建新线程时，Thread 类的代码将调用 ThreadFunc 对象，此时会调用__call__()这个特殊方法。
由于我们已经有了要用到的参数，这里就不需要再将其传递给 Thread()的构造函数了，直接调用即可。
"""

import threading
from time import sleep, ctime

loops = [4, 2]

class ThreadFunc(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print("start loop", nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())

def main():
    print('starting at:', ctime())
    threads = []
    nloops = len(loops)

    for i in range(nloops):     # create all threads
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in range(nloops):     # start all threads
        threads[i].start()

    for i in range(nloops):     # wait for completion
        threads[i].join()

    print('all done at:', ctime())

if __name__ == '__main__':
    main()