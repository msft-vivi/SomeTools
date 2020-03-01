# -*- coding:utf-8 -*-
# @Time : 2020/3/1 17:37
# @Author : TianWei
# @File : third_blue.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from flask import Blueprint

bp3 = Blueprint("blue3",__name__,url_prefix="/bp3")

@bp3.route("/index")
def index():
	return "third bp"