# -*- coding: utf-8 -*-

import re


# ------------ 1.3.9 重复、特殊字符以及分组 ------------
# 返回 nobody123@xxx.yyy.com
patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt, 'nobody123@xxx.yyy.com').group())


# 不能匹配诸如 xxx-yyy.com 的域名或者使用非单词\W 字符组成的域名
# 返回 nobody123@xxx.yyy.zzz.com
patt = '\w+@(\w+\.)*\w+\.com'
print(re.match(patt, 'nobody123@xxx.yyy.zzz.com').group())


# 输出 abc-123
m = re.match('\w{3}-\d{3}', 'abc-123')
if m is not None: print(m.group())


# group()：通常用于以普通方式显示所有的匹配部分，但也能用于获取各个匹配的子组
# group(1)：子组1
# groups()：来获取一个包含所有匹配子字符串的元组
m = re.match('(\w{3})-(\d{3})', 'abc-123')
# 输出 ('abc', '123')
if m is not None: print(m.groups())


# 输出 abc-123, abc, 123
print(m.group(), m.group(1), m.group(2))


# 输出 ab
m = re.match('ab', 'ab')
print(m.group())
# 输出  ()， 没有子组
print(m.groups())


#输出 ('ab',) ab ab
m = re.match('(ab)', 'ab')
print(m.groups(), m.group(), m.group(1))


# ============== TBD ===============
#输出 ('a', 'b') ab a b
m = re.match('(a)(b)', 'ab')
print(m.groups(), m.group(), m.group(1), m.group(2))


# #输出 ('ab', 'b') ab ab b
m = re.match('(a(b))', 'ab')
print(m.groups(), m.group(), m.group(1), m.group(2))