#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : scraptest.py.py
# @Author: huyn
# @Date  : 2018/3/30
# @Desc  :




from urllib.request import urlopen
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None

    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title  == None:
    print("Title could not be found")
else:
    print(title)