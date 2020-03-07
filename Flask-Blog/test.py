# -*- coding:utf-8 -*-
# @Time : 2020/3/4 12:20
# @Author : Bravezhangw
# @File : test.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask import current_app

from APP.exts import db
title = "tt"
body = "bbbb"
id = 4
sql = "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",(title, body, id)

# db.session.execute(sql, bind=db.get_engine(current_app,bind='bindname'))
