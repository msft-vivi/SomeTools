# -*- coding:utf-8 -*-
# @Time : 2020/3/8 13:02
# @Author : Bravezhangw
# @File : models.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from datetime import datetime

from werkzeug.security import check_password_hash, generate_password_hash

from APP.exts import db


class News(db.Model):
	__tablename__ = "news"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True,unique=True)
	n_title = db.Column(db.String(32),nullable=True)
	n_content = db.Column(db.String(256))

class Student(db.Model):
	__tablename__ = "student"
	id = db.Column(db.Integer,primary_key=True,autoincrement=True)
	s_name = db.Column(db.String(16),unique=True)
	_s_password = db.Column(db.String(256),nullable=True)
	s_phone = db.Column(db.String(32),unique=True)
	@property
	def s_password(self):
		raise Exception("Error Action : password can't be access.")

	@s_password.setter
	def s_password(self,value):
		self._s_password = generate_password_hash(value)

	def check_password(self,password):
		return check_password_hash(self._s_password,password)

