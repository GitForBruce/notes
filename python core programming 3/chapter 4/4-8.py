# -*- coding:utf-8 -*-

from myThread import MyThread
from time import sleep, ctime

'''
*** single thread ***
starting fib at: Thu Apr  8 10:58:43 2021
233
fib finished at: Thu Apr  8 10:58:46 2021
starting fac at: Thu Apr  8 10:58:46 2021
479001600
fac finished at: Thu Apr  8 10:58:47 2021
starting sum at: Thu Apr  8 10:58:47 2021
78
sum finished at: Thu Apr  8 10:58:48 2021
*** multiple threads ***
starting fib at: Thu Apr  8 10:58:48 2021
starting fac at: Thu Apr  8 10:58:48 2021
starting sum at: Thu Apr  8 10:58:48 2021
fac finished at: Thu Apr  8 10:58:49 2021
sum finished at: Thu Apr  8 10:58:49 2021
fib finished at: Thu Apr  8 10:58:50 2021
233
479001600
78
all done
'''

def fib(x):
    sleep(0.005)
    if x < 2: return 1
    return fib(x-2) + fib(x-1)

def fac(x):
    sleep(0.1)
    if x < 2: return 1
    return x * fac(x-1)

def sum(x):
    sleep(0.1)
    if x < 2: return 1
    return x + sum(x-1)

funcs = [fib, fac, sum]
n = 12

def main():
    nfuncs = len(funcs)
    print("*** single thread ***")
    for i in range(nfuncs):
        print("starting", funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print("*** multiple threads ***")
    threads = []

    for i in range(nfuncs):
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in range(nfuncs):
        threads[i].start()

    for i in range(nfuncs):
        threads[i].join()
        print(threads[i].getresult())


    print("all done")

if __name__ == '__main__':
    main()