# -*- coding: utf-8 -*-

import re


# ------------ 1.3.11 使用 findall()和 finditer()查找每一次出现的位置 ------------
# 输出 ['car']
print(re.findall('car', 'car'))

# 输出 ['car']
print(re.findall('car', 'scary'))

# 输出 ['car', 'car', 'car']
print(re.findall('car', 'carry the barcardi to the car'))


'''
re.I 使匹配对大小写不敏感
re.L 做本地化识别（locale-aware）匹配
re.M 多行匹配，影响 ^ 和 $
re.S 使 . 匹配包括换行在内的所有字符
re.U 根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X 该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。
'''
s = 'This and that.'
print(re.findall(r'(th\w+) and (th\w+)', s, re.I))

# ('This', 'that')
print(next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).groups())
# This
print(next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).group(1))
# that
print(next(re.finditer(r'(th\w+) and (th\w+)', s, re.I)).group(2))

# [('This', 'that')]
print([g.groups() for g in re.finditer(r'(th\w+) and (th\w+)',s, re.I)])

# ['This', 'that']
print(re.findall(r'(th\w+)', s, re.I))

it = re.finditer(r'(th\w+)', s, re.I)
g = next(it)

# ('This',) This
print(g.groups(), g.group(1))

h = next(it)
# ('that',) that
print(h.groups(), h.group(1))

# ['This', 'that']
print( [g.group(1) for g in re.finditer(r'(th\w+)', s, re.I)])