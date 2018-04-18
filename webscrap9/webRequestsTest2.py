#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webRequestsTest2.py
# @Author: huyn
# @Date  : 2018/4/18
# @Desc  :

import requests
# files = {'uploadFile':open('/Users/huyn/PycharmProjects/webScrap/webscrap5/logo.jpg','rb')}
# r = requests.post("http://pythonscraping.com/pages/processing2.php",files = files)
# print(r)

# params = {"username":'ryan',"password":"password"}
# r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php",params)
# print('Cookie is set to:')
# print(r.cookies.get_dict())
# print('----------------')
# print('Going tp profile page....')
# r = requests.get("http://pythonscraping.com/pages/cookies/profiles.php",cookies = r.cookies)
# print(r.text)


from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('ryan','password')
r = requests.post(url= 'http://pythonscraping.com/pages/auth/login.php',auth=auth)
print(r.text)