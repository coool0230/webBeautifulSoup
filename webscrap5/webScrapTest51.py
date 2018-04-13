#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest51.py
# @Author: huyn
# @Date  : 2018/4/13
# @Desc  :


from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html,"html.parser")

imageLocation = bsObj.find("a",{"id":"logo"}).find("img")["src"]
urlretrieve(imageLocation,"logo.jpg")