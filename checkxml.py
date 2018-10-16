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

from checkcvmouse import *


tdir='./finish/'
tdirdes='./checked/'
tdirerror='./error/'
tdirxml='./xml/'
txmldes='./xmldes/'
paralist=[]

def getlistdir(pdir,plist):
	del plist[:]
	filenum = 0
	print pdir,'000'
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

settxtpath(tdirxml)
print '11'
while(1):
	print '22'
	str1=getlistdir(tdir,paralist)
	if(len(str1)>0):
		print str1,'--'
		print paralist,'=='
		tvalue=dealimg(str1)
		if(tvalue==27):
			break
		if(tvalue==97):
			shutil.move(str1,tdirdes+str(paralist[1]))

			tbfn=os.path.basename(str(paralist[1]))#真实文件名
			suffix=os.path.splitext(tbfn)[1]#获取后缀
			xmlfn=tbfn[0:(0-len(suffix))]+'.xml'
			try:
				shutil.move(tdirxml+xmlfn,txmldes+xmlfn)
			except:
				pass
			
		if(tvalue==98):
			shutil.move(str1,tdirerror+str(paralist[1]))
		if(tvalue==99):
			shutil.move(str1,tdirerror+str(paralist[1]))
		if(tvalue==100):
			shutil.move(str1,tdirerror+str(paralist[1]))
		if(tvalue==101):
			shutil.move(str1,tdirerror+str(paralist[1]))
		if(tvalue==102):
			shutil.move(str1,tdirerror+str(paralist[1]))
	if(len(str1)==0):

		break
stop()
