# -*- coding:utf-8 -*-

from atexit import register
from re import compile
from threading import Thread
from time import ctime
from urllib.request import urlopen as uopen, Request

'''
At Thu Apr  8 11:01:34 2021 on Amazon...
- 'Python Web Development with Diango' ranked 1,882,764
- 'Core Python Programming' ranked 756,966
- 'Python Fundamentals' ranked 7,822,708
all done at: Thu Apr  8 11:01:40 2021
'''

REGEX = compile('#([\d,]+) in Books ')      # 用于匹配 Amazon 商品页中图书排名的模式
AMZN = 'https://www.amazon.com/dp/'
ISBNs = {
    '0132269937' : 'Core Python Programming',
    '0132356139' : 'Python Web Development with Diango',
    '0137143419' : 'Python Fundamentals'
}

def getrangking(isbn):
    """
    目的：使用正则表达式来拉取和返回当前的排名
    步骤：根据 ISBN，创建与 Amazon 服务器通信的最终 URL，然后调用 urllib.request.urlopen 来打开这个地址.

    :param isbn: isbn 代码
    :return: 排名
    """
    # page = uopen('%s%s' %(AMAZN, isbn))
    url = '%s%s' % (AMZN, isbn)
    req = Request(url, headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    page = uopen(req)
    data = page.read()
    page.close()
    return REGEX.findall(data.decode())[0]

def _showranking(isbn):
    """
    目的：向用户显示结果

    Notes：函数名最前面的单下划线表示这是一个特殊函数，只能被本模块的代码使用，不能被其他使用本文件作为库或者工具模块的应用导入。

    :param isbn:
    :return:
    """
    print('- %r ranked %s' %(ISBNs[isbn], getrangking(isbn)))

def main():
    print('At', ctime(), 'on Amazon...')
    for isbn in ISBNs:
        Thread(target=_showranking, args=(isbn,)).start()

@register           # 告知脚本何时结束
def _atexit():
    """
    atexit.register() 函数（这里使用了装饰器的方式）会在 Python 解释器中注册一个退出函数，也就是说，它会在脚本退出之前请求调用这个特殊函数 。
    （如果不使用装饰器的方式，也可以直接使用 register(_atexit())
    """
    print('all done at:', ctime())

if __name__ == '__main__':
    main()