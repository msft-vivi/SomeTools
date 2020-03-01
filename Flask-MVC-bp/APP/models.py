# -*- coding:utf-8 -*-
# @Time : 2020/3/1 17:18
# @Author : TianWei
# @File : models.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from APP.exts import db

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def save(self):
		db.session.add(self)
		db.session.commit()

class Student(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	#
	# def __repr__(self):
	# 	return '<User %r>' % self.username

class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)

