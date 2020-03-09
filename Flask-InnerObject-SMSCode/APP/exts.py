# -*- coding:utf-8 -*-
# @Time : 2020/3/8 12:48
# @Author : Bravezhangw
# @File : exts.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache(config={'CACHE_TYPE': 'simple',"CACHE_DEFAULT_TIMEOUT": 300})

def init_exts(app):
	db.init_app(app)
	migrate.init_app(app,db)
	mail.init_app(app)
	cache.init_app(app)

