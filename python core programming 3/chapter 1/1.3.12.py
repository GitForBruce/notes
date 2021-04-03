# -*- coding: utf-8 -*-

import re

# ------------ 1.3.12 使用 sub()和 subn()搜索与替换 ------------

'''
attn: Mr. Smith

Dear Mr. Smith,
'''
print( re.sub('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'))

# ('attn: Mr. Smith\n\nDear Mr. Smith,\n', 2)
print( re.subn('X', 'Mr. Smith', 'attn: X\n\nDear X,\n'))

# XbcdXf
print(re.sub('[ae]', 'X', 'abcdef'))

# ('XbcdXf', 2)
print(re.subn('[ae]', 'X', 'abcdef'))

# 20/2/91
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/91'))

# 20/2/1991
# r 后面的数字 代表获取的数字的位置： 2：取 "20" 并以 1-2 位数字展示， 1：取 "2" 并以 1-2 位数字展示，3：取"1991" 并以 2或 4位数字展示，
print(re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})', r'\2/\1/\3', '2/20/1991'))