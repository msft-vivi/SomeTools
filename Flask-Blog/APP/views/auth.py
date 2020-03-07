# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:41
# @Author : Bravezhangw
# @File : auth.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from flask import Blueprint, make_response, abort, request, session, g, flash, redirect
from flask import render_template,url_for,Response
from werkzeug.security import generate_password_hash, check_password_hash
from APP.models import User
from APP.exts import db

bp1 = Blueprint("auth",__name__,url_prefix="/auth")


@bp1.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        # TODO 从数据库加载这个人的信息
        g.user = User.query.filter_by(id=user_id).first()



@bp1.route("/login/",methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # print("{} : {}".format(username,password))
        error = None
        user = User.query.filter_by(username=username).first()
        if user is None:
            error = "Incorrect username."
        elif not check_password_hash(user.password, password):
            error = "Incorrect password."

        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("blog.home"))

        flash(error)
    return render_template('auth/login.html')

@bp1.route("/register/",methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        error = None
        if not username:
            error = "Username is required."
        elif not password1:
            error = "Password is required."
        elif not password2:
            error = "Repeat password is required."
        elif not (password1 == password2):
            error = "Twice password not the same"
        else:
            user = User.query.filter_by(username=username).first()
            if user is not None:
                error = "User {0} is already registered.".format(username)

        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            user = User(username=username,password=generate_password_hash(password1))
            db.session.add(user)
            db.session.commit()

            return redirect(url_for("auth.login"))

        flash(error)
    else:
        abort(401)
    return render_template('auth/register.html')


@bp1.route("/logout/")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("blog.home"))

@bp1.route('/jinja/')
def jinja():
    # title = "tt"
    # body = "bbbb"
    # id = 4
    # sql = "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)", (title, body, id)
    # db.session.excute(sql)
    # db.commit()
    users = ['小白用户{}'.format(i) for i in range(5)]
    msg = "hello world {{"
    return render_template("auth/jinja_template.html",users=users,msg=msg)
