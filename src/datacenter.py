#coding=utf-8
'''
Created on 2017年1月11日

@author: Administrator
'''

parent=[]

def AddParent(dic):
    parent.append(dic);


def FindPath(dic):
    if dic['Url']=="http://huangshan.lotour.com/huangshanfjq/":
        print "";
    for item in parent:
        if int(str(item['Id']).replace(str(item['Pid']),"",1))==dic['Pid']:
            return (item['PName'].replace(" ","")+'/'+item['BriefName'].replace(" ",""));
    return dic['PName'].replace(" ","");
