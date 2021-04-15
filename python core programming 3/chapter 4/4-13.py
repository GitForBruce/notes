# -*- coding:utf-8 -*-

from re import compile
from concurrent.futures import ThreadPoolExecutor
from time import ctime
from urllib.request import urlopen as uopen, Request

'''
At Thu Apr  8 17:23:07 2021 on Amazon...
- 'Core Python Programming' ranked 819,070
- 'Python Web Development with Diango' ranked 1,903,181
- 'Python Fundamentals' ranked 7,825,966
all DONE at: Thu Apr  8 17:23:14 2021
'''

REGEX = compile('#([\d,]+) in Books ')      # 用于匹配 Amazon 商品页中图书排名的模式
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
    '0132269937' : 'Core Python Programming',
    '0132356139' : 'Python Web Development with Diango',
    '0137143419' : 'Python Fundamentals'
}

def getrangking(isbn):
    url = '%s%s' % (AMZN, isbn)
    req = Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    with uopen(req) as page:
        return REGEX.findall(page.read().decode())[0]

def main():
    print('At', ctime(), 'on Amazon...')
    with ThreadPoolExecutor(3) as executor:
        for isbn, ranking in zip(ISBNs, executor.map(getrangking, ISBNs)):
            print('- %r ranked %s' %(ISBNs[isbn], ranking))
    print('all DONE at:', ctime())

if __name__ == '__main__':
    main()