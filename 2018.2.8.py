#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'
#import re
#import requests
#a='wzzldkfjdk  sdlkfjdfk zz 3zz zzszz,sj;sdlksa;djfsdozzdsszzzz'
#info=re.findall('zz(.*?)zz',a)
#print(info)
#b='asdf2jg2jkhgjk2h3jhg3kj2g2j'
#3info1=re.findall('\d+',b)#匹配所有符合规律的内容
#print(info1)
#c='asdf2jg2jkhgjk2h3jhg3kj2g2j'
#info2=re.search('\d+',c)#提取第一个的内容
#print(info2.group())#group方法获取信息
#d='klsjdhfksa2143234hdkfhsakdfhsakdh234214312431fayuywewiubsicubsiudbw'
#nfo3=re.sub('\d+','@',d)#sub用于替换
import re
import requests
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
}
res = requests.get('http://newhouse.nb.fang.com/',headers=headers)
res.encoding="gb2312"
print(res.text)
prices = re.findall('<span>(.*?)</span><em>元/',res.text)
for price in prices:
	print(price)