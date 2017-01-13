#coding=utf-8
import urllib2;
import urllib;
import json;
import zxregular
'''
Created on 2016年9月23日

@author: chenzengxin
'''
from _codecs import decode
def getRegiondata():
    name_url=[];#用以保存抓取到的链接数据
    api="http://api.lotour.net/brandhome/region/getregiondataa?"
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36' 
    accept_language='zh-CN,zh;q=0.8'
    headers = { 'User-Agent' : user_agent,'Accept-Language':accept_language} 
    href =api+"name=%u4E2D%u56FD&depth=2&callback=";
    
    #国内
    request = urllib2.Request(href) 
    data = urllib2.urlopen(request);
#     (data.read().decode('GBK'));
    json_data=data.read()[1:-1]
    json_obj=json.loads(json_data,'GBK')
    zxregular.getUrlFromDic(json_obj,name_url);
    
    #国外
    href = api+"name=%u4E16%u754c&depth=2&callback="
    request = urllib2.Request(href) 
    data = urllib2.urlopen(request);
#     (data.read().decode('GBK'));
    json_data=data.read()[1:-1]
    json_obj=json.loads(json_data,'GBK')
    zxregular.getUrlFromDic(json_obj,name_url);
    return name_url;
    
#     json_str= json.loads(data.read()[1:-2]);
#     print json_str;
#     print decode(data.read(),"GBK");
    
    
    
def getPageContent(href):
    try:
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36' 
        values = {'username' : 'cqc',  'password' : 'XXXX' }
        accept_language='zh-CN,zh;q=0.8'
        headers = { 'User-Agent' : user_agent,'Accept-Language':accept_language}  
        data = urllib.urlencode(values)
        request = urllib2.Request(href, data, headers) 
        response = urllib2.urlopen(request)
        pageContent = response.read()
    except Exception:
        return None;
    return pageContent;


if __name__=="__main__":
    getRegiondata();
#     data = {
#     'name' : 'ACME',
#     'shares' : 100,
#     'price' : 542.23
#     }
#      
#     json_str = json.dumps(data)
#     print json_str;
    
    