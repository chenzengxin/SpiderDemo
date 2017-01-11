#coding=utf-8;
'''
Created on 2016年9月23日

@author: chenzengxin
'''
import re;
from lxml import etree;
import zxhtml;
import datacenter


def cleanSpace(content):
    reg='\s+'
    sre=re.compile(reg)
    return re.sub(sre, '', content, 1, 0)

def getSubHref(pageContent):
    if pageContent:
#         reg='<a.*?href="[A-Za-z.:/]+?".*?>[\x80-\xff]*?</a>'
#         are=re.compile(reg)
#         return re.findall(are, pageContent, 0)
        selector=etree.HTML(pageContent);
        data = selector.xpath('//div[@class="the-list"]//a/@href');
        return data;
    else:
        return None
def getMudidiHref(pageContent):
    if pageContent:
#         reg='<a.*?href="[A-Za-z.:/]+?".*?>[\x80-\xff]*?</a>'
#         are=re.compile(reg)
#         return re.findall(are, pageContent, 0)
        selector=etree.HTML(pageContent);
        data = selector.xpath('//*[@id="htmlFt"]/body/div[1]/div/div[2]/div[2]//a/@href');
        return data;
    else:
        return None    
def getUrlFromDic(dic,name_url):
    for item in dic:
        temp={};
        temp['BriefName']=item['BriefName'];
        temp['Url']=item['Url'];
        temp['PName']=item['PName'];
        temp['Id']=item['Id'];
        temp['Pid']=item['Pid'];
        temp['SubRegion']=item['SubRegion']
        name_url.append(temp);
        if item['SubRegion']!=None:
            datacenter.AddParent(item);
            getUrlFromDic(item['SubRegion'],name_url);
    
    
def getChinese(content):
    reg='([\x80-\xff]+)'
    cre=re.compile(reg)
    return re.findall(cre, content, 0)

def getHttp(content):
    reg='http://[a-zA-Z0-9./]+'
    hre=re.compile(reg)
    return re.findall(hre, content, 0)

def getCharset(content):
    reg='<meta.* charset=.*?>'
    cre=re.compile(reg)
    return re.findall(cre,content,0);

def getTitle(content):
    reg='<title>.*</title>'
    tre=re.compile(reg)
    return re.findall(tre, content, 0)

# def getSubHttp(content):
# #     root=etree.fromstring(content);
#     return root.xpath('span');

def getCharset(content):
    reg='charset=".*?"'
    cre=re.compile(reg)
    return re.findall(cre, content, 0)

if __name__=='__main__':
    content=zxhtml.getPageContent("http://www.lotour.com/mudidi/")
    for n in getMudidiHref(content):
        print n;
    
    
