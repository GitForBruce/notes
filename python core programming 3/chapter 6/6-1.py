# -*- coding: utf-8 -*-

import os
from random import randrange as rand
import builtins
from pymysql import err

if isinstance(builtins, dict) and 'raw_input' in builtins:
    scanf = raw_input
elif hasattr(builtins, 'raw_input'):
    scanf = raw_input
else:
    scanf = input

COLSIZ = 10
FIELDS = ('login', 'userid', 'projid')
RDBMSs = {'s': 'sqlite', 'm': 'mysql', 'g': 'gadfly'}
DBHOST = 'localhost'
DBPORT = 3308
DBNAME = 'test'
DBUSER = 'root'
DBPASSWORD = 'root1234'
DB_EXC = None
NAMELEN = 16

'''
lambda:
    1) 只是一个表达式，函数体比 def 简单很多；
    2）主体是一个表达式，不是一个代码块。仅能在 lambda 表达式中封装有限的逻辑进去；
    3）拥有自己的命名空间，且不能访问自有参数列表以外或全局命名空间里的参数；
    4）只能写一行，不等同于C/C++的内联函数（C的目的是调用小函数时不占用内存从而增加运行效率）
    5）语法：lambda [arg1 [,arg2,.....argn]]:expression
'''
tformat = lambda s: str(s).title().ljust(COLSIZ)
cformat = lambda s: s.upper().ljust(COLSIZ)

def setup():
    return RDBMSs[input('''
    Choose a database system:
    (M)ySQL
    (G)adfly
    (S)QLite
    Enter choice: ''').strip().lower()[0]]

def connect(db):
    global DB_EXC
    dbDir = '%s_%s' % (db, DBNAME)
    if db == 'sqlite':
        try:
            import sqlite3
        except ImportError:
            try:
                from pysqlite2 import dbapi2 as sqlite3
            except ImportError:
                return None

        DB_EXC = sqlite3
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn = sqlite3.connect(os.path.join(dbDir, DBNAME))

    elif db == 'mysql':
        try:
            import pymysql
            # import _mysql_exceptions as DB_EXC   # Python 3 无此函数
        except ImportError:
            return None

        try:
            cxn = pymysql.connect(host=DBHOST, port=DBPORT,user=DBUSER, password = DBPASSWORD)
        except ConnectionError:
            return None

        '''查看数据库，检查是否有 test 库，有则直接连接，没有则创建库'''
        cur = cxn.cursor()
        cur.execute("show databases;")
        databases = str(cur.fetchall())
        # cur.close()

        strdbname = "'" + DBNAME + "'"
        if not strdbname in databases:
            cxn.query('CREATE DATABASE %s' % DBNAME)
            cxn.commit()
            cxn.close()

        try:
            cxn = pymysql.connect(host=DBHOST, port=DBPORT, user=DBUSER, password=DBPASSWORD, db=DBNAME)
        except ConnectionError:
            return None

    elif db == 'gadfly':
        try:
            from gadfly import gadfly
            DB_EXC = gadfly
        except ImportError:
            return None

        try:
            cxn = gadfly(DBNAME, dbDir)
        except IOError:
            cxn = gadfly()
        if not os.path.isdir(dbDir):
            os.mkdir(dbDir)
        cxn.startup(DBNAME, dbDir)
    else:
            return None
    return cxn

def create(cur):
    try:
        cur.execute('''
          CREATE TABLE users (
            login VARCHAR(%d),
            userid INTEGER,
            projid INTEGER)
            ''' % NAMELEN)
    except Exception as e:
        print(e)
        drop(cur)
        create(cur)

drop = lambda cur: cur.execute('DROP TABLE users')
NAMES = (
 ('aaron', 8312), ('angela', 7603), ('dave', 7306),
 ('davina',7902), ('elliot', 7911), ('ernie', 7410),
 ('jess', 7912), ('jim', 7512), ('larry', 7311),
 ('leslie', 7808), ('melissa', 8602), ('pat', 7711),
 ('serena', 7003), ('stan', 7607), ('faye', 6812),
 ('amy', 7209), ('mona', 7404), ('jennifer', 7608),
)

'''
一个带有 yield 的函数就是一个 generator，它和普通函数不同，生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。

看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力，比起用类的实例保存状态来计算下一个 next() 的值，不仅代码简洁，而且执行流程异常清晰。
'''
def randName():
    pick = set(NAMES)
    while pick:
        yield pick.pop()

def insert(cur, db):
    if db == 'sqlite':
        cur.executemany("INSERT INTO users VALUES(?, ?, ?)",
        [(who, uid, rand(1,5)) for who, uid in randName()])
    elif db == 'gadfly':
        for who, uid in randName():
            cur.execute("INSERT INTO users VALUES(?, ?, ?)",
            (who, uid, rand(1,5)))
    elif db == 'mysql':
            cur.executemany("INSERT INTO users VALUES(%s, %s, %s)",
            [(who, uid, rand(1,5)) for who, uid in randName()])

getRC = lambda cur: cur.rowcount if hasattr(cur, 'rowcount') else -1

def update(cur):
    fr = rand(1,5)
    to = rand(1,5)
    cur.execute("UPDATE users SET projid=%d WHERE projid=%d" % (to, fr))
    return fr, to, getRC(cur)


def delete(cur):
    rm = rand(1, 5)
    cur.execute('DELETE FROM users WHERE projid=%d' % rm)
    return rm, getRC(cur)


def dbDump(cur):
    cur.execute('SELECT * FROM users')
    print('\n%s' % ''.join(map(cformat, FIELDS)))
    for data in cur.fetchall():
        print(''.join(map(tformat, data)))

def main():
    db = setup()
    print('*** Connect to %r database' % db)
    cxn = connect(db)

    if not cxn:
        print('ERROR: %r not supported or unreachable, exiting' % db)
        return
    cur = cxn.cursor()

    print('\n*** Create users table (drop old one if appl.)')
    create(cur)
    print('\n*** Insert names into table')
    insert(cur, db)
    dbDump(cur)

    print('\n*** Move users to a random group')
    fr, to, num = update(cur)
    print('\t(%d users moved) from (%d) to (%d)' % (num, fr, to))
    dbDump(cur)

    print('\n*** Randomly delete group')
    rm, num = delete(cur)
    print('\t(group #%d; %d users removed)' % (rm, num))
    dbDump(cur)

    print('\n*** Drop users table')
    drop(cur)
    print('\n*** Close cxns')

    cur.close()
    cxn.commit()
    cxn.close()


if __name__ == '__main__':
    main()

