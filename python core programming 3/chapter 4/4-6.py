# -*- coding: utf-8 -*-
"""
threading 模块
方式三： 派生 Thread 的子类，并创建子类的实例


"""

import threading
from time import sleep, ctime

loops = [4, 2]

class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def run(self):
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
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in range(nloops):     # start all threads
        threads[i].start()

    for i in range(nloops):     # wait for completion
        threads[i].join()

    print('all done at:', ctime())

if __name__ == '__main__':
    main()