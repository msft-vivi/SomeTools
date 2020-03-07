# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:41
# @Author : Bravezhangw
# @File : views.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from .auth import bp1
from .blog import bp2

def init_views(app):
	app.register_blueprint(bp1)
	app.register_blueprint(bp2)
	app.add_url_rule('/',endpoint='blog.home')
