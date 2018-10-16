#!/usr/bin/env python
#coding=utf8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

import os
import os.path
'''
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEMOVE', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
'''
import cv2
import numpy as np
from checkreadvoc import *

imgnew=cv2.imread('/home/heavytank/temp/c.jpg')#新图
img1 = cv2.imread('/home/heavytank/temp/c.jpg')#原始图
cv2.namedWindow('image',cv2.WINDOW_NORMAL)#界面


pre_pt=(0,0)#保存左键按下的点
flag=1#开始有效区域划定
flagmove=1

value=0#按下的键值表示按下哪个键，0表示什么分类都没有

posxf=0#按下时的x
posyf=0#按下时的y
posxs=0#弹起时的x
posys=0#弹起时的y

pushtag=1#是否处在按下过程中
g_min_max_list=[]#保存x，y min max的列表

xmlpath='' #txt文件的放置路径 带/

def c_or_w(pfn,pwritedata):#创建文件写入内容或者打开已经有的文件追加内容
    if os.path.exists(pfn):
        print 'ok'
        tf=open(pfn,'a')
        tf.write('\n'+pwritedata)
        tf.close()
    else:
        print 'no'
        tf=open(pfn,'w')
        tf.write(pwritedata)
        tf.close()



def write2txt(pfn,pvalue,plist):#将文件名，类型和x,y minmax整理好写入规定路径的txt文件
    if(len(plist)<4):
        return 
    else:
        tdata='%d,%s,%s,%s,%s,' %(pvalue,plist[0],plist[1],plist[2],plist[3])
        #print tdata
        c_or_w(pfn,tdata)

def settxtpath(ppath):#从其他模块传递txt路径
	global xmlpath
	xmlpath=ppath
	print xmlpath


def getminmax(xf,yf,xs,ys):#从基本坐标
	plist=[]
	del plist[:]
	if(abs(xf-xs)<15 or abs(yf-ys)<15):
		return plist
	if(xf<xs):
		plist.append(xf)
		plist.append(xs)
	if(xf>xs):
		plist.append(xs)
		plist.append(xf)
	if(yf<ys):
		plist.append(yf)
		plist.append(ys)
	if(yf>ys):
		plist.append(ys)
		plist.append(yf)
	return plist

def draw(event,x,y,flags,param):#鼠标事件回调处理
	global imgnew
	global img1
	global pre_pt
	global flag
	global flagmove
	global value
	global posxf
	global posyf
	global posxs
	global posys
	global pushtag
	global g_min_max_list



	if event==cv2.EVENT_LBUTTONDOWN:
		
		flag=1
		pushtag=1
		imgnew=img1.copy()
		pre_pt = (x,y)
		posxf=x
		posyf=y
		
		
	if (event==cv2.EVENT_MOUSEMOVE and flag):
		if(pushtag==1):
			flagmove=1
			tp=(x,y)
			imgnew=img1.copy()
			cv2.rectangle(imgnew,pre_pt,tp,(0,0,255),2)
			posxs=x
			posys=y
			cv2.imshow('image',imgnew)
	if event==cv2.EVENT_LBUTTONUP:
		print 'value'+str(value)
		pushtag=0
		if(flagmove==1):
			posxs=x
			posys=y
		flagmove=0
		del g_min_max_list[:]
		g_min_max_list=getminmax(posxf,posyf,posxs,posys)
		print g_min_max_list
		if(len(g_min_max_list)==0):
			value=0
		

#右键部分不用
''''
	if event==cv2.EVENT_RBUTTONDOWN:
		flag=1
		imgnew=img1.copy()
		pre_pt = (x,y)
	if (event==cv2.EVENT_MOUSEMOVE and flag):
		tp=(x,y)
		imgnew=img1.copy()
		cv2.rectangle(imgnew,pre_pt,tp,(55,255,155),1)
		cv2.imshow('image',imgnew)
	if event==cv2.EVENT_RBUTTONUP:
		flag=0
		print 'right up'
		print pre_pt
		print x,y
'''

def getrealxmlname(pfn):#根据jpg路径，得到真实的txt全路径

	global xmlpath

	tbfn=os.path.basename(pfn)#真实文件名
	suffix=os.path.splitext(tbfn)[1]#获取后缀
	return xmlpath+tbfn[0:(0-len(suffix))]+'.xml'


def dealimg(fn):#给定一个jpg文件，对其进行标定处理
	
	global imgnew
	global img1
	global pre_pt
	global flag
	global flagmove
	global value
	global posxf
	global posyf
	global posxs
	global posys
	global pushtag
	global g_min_max_list

	global xmlpath

	xmlfn=getrealxmlname(fn)
	tl=[]
	try:
		read_xml(open(xmlfn).read(),tl)
		print tl
	except Exception,e:
		print e

	print '**************\n'+xmlfn+'************'
	imgnew=cv2.imread(fn)
	img1 = cv2.imread(fn)# 
	sp=img1.shape
	
	print str(sp[0])+str(sp[1])
	#cv2.setMouseCallback('image',draw)
	flag=0
	flagmove=0
	pushtag=0
	while(1):
		if flag==0:
			if(len(tl)>0):
				for each in tl:
					cv2.rectangle(img1,((int)(each[0]),(int)(each[1])),((int)(each[2]),(int)(each[3])),(0,0,255),2)
					font = cv2.FONT_HERSHEY_SIMPLEX
					cv2.putText(img1,str(each[4]), ((int)(each[2]),(int)(each[3])), font, 1, (0,0,255), 2)
					#print 'each'+'xxx'
					#print each
			cv2.imshow('image',img1)	
		keyv=cv2.waitKey(20)&0xFF
		if keyv==27:
			break
		if keyv==97:
			value=97
			break
		if keyv==98:
			value=98
			break
		if keyv==99:
			value=99
			break
		if keyv==100:
			value=100
			break
		if keyv==101:
			value=101
			break
		if keyv==102:
			value=102
			break
		if keyv==119:
			pass
		if keyv==120:
			pass
	return keyv
def stop():#销毁opencv窗口
  cv2.destroyAllWindows()

#dealimg('/home/heavytank/temp/c.jpg')
