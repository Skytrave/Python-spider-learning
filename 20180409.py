#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
import requests
from lxml import etree

urls=['http://www.meizitu.com/a/{}.html'.format(str(i)) for i in range(3526,3527)]
path='G:/picture/'

header={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
def get_photo(url):
	html=requests.get(url)
	selector=etree.HTML(html.text)
	photo_urls=selector.xpath('//div[@id="picture"]/p/@src')
	for photo_url in photo_urls:
		data=requests.get('http:'+photo_url,headers=header)
		fp=open(path + photo_url[-10:],'wb')
		fp.write(data.content)
		fp.close()

for url in urls:
	get_photo(url)