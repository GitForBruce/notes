# -*- coding: utf-8 -*-

import re

# ------------ 1.3.13 在限定模式上使用 split()分隔字符串 ------------
# ['str1', 'str2', 'str3']
print(re.split(':', 'str1:str2:str3'))

'''
['Mountain View', 'CA', '94040']
['Sunnyvale', 'CA']
['Los Altos', '94023']
['Cupertino', '95014']
['Palo Alto', 'CA']
'''
DATA = (
 'Mountain View, CA 94040',
 'Sunnyvale, CA',
 'Ls Altos, 94023',
 'Cupertino 95014',
 'Palo Alto CA',
)

for datum in DATA:
    # ',' 分割后，再按照 空格+5个数字，或大写的2个字母
    print(re.split(', |(?= (?:\d{5}|[A-Z]{2})) ', datum))