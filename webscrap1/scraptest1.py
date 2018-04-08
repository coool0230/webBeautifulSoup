#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : scraptest1.py
# @Author: huyn
# @Date  : 2018/4/2
# @Desc  :


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
# html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")

# nameList = bsObj.findAll("span",{"class":"green"})
# print(nameList)
# for name in nameList:15639170199
#     print(name.get_text())
# allText = bsObj.findAll(id="text")
# allText = bsObj.findAll("",{"id":"text"})
# print(allText[0].get_text())

# for child in bsObj.find("table",{"id":"giftList"}).descendants:
#     print(child)
#
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_sibling:
#     print(sibling)

# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

# images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
images = attrs["src"]
for image in images:
    print(image["src"])