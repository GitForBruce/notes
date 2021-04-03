# -*- coding: utf-8 -*-

import _thread
from time import sleep, ctime

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
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)                            # 不加 sleep，则主线程执行 print all done，子线程 loop0, loop1 直接退出
    print("all done at:", ctime())

if __name__ == '__main__':
    main()