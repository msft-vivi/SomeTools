# -*- coding:utf-8 -*-
# @Time : 2020/3/8 12:48
# @Author : Bravezhangw
# @File : __init__.py.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import Flask
from APP import config
from APP.exts import init_exts
from APP.middleware import load_middleware
from APP.views import init_views

def create_app(env):
	app = Flask(__name__)
	app.config.from_object(config.envs.get(env))
	load_middleware(app)
	init_views(app)
	init_exts(app)
	return app
