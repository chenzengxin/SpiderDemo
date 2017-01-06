<<<<<<< HEAD
#coding=utf-8
  
=======
#coding=utf-8;
>>>>>>> origin/master
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
        reg='<a.*?href="[A-Za-z.:/]+?".*?>[\x80-\xff]*?</a>'
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

def getTitle(content):
    reg='<title>.*</title>'
    tre=re.compile(reg)
    return re.findall(tre, content, 0)


def getCharset(content):
    reg='charset=".*?"'
    cre=re.compile(reg)
    return re.findall(cre, content, 0)

if __name__=='__main__':
    test='<a title="呼和浩特旅游景区" href="http://huhehaote.lotour.com/jingqu/"><span>景区</span></a>'
    print getChinese(test)
    
    
    
    
