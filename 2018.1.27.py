#!/usr/bin/env python
# _* _ coding:utf-8 _*_

#	def use(self,time):
#		print('you are riding {}m'.format(time*100))

#my_bike.other='basket'
class bike:#定义类
	compose=['frame','wheel','pedal']
	def __init__(self):
		self.other='basket'#定义实例属性
	def use(self,distance):
		print('you are riding {}m'.format(distance*100))
class share_bike(bike):
	def cost(self,time):
		print('you are spent {}.format(time*2)')
my_bike=share_bike()
print(my_bike.compose)
print(my_bike.other)
my_bike.use(10)
my_bike.cost(10)
