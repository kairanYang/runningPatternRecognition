#-*- coding:utf-8 -*-  
from xml.etree import ElementTree  
def print_node(node):  
	'''''打印结点基本信息'''  
	print "=============================================="  
	print "node.attrib:%s" % node.attrib  
	#if node.attrib.has_key("x1") > 0 :  
	#	print "node.attrib['x1']:%s" % node.attrib['x1']  
	print "node.tag:%s" % node.tag  
	#print "node.text:%s" % node.text  
def print_nodegf(node,index):  
	'''''打印结点基本信息'''  
	print "==============================================%d" % index 
	print "node.attrib:%s" % node.attrib  
	
	print "node.tag:%s" % node.tag  
	
	if node.attrib.has_key("x1") > 0 :  
		print "node.attrib['x1']:%s" % node.attrib['x1']  
		
	if node.attrib.has_key("y1") > 0 :  
		print "node.attrib['y1']:%s" % node.attrib['y1']  
		
	if node.attrib.has_key("x2") > 0 :  
		print "node.attrib['x2']:%s" % node.attrib['x2']  
		
	if node.attrib.has_key("y2") > 0 :  
		print "node.attrib['y2']:%s" % node.attrib['y2']  
	print "node.text:%s" % node.text 
def read_xml(text,resultlist):
	del resultlist[:]  
	'''''读xml文件'''  
	# 加载XML文件（2种方法,一是加载指定字符串，二是加载指定文件)
	# root = ElementTree.parse(r"D:/test.xml")
	root = ElementTree.fromstring(text)
	# 获取element的方法
	# 1 通过getiterator 拿到annotation
	lst_node = root.getiterator("annotation")
	#for node in lst_node:
	#print_node(node)
		  
	# 2通过 getchildren 直接拿到object
	lst_node_child = lst_node[0].getiterator("object")
	#print_node(lst_node_child)
	
	tname=''
	for nodet in lst_node_child:
		nc = nodet.getchildren()
		for child in nc:
			print '-----',child.tag		
			if(child.tag=='name'):
				tname=child.text
			if(child.tag=='bndbox'):
				tlist=[]			
				lstend=child.getchildren()
				for each in lstend:
					tlist.append(each.text)
				tlist.append(tname)
				resultlist.append(tlist)
	print resultlist

if __name__ == '__main__':
	tlst=[]
	read_xml(open("./des.xml").read(),tlst)
	#print tlst
