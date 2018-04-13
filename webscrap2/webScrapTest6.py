#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest6.py
# @Author: huyn
# @Date  : 2018/4/11
# @Desc  :


from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re,ssl
ssl._create_default_https_context = ssl._create_unverified_context

random.seed(datetime.datetime.now())

def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html,"html.parser")
    return bsObj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile(("^(/wiki/)((?!:).)*$")))

def getHistoryIPs(pageUrl):
    #编辑历史页面 URL 链接格式是:
    #http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/","")
    historyUrl = "http://en.wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is :" + historyUrl)
    html = urlopen(historyUrl,)
    bsObj = BeautifulSoup(html,"html.parser")
    #找出 class 属性是" mw-userlink mw-anonuserlink"的链接
    #他们用 IP 地址代替用户名
    ipAddresses = bsObj.findAll("a",{"class":"mw-userlink ms-anonuserlink"})
    addressList = set()

    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ipAddress):
    try:
        response = urlopen("http://freegeoip.net/json"+ipAddress).read().decode('utf-8')

    except HTTPError:
        return None
    responseJson = json.loads(response)
    return responseJson.get("country_code")


links = getLinks("/wiki/python_(programming_language)")

while(len(links) > 0):
    for link in links:
        print("-------------------------------")
        histotyIPs = getHistoryIPs(link.attrs["href"])
        for histotyIP in histotyIPs:
            country = getCountry(histotyIP)
            if country is not None:
                print(histotyIP + "is from " + country)

    newLink = links[random.randint(0,len(links)-1)].attrs["href"]
    links = getLinks(newLink)