# -*- coding:utf-8 -*-
# @Time : 2020/3/1 17:32
# @Author : TianWei
# @File : second_blue.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import Blueprint

bp2 = Blueprint("blue2",__name__,url_prefix='/bp2')

@bp2.route("/index")
def index():
	return "second bp"