# -*- coding: utf-8 -*-

import re

# ------------ 1.3.15 杂项 ------------

m = re.match('\bblow', 'blow')    # backspace、no match
if m: print(m.group())

#\b 表示 ASCII 字符的退格符，但是\b 同时也是一个正则表达式的特殊符号，表示匹配一个单词的边界。对于正则表达式编译器而言，若它把两个\b 视为字符串内容而
# 不是单个退格符，就需要在字符串中再使用一个反斜线转义反斜线，就像这样：\\b
# blow
m = re.match('\\bblow', 'blow')    # escaped\，now it works
if m: print(m.group())

# blow
m = re.match(r'\bblow', 'blow')    # use raw string instead
if m: print(m.group())