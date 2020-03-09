# -*- coding:utf-8 -*-
# @Time : 2020/3/8 16:02
# @Author : Bravezhangw
# @File : Property.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import hashlib


class Student:
	def __init__(self, _password=None):
		self._passwprd = _password

	'''
		property 可以让把函数变成属性
	'''
	@property
	def password(self):
		raise Exception("Error Action") # 禁止直接访问密码
		# return self._passwprd

	@password.setter
	def password(self, value):
		self._passwprd = hashlib.new("sha1", value.encode("utf-8")).hexdigest()



if __name__ == '__main__':
	student = Student()
	student.password = "110" # 允许
	print(student.password) # 禁止
