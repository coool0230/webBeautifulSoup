#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : apiGetJson1.py
# @Author: huyn
# @Date  : 2018/4/10
# @Desc  :

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")


print(getCountry('50.78.253.58'))