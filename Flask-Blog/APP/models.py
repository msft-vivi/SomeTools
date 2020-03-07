# -*- coding:utf-8 -*-
# @Time : 2020/3/2 22:37
# @Author : Bravezhangw
# @File : models.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from APP.exts import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from sqlalchemy.sql.sqltypes import DateTime,TIMESTAMP
from sqlalchemy.sql import func

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,unique=True)
    username = db.Column(db.String(50),nullable=False)
    password = db.Column(db.String(300),nullable=False)

    def __init__(self,*args,**kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')

        self.username = username
        self.password = password


    def check_password(self,raw_password):
        result = check_password_hash(self.password,raw_password)
        return result

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False) # table_name.key
    created = db.Column(db.DateTime,default=datetime.now,onupdate=datetime.now)
    title = db.Column(db.Text,nullable=False)
    body = db.Column(db.Text,nullable=False)
    author = db.relationship('User',backref=db.backref('posts'))

    # 所有属性值都要初始化（有些有默认值的可以不显示初始化）
    def __init__(self,*args,**kwargs):
        self.author_id = kwargs.get('author_id')
        self.title = kwargs.get('title')
        self.body = kwargs.get('body')

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}