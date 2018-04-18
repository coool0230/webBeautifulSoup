#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest71.py
# @Author: huyn
# @Date  : 2018/4/18
# @Desc  :

from urllib.request import urlopen
from bs4 import BeautifulSoup

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def ngrams(input,n):
    input = input.split(' ')
    output = []
    for i in range(len(input)-n+1):
        output.append(input[i:i+n])
        return output



html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html,"html.parser")
content = bsObj.find("div",{"id":"mw-content-text"}).get_text()
ngrams = ngrams(content,2)
print(ngrams)
print("2-grams count is:" + str(len(ngrams)))