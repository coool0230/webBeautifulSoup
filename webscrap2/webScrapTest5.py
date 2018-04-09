#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest5.py
# @Author: huyn
# @Date  : 2018/4/9
# @Desc  :

from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import ssl

from webscrap2.webScrapTest4 import getExternalLinks,\
    getInternalLinks,splitAddress

ssl._create_default_https_context = ssl._create_unverified_context


#
# #获取页面所有内链的列表
# def getInternalLinks(bsObj,includeUrl):
#     includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
#     internalLinks = []
#     #找出所有以"/"开头的链接
#     for link in bsObj.findAll("a",href = re.compile("^(/|.*'+includeUrl+')")):
#         if link.attrs['href'] is not None:
#             if (link.attrs['href']) not in internalLinks:
#                 if (link.attrs['href'].startwith("/")):
#                     internalLinks.append(includeUrl+link.attrs['href'])
#                 else:
#                     internalLinks.append(link.attrs['href'])
#
#     return internalLinks
#
#
#
# #获取页面所有外链的列表
#
# def getExternalLinks(bsObj,excludeUrl):
#     externalLinks = []
#     #找出所有以" HTTP" 或" www" 开头且不包含当前 URL 的链接
#     for link in bsObj.findAll("a",href = re.compile("^(http|www)((?!'+excludeUrl+').)*$")):
#         if link.attrs['href'] is not None:
#             if link.attrs['href'] not in externalLinks:
#                 externalLinks.append(link.attrs['href'])
#     return externalLinks
#
#
#
# def splitAddress(address):
#     addressParts = address.replace("http://", "").split("/")
#     return addressParts

#收集网站上发现的所有外链列表
allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(ling)
            print(link)

    for link in internalLinks:
        if link not in allIntLinks:
            print("即将获取链接的 url 是:"+link)
            allIntLinks.add(link)
            getAllExternalLinks(link)




getAllExternalLinks("http://oreilly.com")