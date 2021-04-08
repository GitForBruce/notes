# -*- coding: utf-8 -*-

from __future__ import with_statement       # 必须放在文件开头位置
from atexit import register
from random import randrange
from time import ctime, sleep
from threading import Thread, Lock, currentThread

'''
[Thu Apr  8 11:32:41 2021] Started Thread-1
[Thu Apr  8 11:32:41 2021] Started Thread-2
[Thu Apr  8 11:32:41 2021] Started Thread-3
[Thu Apr  8 11:32:41 2021] Started Thread-4
[Thu Apr  8 11:32:43 2021] Completed Thread-2 (2 secs)
     (remaining: Thread-4, Thread-1, Thread-3)
[Thu Apr  8 11:32:43 2021] Completed Thread-1 (2 secs)
     (remaining: Thread-4, Thread-3)
[Thu Apr  8 11:32:45 2021] Completed Thread-4 (4 secs)
     (remaining: Thread-3)
[Thu Apr  8 11:32:45 2021] Completed Thread-3 (4 secs)
     (remaining: None)
all DONE at: Thu Apr  8 11:32:45 2021
'''

class CleanOutputSet(set):
    def __str__(self):
        return ', '.join(x for x in self)

lock = Lock()                                               # 锁
loops = (randrange(2,5) for x in range(randrange(3,7)))     # 语句意思：生成3-6个（个数由randrange(3,7)控制）随机数，随机数的值为2-4（由randrange(2,5)控制）
                                                            # 随机数量的线程（3～ 6 个线程），每个线程暂停或睡眠 2～4 秒
remaining = CleanOutputSet()                                # 上面提到的修改后的集合类的实例

def loop(nsec):
    """
    精简写法： 使用 with 语句，，此时每个对象的上下文管理器负责在进入该套件之前调用 acquire()并在完成执行之后调用 release()。
    :param nsec:
    :return:
    """
    myname = currentThread().name

    with lock:
        remaining.add(myname)
        print('[%s] Started %s' % (ctime(), myname))
    sleep(nsec)

    with lock:
        remaining.remove(myname)
        print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
        print('     (remaining: %s)' % (remaining or 'None'))

def _main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    _main()
