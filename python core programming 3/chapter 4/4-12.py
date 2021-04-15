# -*- coding: utf-8 -*-

from random import randint
from time import sleep
import queue
from myThread import MyThread

'''
starting writer at: Thu Apr  8 16:55:34 2021
producing object for Q...
size now 1
starting reader at: Thu Apr  8 16:55:34 2021
consumed object from Q... szie now 0
producing object for Q...
size now 1
producing object for Q...
size now 2
consumed object from Q... szie now 1
writer finished at: Thu Apr  8 16:55:40 2021
consumed object from Q... szie now 0
reader finished at: Thu Apr  8 16:55:49 2021
all DONE
'''

def writeQ(queue):
    print("producing object for Q...")
    queue.put('xxx', 1)
    print("size now", queue.qsize())

def readQ(queue):
    queue.get(1)
    print('consumed object from Q... szie now', queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        writeQ(queue)
        sleep(randint(1,3))     # writer 睡眠的随机秒数通常比 reader 的要短。这是为了阻碍 reader 从空队列中获取对象

def reader(queue, loops):
    for i in range(loops):
        readQ(queue)
        sleep(randint(2,5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def main():
    nloops = randint(2, 5)
    q = queue.Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print("all DONE")

if __name__ == '__main__':
    main()