#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xml.dom.minidom
import cv2
import os
import numpy as np
import sys
import shutil

xmlrdir='./xmldes'#'/home/hyzn/Documents/py-faster-rcnn/data/VOCdevkit2007/VOC2007/Annotations'
imgrdir='./checked'#'/home/hyzn/Documents/py-faster-rcnn/data/VOCdevkit2007/VOC2007/JPEGImages'
txtrdir='./txt'#'/home/hyzn/Documents/py-faster-rcnn/data/VOCdevkit2007/VOC2007/txt'
xmlsuffix='.xml'
imgsuffix='.jpg'
txtsuffix='.txt'
label=''
w=0
h=0
xmin=0
ymin=0
xmax=0
ymax=0
subw=0
subh=0

def c_or_w(pfn,pwritedata):#创建文件写入内容或者打开已经有的文件追加内容
	if os.path.exists(pfn):
		#print 'ok'
		tf=open(pfn,'a')
		tf.write('\r\n'+pwritedata)
		tf.close()
	else:
		#print 'no'
		tf=open(pfn,'w')
		tf.write(pwritedata)
		tf.close()

def write2txt(pfn,plist):#将文件名，类型和x,y minmax整理好写入规定路径的txt文件
	if(len(plist)<4):
		return 
	else:
		tdata=','.join(plist)+','
		#print tdata
		c_or_w(pfn,tdata)

xmllist=os.listdir(xmlrdir)
count=0
for item in xmllist:
	count+=1
	if item.lower().endswith(xmlsuffix.lower()):
		imgname=os.path.splitext(item)[0]
		imgpath = os.path.join(imgrdir,imgname+imgsuffix)
		print imgpath
		if os.path.exists(imgpath):
			xmlpath=os.path.join(xmlrdir,item)
			print xmlpath
			dom = xml.dom.minidom.parse(xmlpath)
			root = dom.documentElement
			subsize = root.getElementsByTagName('size')
			for item in subsize:
				ss=item.childNodes
				ww=int(ss[1].firstChild.data)
				hh=int(ss[3].firstChild.data)	
			subobject = root.getElementsByTagName('object')
			n=0
			for item in subobject:
				tlist=[]
				subname=item.getElementsByTagName('name')[0]
				label=subname.firstChild.data
				subbndbox=item.getElementsByTagName('bndbox')
				for coordinate in subbndbox:
					n=n+1
					#print coordinate.nodeName
					xy=coordinate.childNodes
					xmin=int(xy[1].firstChild.data)
					ymin=int(xy[3].firstChild.data)
					xmax=int(xy[5].firstChild.data)
					ymax=int(xy[7].firstChild.data)
					img = cv2.imread(imgpath,cv2.IMREAD_UNCHANGED)
					h=int(img.shape[0])
					w=int(img.shape[1])
					#print label,w,h,xmin,xmax,ymin,ymax
					value=(float)(xmax-xmin)/(float)(ymax-ymin)
					if(value<0.117 or value>15.50):
						print 'error'+xmlpath
					'''
					if w!=ww:
						print 'error ','h= ',hh
					if h!=hh:
						print 'error ','w= ',ww
					if xmin<=0 and xmin>=w:
						print 'error xmin ',xmin
					if ymin<=0 and ymin>=h:
						print 'error ymin ',ymin
					if xmax<=0 and xmax>=w:
						print 'error xmax ',xmax
					if ymax<=0 and ymax>=h:
						print 'error ymax ',ymax
					if xmin<=0:
						xmin=1
					if xmin>=w:
						xmin=w-1
					if ymin<=0:
						ymin=1
					if ymin>=h:
						ymin=h-1
					if xmax>=w:
						xmax=w-1
					if xmax<=0:
						xmax=1
					if ymax>=h:
						ymax=h-1
					if ymax<=0:
						ymax=1
					tlist.append(label)
					tlist.append(w)
					tlist.append(h)
					tlist.append(xmin)
					tlist.append(xmax)
					tlist.append(ymin)
					tlist.append(ymax)
					tlist=[ str(i) for i in tlist ]
					txtpath=os.path.join(txtrdir,imgname+txtsuffix)
					write2txt(txtpath,tlist)
					'''
