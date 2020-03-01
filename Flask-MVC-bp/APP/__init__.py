# -*- coding:utf-8 -*-
# @Time : 2020/3/1 17:18
# @Author : TianWei
# @File : __init__.py.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from flask import Flask
from APP.views import init_views
from APP.exts import init_ext
from APP.config import envs

# env 为传入的环境（testing,develpope）
def create_app(env):
	app = Flask(__name__)
	app.config.from_object(envs.get(env))
	init_views(app=app) # 初始化视图
	init_ext(app=app) # 初始化第三方库

	return app