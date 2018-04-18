#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest55.py
# @Author: huyn
# @Date  : 2018/4/17
# @Desc  :

# from urllib.request import  urlopen
# from io import StringIO
# import csv
# data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
#
# dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
#
# for row in csvReader:
#     # print(row)
#     print('The album \"' + row[0] + '\" + was released in  '+ str(row[1]))



from urllib.request import urlopen
from io import StringIO
import csv
data = urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)

dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)