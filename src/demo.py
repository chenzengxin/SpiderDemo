#coding=utf-8



import urllib2

import urllib

import re

import threading

from time import ctime,sleep

import os

import time

'''
create time: 2016年7月16日

@author: chenzengxin
'''



#get the page information,startPage------url,example:http://www.baidu.com;

def GetPageInfo(startPage):
	
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  
	
	values = {'username' : 'cqc',  'password' : 'XXXX' }
	
	headers = { 'User-Agent' : user_agent }  
	
	data = urllib.urlencode(values)
	
	request = urllib2.Request(startPage, data, headers) 
	
	response = urllib2.urlopen(request)  
	
	pageContent = response.read()
	
	
#print pageContent
	
	
#print page
	
#GetSubPages(page):
	
	pageList=GetSubPages(pageContent);
	
	for item in pageList:
		print item+'\n';	
	file.CreateFile("file","href",pageList)
		
#get subpages information;

def GetSubPages(page):
	
	reg=r'<a.*?/a>'
    	
	hrefre=re.compile(reg)
    	
	return re.findall(hrefre,page,0)



if __name__=='__main__':
	
	GetPageInfo('http://www.lotour.com/mudidi/')
