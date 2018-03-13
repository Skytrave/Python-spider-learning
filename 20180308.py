#!/usr/bin/env python
# _* _ coding:utf-8 _*_
# {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537
import requests
from lxml import etree
headers={
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
url='https://www.qiushibaike.com/text/page/5/'
res=requests.get(url,headers=headers)
selector=etree.HTML(res.text)
#result=etree.tostring(selector,pretty_print=True)
#print(result)
url_infos=selector.xpath('//div[@class="article block untagged mb15"]')
#print(url_infos)
for url_info in url_infos :
	id=url_info.xpath('div[1]/a[2]/h2/text()')[0]
	print(id)
