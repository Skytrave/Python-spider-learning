#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

#html = etree.HTML('flower.html')
#result = etree.tostring(html,pretty_print=True)
#print(result)

import requests
from lxml import etree

headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

res = requests.get('https://book.douban.com/top250',headers=headers)
html = etree.HTML(res.text)
result = etree.tostring(html)
print(result)