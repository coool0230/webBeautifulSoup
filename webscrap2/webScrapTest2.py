#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest2.py
# @Author: huyn
# @Date  : 2018/4/8
# @Desc  :

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    for link in bsObj.findAll("a",href = re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks("")