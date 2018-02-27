#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
import requests
import re
import time
                                    #导入库文件
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}                                   #加入请求头
f=open('F:/resource/文件/斗破苍穹/斗破苍穹.txt','a+')  #新建TXT文档，追加方式
def get_info(url):                                  #定义获取信息的函数
	res=requests.get(url,headers=headers)
	if res.status_code==200:  #请求码200     成功处理了请求，一般情况下都是返回此状态码；
		contents=re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
		for content in contents:
			f.write(content+'\n')#正则获取数据写入TXT文件中
	else:
		pass#不为200就PASS掉
if __name__ =='__main__':
	urls=['http://www.doupoxs.com/doupocangqiong/{}.html'.format(str(i)) for i in range(2,1665)]#构造多页URL
	for url in urls:
		get_info(url)  #循环调用get_info函数
		time.sleep(1)  #休息1秒
f.close()               #关闭文件
