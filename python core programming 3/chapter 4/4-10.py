# -*- coding: utf-8 -*-

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
    loop()函数首先保存当前执行它的线程名，然后获取锁，以便使添加该线程名到 remaining集合以及指明启动线程的输出操作是原子的（没有其他线程可以进入临界区）。
    释放锁之后，这个线程按照预先指定的随机秒数执行睡眠操作，然后重新获得锁，进行最终输出，最后释放锁。
    临界区：操作 remaining 集合
    """
    myname = currentThread().name
    lock.acquire()
    remaining.add(myname)
    print('[%s] Started %s' % (ctime(), myname))
    lock.release()
    sleep(nsec)
    lock.acquire()
    remaining.remove(myname)
    print('[%s] Completed %s (%d secs)' % (ctime(), myname, nsec))
    print('     (remaining: %s)' %(remaining or 'None'))
    lock.release()


def _main():
    for pause in loops:
        Thread(target=loop, args=(pause, )).start()

@register
def _atexit():
    print('all DONE at:', ctime())

if __name__ == '__main__':
    # print(list(loops))        # [3, 2, 2, 4]
    _main()
