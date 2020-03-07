# -*- coding:utf-8 -*-
# @Time : 2020/3/3 21:57
# @Author : Bravezhangw
# @File : db.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext
from APP.exts import db


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    if "db" not in g:
        g.db = db
    return g.db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()

