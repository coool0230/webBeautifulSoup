#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : apiJson2.py
# @Author: huyn
# @Date  : 2018/4/10
# @Desc  :


import json
jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":3}],' \
             '"arrayOfFruits":[{"fruit":"apple","str":"huyn"},{"fruit":"banbana"},{"fruit":"pear"}]}'

jsonObj = json.loads(jsonString)

print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number")+jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[0].get("str"))