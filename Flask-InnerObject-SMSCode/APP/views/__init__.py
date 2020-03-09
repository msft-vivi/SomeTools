# -*- coding:utf-8 -*-
# @Time : 2020/3/8 12:48
# @Author : Bravezhangw
# @File : __init__.py.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import Blueprint
from .HelloViews import bp1

def init_views(app):
	app.register_blueprint(bp1)
