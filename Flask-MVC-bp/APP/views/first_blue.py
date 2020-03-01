# -*- coding:utf-8 -*-
# @Time : 2020/3/1 17:32
# @Author : TianWei
# @File : first_blue.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import Blueprint

bp1 = Blueprint("blue",__name__)
@bp1.route("/")
def index():
	return "first bp"
