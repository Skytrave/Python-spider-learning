#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
from bs4 import BeautifulSoup
import requests
import time #导入相应的库
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}#伪装浏览器请求头
def judgment_sex(class_name):
	if class_name ==['member_ico']:
		return '男'
	else:
		return '女'#定义判断性别函数
def get_links(url):
	wb_data=requests.get(url,headers=headers)
	soup=BeautifulSoup(wb_data.text,'lxml')
	links=soup.select('#page_list > ul > li > a') #获取多个详细页的链接
	for link in links:
		href=link.get("href")
		get_info(href)#获取单个详细页链接
def get_info(url):
	wb_data=requests.get(url,headers=headers)
	soup=BeautifulSoup(wb_data.text,'lxml')
	titles=soup.select('div.pho_info > h4 > em')
	addresses=soup.select('div.pho_info > p > span')
	prices=soup.select('#pricePart > div.day_l > span')
	imgs=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')
	names=soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
	sexs=soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
	for title,address,price,img,name,sex in zip(titles,addresses,prices,imgs,names,sexs):
		data={
			'title':title.get_text().strip(),
			'address':address.get_text().strip(),
			'price':price.get_text(),
			'img': img.get("src"),#src 图像文件的url
			'name': name.get_text(),
			'sex': judgment_sex(sex.get("class"))
		}#获取信息并通过字典的信息打印
	print(data)
if __name__=='__main__':#程序主入口
	urls=['https://nb.xiaozhu.com/search-duanzufang-p{}-0/'.format(number) for number in range(1,6)]
	for single_url in urls:
		get_links(single_url)#循环调用get_links()函数
		time.sleep(2)#睡眠2秒