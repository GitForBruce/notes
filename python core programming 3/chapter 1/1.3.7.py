# -*- coding: utf-8 -*-

import re

# ------------ 1.3.7 匹配任意单个字符串 ------------

anyend = '.end'

# 返回 'bend'
m = re.match(anyend, 'bend.')
if m is not None:    print(m.group())


# 无返回
m = re.match(anyend, 'end.')
if m is not None:    print(m.group())

# 无返回
m = re.match(anyend, '\nend.')
if m is not None:    print(m.group())


# 返回 ' end'
anyend = '.end'
m = re.search(anyend, 'The end.')
if m is not None:    print(m.group())


patt314 = '3.14'
pi_patt = '3\.14'

# 返回 3.14
m = re.match(patt314, '3.14')
if m is not None:    print(m.group())


# 返回 3014
m = re.match(patt314, '3014')
if m is not None:    print(m.group())


# 返回 3.14
m = re.match(pi_patt, '3.14')
if m is not None:    print(m.group())