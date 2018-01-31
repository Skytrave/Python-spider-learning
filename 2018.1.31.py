#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
from bs4 import BeautifulSoup
import requests
import time #导入相应的库
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
}#伪装浏览器请求头
def judgment_sex(class_name):
	if class_name ==['member_ico']:
		return '男'
	else：
		return '女'#定义判断性别函数
def get_links(url):
	wb_data=requests.get(url,headers=headers)
	soup=BeautifulSoup(wb_data.text,'lxml')

