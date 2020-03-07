# -*- coding:utf-8 -*-
# @Time : 2020/3/2 16:37
# @Author : Bravezhangw
# @File : exts.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import functools

from flask_session import Session

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import redirect, url_for, g

db = SQLAlchemy()
migrate = Migrate()
sess = Session()
def init_exts(app):
    db.init_app(app)
    migrate.init_app(app,db)
    # sess.init_app(app)


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""

    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view