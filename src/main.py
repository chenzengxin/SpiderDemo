#coding=utf-8
import zxfile
import zxregular
import zxhtml
import time
import threading
from time import ctime,sleep
import sys;
from lxml import etree;
import datacenter
# reload(sys)
# sys.setdefaultencoding('utf-8')  # @UndefinedVariable
GrabDirectory={}
def Spider(rootpath,page,time):
        if time<0:
            return
        content=zxhtml.getPageContent(page);
        alist=zxregular.getSubHref(content)
        zxfile.CreateFile(rootpath, str(rootpath.split('/')[-1])+'ALink'+'.txt',alist)
        zxfile.CreateFile(rootpath, str(rootpath.split('/')[-1])+'.txt',content)
        if (alist is None):
            return
        if not (len(alist)>0):
            return
        for item in alist:
            namelist=zxregular.getChinese(item)
            httplist=zxregular.getHttp(item)
            if len(namelist)>0 and len(httplist)>0:
                for e in httplist:
                    try:
                        name=str(namelist[-1]).decode('utf-8')
                    except Exception:
                        name=str(namelist[-1]).decode('gbk')
                    Spider(rootpath+'/'+name, e,time-1)
def CheckIfGraboff(key):
    global GrabDirectory
    if(GrabDirectory.__contains__(key)):
        return True
    else:
        return False
def getSubPageInfo(href,father):
    print "SubPageInfoEnter"
    try:
        print "SubPageInfoTry"
        content=zxhtml.getPageContent(href)
        if content:
            zxfile.CreateFile(u"Contents\\"+father, father+u".txt", content)
        alist=zxregular.getSubHref(content)
        if alist==None:
            return
        for item in alist:
            namelist=zxregular.getChinese(item)
            httplist=zxregular.getHttp(item)
            if len(namelist)>0 and len(httplist)>0:
                for e in httplist:
                    try:
                        name=str(namelist[0]).decode('utf-8')
                    except Exception:
                        name=str(namelist[0]).decode('gbk')
                    print name
                    getPageDetail(e,'Contents\\'+father,name)

    except Exception:
        print "Over"
def getPageDetail(http,father,name):
    print http
    hm=zxhtml.HtmlManager(50);
    content=hm.getPageContent(http)
    alist=zxregular.getSubHref(content)
    if alist==None:
       return
    if content is not None:
        zxfile.CreateFile(father+u'\\'+name, name+u".txt", content)
        print str(father)+u'\\'+str(name)+'\\'+str(name)+u".txt"

def Spider(): 
    links=zxhtml.getRegiondata();
    for link in links:
        name = link['BriefName'];
        print name;
        url = link['Url'];
        print url;
        ScanEachRegion(link);
    
def ScanEachRegion(link):
    neme = link['BriefName'].replace(" ","");
    path=datacenter.FindPath(link)+'/'+neme;
    print path;
    zxfile.CreateFile(path,neme+".txt","");

    

if __name__ == '__main__':
#     href={}
#     mainpage='http://www.lotour.com/mudidi/'
#     t1=threading.Thread(target=getAllLink,args=('Contents',mainpage,2))
#     t1.start()
#     while t1.isAlive():
#         pass
    Spider()
