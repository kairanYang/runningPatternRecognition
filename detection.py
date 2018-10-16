#!/usr/bin/env python
#coding=utf-8

import os

from demo import *

filepath = '/home/gf/temp/yifu97.JPG'


'''

'''


def find_target_rewriteimage(source_path,des_path,file_index=-1):#处理单一一张图片
	
	lstresult=[]
	im_names = []
	im_names.append(source_path)
	del lstresult[:]
	y_sum=0
	num = 0

	
	timer = Timer()
	timer.tic()#计时开始
	detection(im_names,lstresult)
	timer.toc()#计时结束
	if(len(lstresult)>0):
		print "耗时"
		print ('Detection took {:.3f}s ').format(timer.total_time)
		count = len(lstresult)
		for x in lstresult:
			print x
		print '检测到的物品数量'+str(count)

		im = cv2.imread(source_path)
		if len(lstresult)>0 :
			for x in lstresult:
				if(x[5]=='98'):
					cv2.rectangle(im,((int)(x[0]),(int)(x[1])),((int)(x[2]),(int)(x[3])),(0,0,255),20)
				if(x[5]=='97'):
					cv2.rectangle(im,((int)(x[0]),(int)(x[1])),((int)(x[2]),(int)(x[3])),(0,255,0),20)
				if(x[5]=='99'):
					cv2.rectangle(im,((int)(x[0]),(int)(x[1])),((int)(x[2]),(int)(x[3])),(255,0,0),20)
		if(file_index!=-1):
			fn=('./test-{0}.jpg').format(file_index)
		else:
			fn=des_path
		print fn
		cv2.imwrite(fn,im)


def list_dir(source_img_fullpath,des_path):

	files=os.listdir(source_img_fullpath)
	for filename in files:
		portion = os.path.splitext(filename)
		if portion[1] ==".jpg":
			t_single_img_path=('{0}/{1}{2}').format(source_img_fullpath,portion[0],portion[1])
			t_des_img_path=des_path+'/'+portion[0]+portion[1]
			print portion,t_single_img_path,t_des_img_path
			find_target_rewriteimage(t_single_img_path,t_des_img_path)


#result = find_target_rewriteimage(filepath,'./gf.jpg')
list_dir('/home/gf/temp/慨然行人/checked','/home/gf/temp/慨然行人/des')
	




