#!/usr/bin/env python
# _* _ coding:utf-8 _*a
#for i in range(1,10):
	#print(i)

names=['xiaoming','travel']
ages=['23','24','26','78']
for name,age in zip(names,ages):
	print(name,age)
#for a in range(1,14):
#	print(a)
urls=['https://www.cnblogs.com/waltsmith/p{}-0/'.format(a) for a in range(1,14)]
for url in urls:
	s=list(url)#修改字符串为列表
	s.pop(4)#改动需要改动的单个字符
	newurl=''.join(s)#链接某些元素生成字符串
	print(newurl)
