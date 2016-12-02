#coding=utf-8

'''
Created on 2016年9月23日

@author: chenzengxin
'''
import re;

def cleanSpace(content):
    reg='\s+'
    sre=re.compile(reg)
    return re.sub(sre, '', content, 1, 0)

def getSubHref(pageContent):
    if pageContent:
        reg='<a href="[A-Za-z.:/]+?".*?>[\x80-\xff]*?</a>'
        are=re.compile(reg)
        return re.findall(are, pageContent, 0)
    else:
        return None
def getChinese(content):
    reg='([\x80-\xff]+)'
    cre=re.compile(reg)
    return re.findall(cre, content, 0)

def getHttp(content):
    reg='http://[a-zA-Z0-9./]+'
    hre=re.compile(reg)
    return re.findall(hre, content, 0)