# -*- coding: utf-8 -*-

import re


# ------------ 1.3.14 扩展符号 ------------
#['yes', 'Yes', 'YES']
print(re.findall(r'(?i)yes', 'yes? Yes. YES!!'))

#['The', 'through', 'this']
print( re.findall(r'(?i)th\w+', 'The quickest way is through this tunnel.'))

#['This line is the first', 'that line']
print(re.findall(r'(?im)(^th[\w ]+)', """
This line is the first,
another line,
that line, it's the best
"""
))


#['the second line', 'the third line']
print(re.findall(r'th.+', '''
The first line
the second line
the third line
'''
))


# ('800', '555', '1212')
print(re.search(r'''(?x)
(\d{3})     # 区号
[ ]         # 空白符
(\d{3})     # 前缀
-           # 横线
(\d{4})     # 终点数字
''', '800 555-1212').groups())

#('800', '555', '1212')
print(re.search(r"\((\d{3})\) (\d{3})-(\d{4})", '(800) 555-1212').groups())
print(re.match('\((\d{3})\) (\d{3})-(\d{4})', '(800) 555-1212').groups())

#['google.com', 'google.com', 'google.com']
print(re.findall(r'http://(?:\w+\.)*(\w+\.com)', 'http://google.com http://www.google.com http://code.google.com'))

# {'areacode': '800', 'prefix': '555'}
print(re.search(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(800) 555-1212').groupdict())

# (800) 555-xxxx
print(re.sub(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?:\d{4})', '(\g<areacode>) \g<prefix>-xxxx' ,'(800) 555-1212'))

# True
print(bool(re.match(r'\((?P<areacode>\d{3})\) (?P<prefix>\d{3})-(?P<number>\d{4}) (?P=areacode)-(?P=prefix)-(?P=number) 1(?P=areacode)(?P=prefix)(?P=number)',
                    '(800) 555-1212 800-555-1212 18005551212')))


# True
print(bool(re.match(r'''(?x)

# match (800) 555-1212, save areacode, prefix, no.
\((?P<areacode>\d{3})\)[ ](?P<prefix>\d{3})-(?P<number>\d{4})

# space
[ ]

# match 800-555-1212
(?P=areacode)-(?P=prefix)-(?P=number)

# space
[ ]

# match 18005551212
1(?P=areacode)(?P=prefix)(?P=number)

 ''', '(800) 555-1212 800-555-1212 18005551212')))

#['Guido', 'Just']
print(
re.findall(r'\w+(?= van Rossum)',
           '''
            Guido van Rossum
            Tim Peters
            Alex Martelli
            Just van Rossum
            Raymond Hettinger
           '''))

# ['sales']
print(
 re.findall(r'(?m)^\s+(?!noreply|postmaster)(\w+)',
'''
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com
'''))

# ['sales', 'eng', 'admin']
print(
 re.findall(r'(?m)\s+(?!noreply|postmaster)(\w+)',
'''
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com
'''))

# ['sales@aw.com', 'eng@aw.com', 'admin@aw.com']
print(
['%s@aw.com' % e.group(1) for e in \
re.finditer(r'(?m)\s+(?!noreply|postmaster)(\w+)',
'''
sales@phptr.com
postmaster@phptr.com
eng@phptr.com
noreply@phptr.com
admin@phptr.com
''')]
)

# True, True, False
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xy')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'yx')))
print(bool(re.search(r'(?:(x)|y)(?(1)y|x)', 'xx')))