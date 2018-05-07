#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36}
import pymysql
conn=pymysql.connect(host='localhost',user='root',passwd='54321xxwhxyM',db='mydb',port=3306,charset='utf8')
cursor=conn.cursor()
cursor.execute("insert into students(name,sex,grade) values (%s,%s,%s)",('张三','女',87))
conn.commit()