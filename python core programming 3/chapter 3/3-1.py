# -*- coding: utf-8 -*-

import ftplib
import os
import socket

HOST = '192.168.2.146'
PORT = 5021
USER = "ftpuser"
PASSWD = "ftppassword"
DIRN = 'ptb/download'
FILE = 'PankouAndAlarm_20210421.log'

def main():
    try:
        # # 默认端口连接
        # f = ftplib.FTP(HOST)

        # 自定义端口连接
        f = ftplib.FTP()
        f.connect(HOST, 5021)
    except (socket.error, socket.gaierror) as e:
        print("ERROR: can not reach %s" % HOST)
        return
    print("connected to host %s" % HOST)

    try:
        f.login()
    except ftplib.error_perm:
        print("ERROR: cannot login anonymously")
        # f.quit()
        # return
    # print("*** Logged in as 'anonymous'")

    try:
        f.login(user=USER, passwd=PASSWD)
    except ftplib.error_perm:
        print("ERROR: cannot login with user %s" % USER)
        f.quit()
        return
    print("*** Logged in as '%s'" % USER)

    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print("ERROR: cannot CD to %s" % DIRN)
        f.quit()
        return
    print("*** Changed to %s folder" % DIRN)

    try:
        loc = open(FILE, 'wb')
        # retrbinary(cmd, cb[,bs=8192[, ra]])。与 retrlines()类似，只是这个指令处理二进制文件。回调函数 cb 用于处理每一块（块大小默认为 8KB）下载的数据
        # cmd: RETR
        f.retrbinary('RETR %s' %FILE, loc.write)
    except ftplib.error_perm:
        print("ERROR: cannot read file %s" % FILE)
        os.unlink(FILE)

    else:
        print('*** Downloaded %s to CWD' % FILE)
    loc.close()
    f.quit()
    return

if __name__ == '__main__':
    main()
