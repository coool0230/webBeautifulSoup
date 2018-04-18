#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest53.py
# @Author: huyn
# @Date  : 2018/4/17
# @Desc  :

import csv

csvFile = open("/Users/huyn/PycharmProjects/webScrap/webscrap5/test.csv","w+")
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number','number plus 2','number times 2'))
    for i in range(10):
        writer.writerow((i,i+2,i*2))



finally:
    csvFile.close()