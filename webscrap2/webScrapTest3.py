#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest3.py
# @Author: huyn
# @Date  : 2018/4/9
# @Desc  :


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re,ssl


ssl._create_default_https_context = ssl._create_unverified_context
pages = set()

def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org"+pageUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-view").find("span").find("a").attrs['href'])

    except AttributeError:
        print("页面缺少一些属性！不过不用担心！")

    for link in bsObj.findAll("a",href = re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #当我们遇到了新页面
                newPage = link.attrs['href']
                print("----------------------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)



getLinks("")