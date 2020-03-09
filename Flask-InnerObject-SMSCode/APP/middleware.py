# -*- coding:utf-8 -*-
# @Time : 2020/3/8 13:40
# @Author : Bravezhangw
# @File : middleware.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import g, render_template


def load_middleware(app):

	@app.before_request
	def before():
		g.username = "Alice"
		print("app before request")
		'''
			统计
			优先级
			反爬
				频率
			用户认证
			用户权限
		'''
	@app.after_request
	def after(resp):
		print("app after request")
		return resp  # 必须返回

	@app.errorhandler(404)
	def not_found(error):
		return render_template('error.html'), 404
