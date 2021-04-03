# -*- coding: utf-8 -*-

import re

# # ------------ 1.3.6 匹配多个字符串 ------------
# 返回 bat
bt = 'bet|bat|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())

# 返回 bit
m = re.search(bt, 'He bit me!')
if m is not None:
    print(m.group())