图片放在ready目录下

1.标记图片
	a.运行mark.py文件，
	b.选择标记类型，有a，b,c,d,e,f几种对应各自按键
	c.选择类型后用鼠标画框，按W写对应的txt文件，按x丢弃当前的选择框，按ESC进入下一张图
	d.处理过的图片会转移到finish目录

2.生成xml文件
	a.运行converttxt2voc.py
	b.根据txt目录下的txt类型文件在xml目录下生成同名的xml文件
	c.处理过的txt文件会转移到txtdes目录

3.检查标记是否正确
	a.运行checkxml.py文件
	b.查看标记结果，按a表示标记正确，b表示错误，esc表示跳过
	c.正确的图片放到checked目录，错误的放到error目录
