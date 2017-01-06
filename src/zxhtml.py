<<<<<<< HEAD
#coding=utf-8
 
=======
#coding=utf-8;
>>>>>>> origin/master
import urllib2;
import urllib;


class HtmlManager(object):
    maxnum=0;
    curnum=0;
    '''
    classdocs
    '''
    def __init__(self,maxnum):
        '''
        Constructor
        '''
        self.maxnum=maxnum;
    def getPageContent(self,href):
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
    
    