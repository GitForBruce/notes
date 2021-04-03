# -*- coding: utf-8 -*-

import re

# ------------ 1.4 一些正则表达式示例 ------------
'''
['root', 'pts/0', '2021-03-31 15:41 (192.168.2.132)\n']
['root', 'pts/2', '2021-04-01 17:24 (192.168.2.146)\n']
['root', 'pts/4', '2021-03-19 16:16 (192.168.2.140)\n']
['root', 'pts/6', '2021-03-19 17:27 (192.168.2.135)\n']
'''
f = open("c1_whodata.txt", 'r')
for eachLine in f:
    print(re.split(r'\s\s+', eachLine))         # 匹配2个空格，用来分割
f.close()

'''
['root', 'pts/0', '2021-03-31 15:41 (192.168.2.132)']
['root', 'pts/2', '2021-04-01 17:24 (192.168.2.146)']
['root', 'pts/4', '2021-03-19 16:16 (192.168.2.140)']
['root', 'pts/6', '2021-03-19 17:27 (192.168.2.135)']
'''
with open('c1_whodata.txt', 'r') as f:
    for eachLine in f:
        print(re.split(r'\s\s+|\t', eachLine.strip()))

'''
['']
['映像名称', 'PID 会话名', '会话#', '内存使用']
['========================= ======== ================ =========== ============']
['System Idle Process', '0 Services', '0', '24 K']
['System', '4 Services', '0', '392 K']
['smss.exe', '372 Services', '0', '1,456 K']
'''
f = open("c1_tasklist.txt", 'r')
for eachLine in f:
    print(re.split(r'\s\s+|\t', eachLine.strip()))         # 首先用 strip 去掉 \n，再匹配2个空格或tab，用来分割
f.close()