#coding=utf-8

import os
def CreateFile(dir_name,file_name,content):
	#mkdir current dir+"/name";
#	if os.path.exists(os.getcwd()+"/"+dir_name):
#		print "file exit"
#	else:
#		os.mkdir(dir_name)
	if not os.path.exists(os.getcwd()+"/"+dir_name):
		os.mkdir(os.getcwd()+"/"+dir_name)
	fc=open(dir_name+"/"+file_name,"w") #文本写模式，不存在则创建
	fc.writelines(content)
	
#	fc=open(dir_name+"/"+file_name,"w");
	
#	fc.writelines(content);
	
def ReadFile(dir_name,file_name,content):
	if not os.path.exists(os.getcwd()+"\\"+dir_name+"\\"+file_name):
		print "False"
		return False
	else:
		fc=open(dir_name+"\\"+file_name,"r")#文本读模式
		content=fc.readlines()
		print fc.readlines()
		return True
	
def GetAllFile(dir):
	return os.listdir(os.getcwd()+'\\'+dir)
	


if __name__=="__main__":
	list=os.listdir(os.getcwd()+'\\'+"Link")
	for name in list:
		print str(name).decode('gbk')+'\n'
