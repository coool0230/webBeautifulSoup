#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest1.py
# @Author: huyn
# @Date  : 2018/4/8
# @Desc  :


from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import datetime
import random

ssl._create_default_https_context = ssl._create_unverified_context
# s = []
t = random.seed(datetime.datetime.now())
print(t)
def getLinks(artticleUrl):

    html = urlopen("https://en.wikipedia.org" + artticleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

# for link in bsObj.findAll("a"):
#     if "href" in link.attrs:
#         print(link.attrs["href"])

# for link in bsObj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
#     s.append(link.attrs)
#     if "href" in link.attrs:
#         print(link.attrs["href"])
#
#
# print(len(s))

