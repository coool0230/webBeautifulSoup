#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : webScrapTest72.py
# @Author: huyn
# @Date  : 2018/4/18
# @Desc  :


from urllib.request import urlopen
# from bs4 import BeautifulSoup
import re
import string
import operator

def cleanInput(input):
    input = re.sub('\n+'," ",input).lower()
    input = re.sub('\[[0-9]*\]',"",input)
    input = re.sub(' +'," ",input)
    input = bytes(input,"UTF-8")
    input = input.decode("ascii","ignore")
    cleanInput = []


    input = input.split(' ')

    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)


    return cleanInput


def ngrams(input,n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0

        output[ngramTemp] +=1
    return output


def isCommon(ngram):
    commonWords = ["the","be","and","of","a","in","to","have","it","i","that","for","you","he","with","on","do","say",
                   "this","they","is","an","at","but","we","his","from","not","by","she","or","as","what","go","their",
                   "can","who","get","if","would","her","all","my","make","about","know","will","up","one","time","has",
                   "been","there","year","so","think","when","which","them","some","me","people","take","out","into",
                   "just","see","him","your","come",'could',"now","than","like","other","hwo","then","its","our",
                   "two","more","thest","want","way","look","first","also","new","because",'day',"use","no","man","find",
                   "here","thing","give","many","well"]

    for word in ngram:
        if word in commonWords:
            return True
    return False

content = str(
    urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(),'utf-8')

# ngrams = isCommon(ngrams)
# print(ngrams)
# print('------------------------------------------------------------------------------------')
ngrams = ngrams(content,2)
# print(ngrams)
# print('***************************************************************************************')

sortedNGrams = sorted(ngrams.items(),key = operator.itemgetter(1),reverse=True)
print(sortedNGrams)

s = isCommon(sortedNGrams)
print(s)