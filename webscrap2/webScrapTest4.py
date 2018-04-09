#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest4.py
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



ssl._create_default_https_context = ssl._create_unverified_context
pages = set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    #找出所有以"/"开头的链接
    for link in bsObj.findAll("a",href = re.compile("^(/|.*'+includeUrl+')")):
        if link.attrs['href'] is not None:
            if (link.attrs['href']) not in internalLinks:
                if (link.attrs['href'].startwith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])

    return internalLinks



#获取页面所有外链的列表

def getExternalLinks(bsObj,excludeUrl):
    externalLinks = []
    #找出所有以" HTTP" 或" www" 开头且不包含当前 URL 的链接
    for link in bsObj.findAll("a",href = re.compile("^(http|www)((?!'+excludeUrl+').)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts





def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html,"html.parser")
    externalLinks = getExternalLinks(bsObj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print ("No external links,looking around the site for one")
        domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
        internalLinks = getInternalLinks(bsObj,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is:"+ externalLink)
    followExternalOnly(externalLink)


followExternalOnly("http://oreilly.com")
