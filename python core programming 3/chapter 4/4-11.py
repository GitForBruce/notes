# -*- coding: utf-8 -*-

from atexit import register
from random import randrange
from threading import BoundedSemaphore, Lock, Thread
from time import sleep, ctime

'''
starting at: Thu Apr  8 14:38:22 2021
THE CANDY MACHINE (full with 5 bars)
Buying candy ...
OK
Refilling candy ...
OK
Refilling candy ...
full, skipping
Buying candy ...
OK
Buying candy ...
OK
Refilling candy ...
OK
Refilling candy ...
OK
Buying candy ...
OK
Buying candy ...
OK
all DONE at: Thu Apr  8 14:38:30 2021
'''
lock = Lock()
MAX = 5
candytray = BoundedSemaphore(MAX)

def refill():
    lock.acquire()
    print("Refilling candy ...")
    try:
        candytray.release()             # 计数器+1
    except ValueError:                  # 满了，报异常
        print("full, skipping")
    else:
        print("OK")
    lock.release()

def buy():
    lock.acquire()
    print("Buying candy ...")
    if candytray.acquire(False):        # 计数器-1
        print('OK')
    else:
        print('empty, skipping')
    lock.release()

def producer(loops):
    for i in range(loops):
        refill()
        sleep(randrange(3))

def consumer(loops):
    for i in range(loops):
        buy()
        sleep(randrange(3))

def _main():
    print('starting at:', ctime())
    nloops = randrange(2,7)
    print('THE CANDY MACHINE (full with %d bars)' % MAX)
    Thread(target=consumer, args=(randrange(nloops, nloops+MAX+2),)).start()
    Thread(target=producer, args=(nloops,)).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()