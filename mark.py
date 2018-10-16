#!/usr/bin/env python
#coding=utf8

import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")


'''
['EVENT_FLAG_ALTKEY', 'EVENT_FLAG_CTRLKEY', 'EVENT_FLAG_LBUTTON', 'EVENT_FLAG_MBUTTON', 'EVENT_FLAG_RBUTTON', 'EVENT_FLAG_SHIFTKEY', 'EVENT_LBUTTONDBLCLK', 'EVENT_LBUTTONDOWN', 'EVENT_LBUTTONUP', 'EVENT_MBUTTONDBLCLK', 'EVENT_MBUTTONDOWN', 'EVENT_MBUTTONUP', 'EVENT_MOUSEMOVE', 'EVENT_RBUTTONDBLCLK', 'EVENT_RBUTTONDOWN', 'EVENT_RBUTTONUP']
'''

import cv2
import numpy as np
import sys
import os
import shutil

from cvmouse import *

tdir='./ready/'
tdirdes='./finish/'
tdirtxt='./txt/'

paralist=[]

def getlistdir(pdir,plist):
	del plist[:]
	filenum = 0
	list = os.listdir(pdir)  #列出目录下的所有文件和目录
	for line in list:
		if(filenum==1):
			return ''
		filepath = os.path.join(pdir,line)
		if os.path:   #如果filepath是文件，直接列出文件名
			try:
				if(line.index('.JPG')):
					
					filenum+=1
					plist.append(pdir)
					plist.append(line)
					return pdir+line
			except:
				pass
			try:
				if(line.index('.jpg')):
					
					filenum+=1
					plist.append(pdir)
					plist.append(line)
					return pdir+line
			except:
				pass
	if(filenum==0):
		return ''

print 'start!!!'

settxtpath(tdirtxt)

while(1):
	str1=getlistdir(tdir,paralist)
	if(len(str1)>0):
		print str1
		print paralist
		tv=dealimg(str1)
		if(tv==121):
			break
		#在将jpg数据剪切前，将同文件前缀名的txt文件进行转xml的处理
		shutil.move(str1,tdirdes+str(paralist[1]))
	if(len(str1)==0):
		break
stop()