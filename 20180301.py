#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
import requests
import re
                                    #导入库文件
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

info_lists=[]#初始化列表

def judgment_sex(class_name):
	if class_name=='manIcon':
		return '男'
	else:
		return '女'

def get_info(url):                                  #定义获取信息的函数
	res=requests.get(url)
	ids=re.findall('<h2>(.*?)</h2>',res.text,re.S)
	levels=re.findall('<div class="articleGender \D+Icon">(.*?)</div>',res.text,re.S)
	sexs=re.findall('<div class="articleGender (.*?)">',res.text,re.S)
	contents=re.findall('<div class="content">.*?<span>(.*?)</span>',res.text,re.S)
	laughs=re.findall('<span class="stats-vote"><i class="number">(\d+)</i> 好笑</span>',res.text,re.S)
	comments=re.findall('<i class="number">(\d+)</i> 评论',res.text,re.S)
	for id,level,sex,content,laugh,comment in zip(ids,levels,sexs,contents,laughs,comments):
		info={
			'id':id,
			'level':level,
			'sex':judgment_sex(sex),
			'content':content,
			'laugh':laugh,
			'comment':comment
		}
		info_lists.append(info)#获取数据并添加到列表中

if __name__== '__main__' :
	urls=['https://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,35)]
	for url in urls:
		get_info(url)
	for info_list in info_lists:
		f = open('F:/resource/文件/糗事百科/糗事百科.txt','a+')#遍历列表，创建TXT文件

		print(info_list)
		try:
			f.write(info_list['id'])
			f.write(info_list['level']+'\n')
			f.write(info_list['sex'])
			f.write(info_list['content'])
			f.write(info_list['laugh'])
			f.write(info_list['comment']+'\n\n')
			f.close()
		except UnicodeEncodeError:
			pass#pass掉错误编码