# -*- coding: utf-8 -*-

import _thread
from time import sleep, ctime

loops = [4, 2]

'''
thread 模块：

starting at: Thu Apr  8 10:50:45 2021
start loop 1start loop at: 0  at: Thu Apr  8 10:50:45 2021
Thu Apr  8 10:50:45 2021
loop 1 done at: Thu Apr  8 10:50:47 2021
loop 0 done at: Thu Apr  8 10:50:49 2021
all done at: Thu Apr  8 10:50:49 2021
'''

def loop(nloop, nsec, lock):
    print("start loop", nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()

def main():
    print('starting at:', ctime())
    locks = []
    nloops = len(loops)

    for i in range(nloops):                 # 上锁
        lock = _thread.allocate_lock()      # 获得锁对象
        lock.acquire()                      # 取得锁，即上锁
        locks.append(lock)

    for i in range(nloops):                 # 派生线程，每个线程都会调用 loop() 函数，并传参
        _thread.start_new_thread(loop,
                                 (i, loops[i], locks[i]))

    for i in range(nloops):                 # 等待，锁释放时会执行
        while locks[i].locked():    pass

    print('all done at:', ctime())

if __name__ == '__main__':
    main()
