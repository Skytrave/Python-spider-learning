#!/usr/bin/env python
# _* _ coding:utf-8 _*_
#{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
import json
jsonstring='{"user_man":[{"name":"peter"},{"name":"xiaoming"}],'\
	       '"user_woman":[{"name":"anni"},{"name":"zhangsan"}]}'
json_data=json.loads(jsonstring)
print(json_data["user_man"])
print(json_data["user_woman"])
print(json_data["user_man"][0]["name"])
print(json_data["user_woman"][1]["name"])