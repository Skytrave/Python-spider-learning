#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
import requests
import csv
from lxml import  etree
fp=open('G:/PY/Pc pratice/Python-spider-learning/豆瓣TOP250.CSV','wt',newline='',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(('name','url','author','publisher','date','price','rate','comment'))

urls=['https://book.douban.com/top250?start={}'.format(str(i)) for i in range (0,250,25)]

headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

for url in urls:
	html=requests.get(url,headers=headers)
	selector=etree.HTML(html.text)
	infos=selector.xpath('//tr[@class="item"]')
	for info in infos:
		name=info.xpath('td[2]/div[1]/a/@title')[0]
		url=info.xpath('td[2]/div[1]/a/@href')[0]
		book_info=info.xpath('td[2]/p[1]/text()')[0]
		author=book_info.split('/')[0]#字符串分为列表
		publisher=book_info.split('/')[-3]
		date=book_info.split('/')[-2]
		price=book_info.split('/')[-1]
		rate=info.xpath('td[2]/div[2]/span[2]/text()')[0]
		comments=info.xpath('td[2]/p[2]/span/text()')
		comment=comments[0] if len(comments)  != 0 else "空"
		writer.writerow((name,url,author,publisher,date,price,rate,comment))

fp.close()