#coding=utf-8
import zxhtml;
import zxregular;
import zxfile;
import time;
import threading
from time import ctime,sleep
import sys;
import chardet
from __builtin__ import str
from test.test_threading_local import target
from mutex import mutex
reload(sys)
sys.setdefaultencoding('utf8')

mutex=threading.Lock()
def getAllLink(mainpage,href):
    hm=zxhtml.HtmlManager(50);
    alist=zxregular.getSubHref(hm.getPageContent(mainpage))
    for item in alist:
#        print item+'\n'
#         print '<a>:'
#         print item
#         print '\n'
        namelist=zxregular.getChinese(item)
#         print '中文'
#         print namelist
#         print '\n'
        httplist=zxregular.getHttp(item)
#         print '网址'
#         print httplist
#         print '\n'
        if len(namelist)>0 and len(httplist)>0:
            time.sleep(1)
            for e in httplist:
                try:
                    name=str(namelist[-1]).decode('utf-8')
                except Exception:
                    print Exception
                    name=str(namelist[-1]).decode('gbk')
                if mutex.acquire(1):
#                     threading.Thread(target=getSubPageInfo,args=(e,name)).start()
                    print name
                    print e
                    print '\n'
                    getSubPageInfo(e, name)
                #href.append(e)
                #name=str(namelist[0]).decode('utf-8')
                #zxfile.CreateFile('Link',name+'.txt',e)
                print '线程结束'
    print "t1 over"
#获取景点中的所有信息
def getSubPageInfo(href,father):
    print "SubPageInfoEnter"
    try:
        print "SubPageInfoTry"
        hm=zxhtml.HtmlManager()
        content=hm.getPageContent(href)
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
    #                    getPageDetail(e, u"Contents\\"+father, name)

    except Exception:
        print "Over"
    finally:
        mutex.release()
#获取景点信息中的景区，酒店**********
def getPageDetail(http,father,name):
    print http
    hm=zxhtml.HtmlManager(50);
    content=hm.getPageContent(http)
    alist=zxregular.getSubHref(content)
    if alist==None:
       return
    if content is not None:
#            print 'Contents/'+father+'/'+name+'/'+name+'.txt'
        zxfile.CreateFile(father+u'\\'+name, name+u".txt", content)
        print str(father)+u'\\'+str(name)+'\\'+str(name)+u".txt"

#def getAllPageInfo(href):
#    while True:
#        if mutex.acquire(1):
#            print href.values()
#            print "线程2正在操作"+'\n'
#           mutex.release()
if __name__ == '__main__':
    href={}
    mainpage='http://www.lotour.com/mudidi/'
    t1=threading.Thread(target=getAllLink,args=(mainpage,href,))
    t1.start()

    while t1.isAlive():
        pass
#        print "主线程正在等待抓取所有链接"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))+'\n'
#    print href.values();
    