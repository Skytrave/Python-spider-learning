#!/usr/bin/env python
# _* _ coding:utf-8 _*_

def change_number():#定义函数部分
	number = input('please input your phone number:')
	hiding_number=number.replace(number[3:7],'*'*4)
	print(hiding_number)

def count_login():
	global a
	password = input('please input your password:')
	if password=='123569':
		print('you are right!')
	else:
		a=a+1
		print('you are faild, please try again!')
		while a==3:
			print('you are faild 3 times, please try again later!')
			exit()
		count_login()


a=0
print('welcome to the school system')
change_number()#调用函数
count_login()

