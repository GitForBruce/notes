# -*- coding: utf-8 -*-

import re


# ------------ 1.3.10 匹配字符串的起始和结尾以及单词边界 ------------
# 输出 The
m = re.search('^The', 'The end.')
if m is not None: print(m.group())


# 无输出
m = re.search('^The', 'end. The ')
if m is not None: print(m.group())


# 输出 the
m = re.search(r'\bthe', 'bite the dog')
if m is not None: print(m.group())


# 无输出
m = re.search(r'\bthe', 'bitethe dog')
if m is not None: print(m.group())


# 输出 the
m = re.search(r'\Bthe', 'bitethe dog')
if m is not None: print(m.group())