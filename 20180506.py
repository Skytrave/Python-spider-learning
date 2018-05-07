#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36}
import pymongo
client =pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
test = mydb['test']
test.insert_one({'name':'sky','sex':'sex','grade':'24'})
