#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
import xlwt
#book=xlwt.Workbook(encoding='utf-8')
#sheet=book.add_sheet('sheet1')
#sheet.write(0,0,'python')
#sheet.write(1,1,'love')
#book.save('test.xls')
import requests
from lxml import etree
import time
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
urls=['https://www.qidian.com/all?&page={}'.format(str(i)) for i in range(1,10)]
all_info_list=[]
def get_info(url):
	html=requests.get(url)
	selector=etree.HTML(html.text)
	infos=selector.xpath('//div[@class="book-mid-info"]')

	for info in infos:
		title=info.xpath('h4/a/text()')[0]
		author=info.xpath('p[1]/a[1]/text()')[0]
		style_1=info.xpath('p[1]/a[2]/text()')[0]
		style_2=info.xpath('p[1]/a[3]/text()')[0]
		style=style_1+'.'+style_2
		complete=info.xpath('p[1]/span/text()')[0]
		introduce=info.xpath('p[2]/text()')[0].strip()
		word=info.xpath('p[3]/span/text()')[0].strip()
		info_list=[title,author,style,complete,introduce,word]
		all_info_list.append(info_list)
	time.sleep(1)

if __name__ == '__main__':
	for url in urls:
		get_info(url)
	header=['title','author','style','complete','introduce','word']
	book=xlwt.Workbook(encoding='utf-8')
	sheet=book.add_sheet('起点中文网全部作品')
	for h in range(len(header)):
		sheet.write(0,h,header[h])
	i=1
	for list in all_info_list:
		j=0
		for data in list:
			sheet.write(i,j,data)
			j +=1
		i +=1
book.save('起点中文网全部作品.xlsx')


