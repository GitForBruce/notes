# -*- coding: utf-8 -*-

import re

# ------------ 1.3.5 search（查找）------------
# 返回 foo
m = re.search('foo', 'seafood')
if m is not None:
    print(m.group())
else:
    print("Not match")