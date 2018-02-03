#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
from bs4 import BeautifulSoup
import requests
import time #导入相应的库
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}#伪装浏览器请求头
def get_info(url):
	wb_data=requests.get(url,headers=headers)
	soup=BeautifulSoup(wb_data.text,'lxml')
	ranks = soup.select('div.pc_temp_songlist > ul > li > span.pc_temp_num')
	titles=soup.select('div.pc_temp_songlist > ul > li > a')
	times=soup.select('div.pc_temp_songlist > ul > li > span.pc_temp_tips_r > span')
	for rank,title,time in zip(ranks,titles,times):
		data={
			'rank': rank.get_text().strip(),
			'song':title.get_text().split('-')[1],#通过split对title进行字符切片。[]选取第n个切片
			'singer': title.get_text().split('-')[0],
			'time':time.get_text().strip()
		}#获取信息并通过字典的信息打印
		print(data)
if __name__=='__main__':#程序主入口
	urls=['http://www.kugou.com/yy/rank/home/{}-8888.html?from=homepage'.format(number) for number in range(1,24)]#构造多页url
	for url in urls:
		get_info(url)#循环调用get_info()函数
	time.sleep(2)#睡眠2秒