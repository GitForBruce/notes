# -*- coding: utf-8 -*-

import re

# 返回 foo
m = re.match('foo', 'foo')
if m is not None:
    print(m.group())
else:
    print("Not match")


# 返回 Not match
m = re.match('foo', 'seafood')
if m is not None:
    print(m.group())
else:
    print("Not match")


# 返回 foo
m = re.match('foo', 'food is good')
if m is not None:
    print(m.group())
else:
    print("Not match")