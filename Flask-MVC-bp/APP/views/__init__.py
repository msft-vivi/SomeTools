# -*- coding:utf-8 -*-
# @Time : 2020/3/1 17:18
# @Author : TianWei
# @File : views.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from .first_blue import bp1
from .second_blue import bp2
from .third_blue import bp3

def init_views(app):
	app.register_blueprint(bp1)
	app.register_blueprint(bp2)
	app.register_blueprint(bp3)
