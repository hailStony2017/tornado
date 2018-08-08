#!/usr/bin/env Python
# coding=utf-8
"""
the url structure of website
"""
# from importlib import reload
#
# import sys     #utf-8，兼容汉字
# reload(sys)
# sys.setdefaultencoding("utf-8")

from handlers.index import IndexHandler    #假设已经有了
from handlers.user import UserHandler

url = [
    (r'/', IndexHandler),
    (r'/user', UserHandler)
]

