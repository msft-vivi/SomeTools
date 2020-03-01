# -*- coding:utf-8 -*-
# @Time : 2020/3/1 20:48
# @Author : TianWei
# @File : exts.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# lazy load
db = SQLAlchemy()
migrate = Migrate()


def init_ext(app):
	db.init_app(app)
	migrate.init_app(app,db)
