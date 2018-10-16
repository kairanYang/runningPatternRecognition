#!/usr/bin/env python
#coding=utf8
import sys 
reload(sys) 
sys.setdefaultencoding("utf-8")

import numpy as np
import sys
import os
import os.path
import shutil
import time
import string
from lxml import etree
from xml.etree import ElementTree  



ttxtdir='./txt/'
ttxtdes='./txtdes/'
txmldir='./xml/'




#fn xml文件名 inname 类别标签   inseg segment  inw 图像width inh 图像高 indep 图像深度，也就是色彩维度  infoldername 文件夹名字 intruefn图片文件名
def create_xml(fn,inname,inseg,inw,inh,indep,infoldername,intruefn,pointlist):
	#global g_list
	annotation = etree.Element("annotation")
	#1 folder
	folder_txt = infoldername
	folder = etree.SubElement(annotation, 'folder')
	folder.text = folder_txt

	#2 filename

	filename_txt = intruefn
	filename = etree.SubElement(annotation, 'filename')
	filename.text = filename_txt


	#3 source
	source_txt = 'source'
	source = etree.SubElement(annotation, 'source')
	source.text = source_txt

	#4 owner
	owner_txt = 'owner'
	owner = etree.SubElement(annotation, 'owner')
	owner.text = owner_txt

	#5 owner
	size_txt = 'size'
	size = etree.SubElement(annotation, 'size')
	#size.text = size_txt

	#5.1 width
	w_txt = inw
	w = etree.SubElement(size, 'width')
	w.text = w_txt

	#5.2 height
	h_txt = inh
	h = etree.SubElement(size, 'height')
	h.text = h_txt

	#5.3 depth
	d_txt = indep
	d = etree.SubElement(size, 'depth')
	d.text = d_txt

	#6
	segmented_txt = inseg
	segmented = etree.SubElement(annotation, 'segmented')
	segmented.text = segmented_txt

	#7

	objects = etree.SubElement(annotation, 'object')
   
	#7.1 name
	name_txt = inname
	name = etree.SubElement(objects, 'name')
	name.text = name_txt
	#7.2 pose
	pose_txt = 'pose'
	pose = etree.SubElement(objects, 'pose')
	pose.text = pose_txt

	#7.3  truncated
	truncated_txt = 'truncated'
	truncated = etree.SubElement(objects, 'truncated')
	truncated.text = truncated_txt

	#7.4 difficult
	difficult_txt = 'difficult'
	difficult = etree.SubElement(objects, 'difficult')
	difficult.text = segmented_txt
	#7.5 bndbox
	for a in pointlist:
		bndbox = etree.SubElement(objects, 'bndbox')

		#7.5.1 xmin
		xmin_txt = a[0]
		xmin = etree.SubElement(bndbox, 'xmin')
		xmin.text = xmin_txt
		#7.5.2 ymin
		ymin_txt = a[1]
		ymin = etree.SubElement(bndbox, 'ymin')
		ymin.text = ymin_txt
		#7.5.3 xmax
		xmax_txt = a[2]
		xmax = etree.SubElement(bndbox, 'xmax')
		xmax.text = xmax_txt

		#7.5.4 ymax
		ymax_txt = a[3]
		ymax = etree.SubElement(bndbox, 'ymax')
		ymax.text = ymax_txt
   

	dataxml = etree.tostring(annotation, pretty_print=True, encoding="UTF-8", method="xml",xml_declaration=True, standalone=None)
	#print dataxml
	f=open(fn,'w')
	f.write(dataxml)
	f.close()


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
				if(line.index('.txt')):
					
					filenum+=1
					plist.append(pdir)
					plist.append(line)
					return pdir+line
			except:
				pass
			try:
				if(line.index('.TXT')):
					
					filenum+=1
					plist.append(pdir)
					plist.append(line)
					return pdir+line
			except:
				pass
	if(filenum==0):
		return ''

def gettxtinfo(fn,plstdata,plstpoint):
	del plstpoint[:]
	del plstdata[:]
	


	file = open(fn) 
	while 1:
		line = file.readline()
		if not line:
			break
		
		tlst=[]
		tlstsencond=[]

		del tlst[:]
		del tlstsencond[:]

		tlst=line.split(',')
		
		plstdata.append(tlst[0])
		plstdata.append(tlst[1])
		plstdata.append(tlst[2])

		
		tlstsencond.append(tlst[3])
		tlstsencond.append(tlst[5])
		tlstsencond.append(tlst[4])
		tlstsencond.append(tlst[6])
		plstpoint.append(tlstsencond)

	file.close()


def Readtxt_and_tran2vocxml(psegment,pimgdep,pimgfoldername):
	global ttxtdir
	global ttxtdes
	global txmldir

	paralist=[]
	while(1):
		str1=getlistdir(ttxtdir,paralist)
		if(len(str1)>0):
				
			tbfn=os.path.basename(str1)#真实文件名
			suffix=os.path.splitext(tbfn)[1]#获取后缀
			prefix=tbfn[0:(0-len(suffix))]#获得前缀
			
			print '**********************************************start'
			print str1+'  '+tbfn+'   '+suffix+'   '+prefix
			lstlwh=[]#保存图片里的分类和宽高
			lstps=[]#保存每一行的框
			gettxtinfo(str1,lstlwh,lstps)
			print lstlwh
			print lstps
			print '**********************************************end'

			pxmlfn=txmldir+prefix+'.xml'
			pinname=lstlwh[0]
			pinseg=psegment
			pinw=lstlwh[1]
			pinh=lstlwh[2]
			pindep=pimgdep
			pinfoldername=pimgfoldername
			pintruefn=prefix+'.jpg'
			create_xml(pxmlfn,pinname,pinseg,pinw,pinh,pindep,pinfoldername,pintruefn,lstps)

			shutil.move(str1,ttxtdes+str(paralist[1]))
		if(len(str1)==0):
			break

print 'start!!!'
tseg='0'
timgdep='3'
tfoldername='finish'
Readtxt_and_tran2vocxml(tseg,timgdep,tfoldername)