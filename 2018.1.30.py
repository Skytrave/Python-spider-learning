#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
res=requests.get('https://bj.xiaozhu.com/',headers=headers)
soup=BeautifulSoup(res.text,'lxml')#解析返回的结果
#print(soup.prettify())
prices=soup.select('#page_list > ul > li > div.result_btm_con.lodgeunitname > span.result_price > i')
for price in prices:
	print(price.get_text())
	