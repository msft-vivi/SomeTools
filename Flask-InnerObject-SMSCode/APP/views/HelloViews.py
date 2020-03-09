# -*- coding:utf-8 -*-
# @Time : 2020/3/8 12:53
# @Author : Bravezhangw
# @File : HelloViews.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from flask import Blueprint, request, g, abort, render_template, current_app, redirect, url_for, flash, jsonify
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash

from APP.exts import db, mail, cache
from APP.models import Student
from APP.utils import send_verify_code

bp1 = Blueprint("blue",__name__)


@bp1.route("/student_register/",methods=['POST','GET'])
def student_register():
	if request.method == 'GET':
		return render_template('student_register.html')
	elif request.method == 'POST':
		username = request.form.get('username')
		phone = request.form.get("phone")
		password = request.form.get('password')
		code = request.form.get("code")
		cached_code = cache.get(username) # 从缓存取平台收到的验证码

		if cached_code != code:
			return "验证失败"
		else:
			student = Student()
			student.s_name = username
			student.s_password = password # 可以设置，但是不可以单独访问
			student.s_phone = phone
			db.session.add(student)
			db.session.commit()
			return redirect(url_for('blue.student_login'))

@bp1.route("/student_login/",methods=['POST','GET'])
def student_login():
	if request.method == 'GET':
		return render_template('student_login.html')
	elif request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		student = get_user_by_name(username)
		error = None
		if student:
			if not student.check_password(password):
				error = "Password does correct."
		else:
			error = "Username does exist."

		if error is None:
			return "Login Success"
		flash(error)

		return render_template("student_login.html")


@bp1.route("/sendmail/")
def send_mail():
	msg = Message("Hello, zhangw",recipients=['bravezhangw@163.com'])
	msg.body = "哈哈哈"
	msg.html = render_template("mail.html") # 可以自己选人模板 发送
	mail.send(msg)
	return "邮件发送成功"

# 发送短信
@bp1.route("/sendcode/")
def send_code():
	phone = request.args.get("phone")
	username = request.args.get("username")

	response = send_verify_code(phone)
	res = response.json()
	if res.get("code") == 200:
		obj = res.get("obj") # 获取验证码
		cache.set(username,obj) # 缓存该用户的验证码
		data = {
			"msg":"ok",
			"status":200
		}
		return jsonify(data)
	data = {
		"msg":"fail",
		"status":400
	}
	return jsonify(data)


def get_user_by_name(username):
	student = Student.query.filter(Student.s_name.__eq__(username)).first()
	if student:
		return student
	else:
		return None


@bp1.route("/")
def index():
	return "Hi~ %s" % (g.username)

@bp1.route("/config/")
def config():
	return render_template('news.html')


@bp1.before_request
def before():
	print("before request : ",request.url)
	config = current_app.config
	for key, v in config.items():
		print(key , v)

@bp1.route("/error/")
def error():
	abort(404)

