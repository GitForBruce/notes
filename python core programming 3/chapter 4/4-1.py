# -*- coding: utf-8 -*-

from time import sleep, ctime

'''
starting at: Thu Apr  8 10:48:13 2021
start loop 0 at: Thu Apr  8 10:48:13 2021
loop 0 done at: Thu Apr  8 10:48:17 2021
start loop 1 at: Thu Apr  8 10:48:17 2021
loop 1 done at: Thu Apr  8 10:48:19 2021
all done at: Thu Apr  8 10:48:19 2021
'''

def loop0():
    print('start loop 0 at:', ctime())
    sleep(4)
    print('loop 0 done at:', ctime())

def loop1():
    print('start loop 1 at:', ctime())
    sleep(2)
    print('loop 1 done at:', ctime())

def main():
    print("starting at:", ctime())
    loop0()
    loop1()
    print("all done at:", ctime())

if __name__ == '__main__':
    main()