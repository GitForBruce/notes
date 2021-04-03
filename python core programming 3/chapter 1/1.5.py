# -*- coding: utf-8 -*-

import re


# ------------ 1.5 更长的正则表达式示例 ------------
'''
Thu Sep 20 14:37:28 1990::jduned@bijwaqlxjchs.edu::6538126486686510689-6-12
Fri Jun 11 23:57:25 1971::hjouy@ppqnjsfycx.edu::455038458509319271-5-10
Thu Dec  5 01:08:21 1985::afsxrsa@porlbsgbqrk.org::5025641017502124524-7-11
Fri Oct 26 10:28:13 1973::optfkgm@rifwspuq.com::1204504938490097034-7-8
Thu Aug 15 00:51:14 1991::adgw@onztperbhuw.net::6821886742598343578-4-11
Wed Dec 25 18:01:01 1974::sryjlo@mbfamsuxvks.edu::1571976615177998717-6-11
Sat Feb  4 11:22:50 1995::nklxcmz@ltgxyillr.net::7918681703698180329-7-9
Tue Oct 13 08:40:46 1981::kigewc@rhycggn.edu::3717816467236620187-6-7
'''
from random import randrange, choice
from string import ascii_lowercase as lc
from sys import maxsize
from time import ctime

tlds = ('com', 'edu', 'net', 'org', 'gov')

for i in range(randrange(5,11)):
    dtint = randrange(maxsize)
    dtstr = ctime(dtint/10000000000)
    llen =  randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen))
    dlen =  randrange(llen, 13)
    dom =   ''.join(choice(lc) for j in range(dlen))
    print('%s::%s@%s.%s::%d-%d-%d' % (dtstr, login, dom, choice(tlds), dtint, llen, dlen))

'''
Thu
Thu
('Thu',)
'''
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m = re.match(patt, data)
print(m.group())
print(m.group(1))
print(m.groups())

'''
Thu
Thu
'''
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(\w{3})'
m = re.match(patt, data)
if m is not None: print(m.group())
print(m.group(1))


'''
Thu
u (当我们访问子组 1 时，出现字母“u”的原因是子组 1 持续被下一个字符替换。换句话说，m.group(1)以字母“T”作为开始，然后变为“h”，最终被替换为“u”。这些是单个字母数字
   字符的三个独立（并且重叠）分组，与一个包含三个连续字母数字字符的单独分组相反。)
'''
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(\w){3}'
m = re.match(patt, data)
if m is not None: print(m.group())
print(m.group(1))


# --------- 贪婪匹配 --------
# 输出 1171590364-67-8
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '\d+-\d+-\d+'
print( re.search(patt, data).group())


# 输出 Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '.+\d+-\d+-\d+'
print( re.search(patt, data).group())


# 输出 4-6-8 => 贪婪匹配
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '.+(\d+-\d+-\d+)'
print( re.search(patt, data).group(1))


# 输出 1171590364-6-8 => 加上? 改成 非贪婪匹配
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '.+?(\d+-\d+-\d+)'
print( re.search(patt, data).group(1))


# # 输出 1171590364-6-8 => 加上? 改成 非贪婪匹配
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '-(\d+)'
print( re.search(patt, data).group(1))
