#coding=utf-8

import zxhtml;
import zxfile;
import zxregular;
import time;
import threading
from time import ctime,sleep
import sys;
reload(sys)
sys.setdefaultencoding('utf-8')  # @UndefinedVariable
GrabDirectory={}



def getAllLink(rootpath,page,time):
    hm=zxhtml.HtmlManager(50);
    content=hm.getPageContent(page);
    alist=zxregular.getSubHref(content)
    zxfile.CreateFile(rootpath, str(rootpath.split('\\')[-1])+'ALink'+'.txt',alist)
    zxfile.CreateFile(rootpath, str(rootpath.split('\\')[-1])+'.txt',content)
    if (alist is None):
        return
    if not (len(alist)>0):
        return
    if (time-1<0):
        return;
    global GrabDirectory
    for item in alist:
        namelist=zxregular.getChinese(item)
        httplist=zxregular.getHttp(item)
        if len(namelist)>0 and len(httplist)>0:
            for e in httplist:
                try:
                    name=str(namelist[-1]).decode('utf-8')
                except Exception:
                    info=sys.exc_info()  
                    print info[0],":",info[1]
                    print item
                    name=str(namelist[-1]).decode('gbk')
                print name
                print e
                getAllLink(rootpath+'\\'+name, e,time-1)
    
def CheckIfGraboff(key):
    global GrabDirectory
    if(GrabDirectory.__contains__(key)):
        return True
    else:
        return False



if __name__ == '__main__':
    href={}
    mainpage='http://www.lotour.com/mudidi/'
    t1=threading.Thread(target=getAllLink,args=('Contents',mainpage,2))
    t1.start()
    while t1.isAlive():
        pass
    