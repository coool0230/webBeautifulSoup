#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webRequestTest1.py
# @Author: huyn
# @Date  : 2018/4/18
# @Desc  :

import requests
# params = {'firstname':"Ryan","lastname":"Mitchell"}
#
# r = requests.post("http://pythonscraping.com/files/processing.php",data = params)
# print(r.text)

params = {"email_addr":"ryan.e.mitchell@gmail.com"}

r = requests.post("http://post.oreilly.com/client/o/oreilly/frorms/quicksignup.cgi",data = params)
print(r)