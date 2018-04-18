#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest54.py
# @Author: huyn
# @Date  : 2018/4/17
# @Desc  :

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html,"html.parser")
#主对比表格是当前页面上的第一个表格

table = bsObj.findAll("table",{"class":"wikitable"})[0]
rows = table.findAll("tr")

csvFile = open("/Users/huyn/PycharmProjects/webScrap/webscrap5/editors.csv","wt",newline='',encoding='utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td','th']):
            csvRow.append(cell.get_text())

        writer.writerow(csvRow)



finally:
    csvFile.close()
