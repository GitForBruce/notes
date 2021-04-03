# -*- coding: utf-8 -*-

import re

# ------------ 1.3.8 创建字符集 [] ------------

# 返回 'c3po'
m = re.match('[cr][23][dp][o2]', 'c3po')  # 匹配 'c3po'
if m is not None:    print(m.group())

# 返回 'c2do'
m = re.match('[cr][23][dp][o2]', 'c2do')  # 匹配 'c2do'
if m is not None:    print(m.group())

# 无返回
m = re.match('r2d2|c3po', 'c2do')# 不匹配 'c2do'
if m is not None:    print(m.group())

# 返回 r2d2
m = re.match('r2d2|c3po', 'r2d2')# 匹配 'r2d2'
if m is not None:    print(m.group())
