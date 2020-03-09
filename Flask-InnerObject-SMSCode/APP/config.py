# -*- coding:utf-8 -*-
# @Time : 2020/3/8 12:49
# @Author : Bravezhangw
# @File : config.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_db_uri(db_info):
    engine = db_info.get("ENGINE") or "sqlite"
    driver = db_info.get("DRIVER") or "sqlite"
    username = db_info.get("USERNAME") or ""
    password = db_info.get("PASSWORD") or ""
    host = db_info.get("HOST") or ""
    port = db_info.get("PORT") or ""
    database = db_info.get("DATABASE") or ""
    return "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(engine,driver,username,password,host,port,database)


DATABASE = "innerobj"
class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY =  b'9527'
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 25
    MAIL_USERNAME = 'bravezhangw@163.com'
    MAIL_PASSWORD = 'aa945151065' # 邮件服务器客户端授权码
    MAIL_DEFAULT_SENDER = MAIL_USERNAME
    # MAIL_USE_TLS = True
    # SESSION_TYPE = 'redis'
    # SESSION_COOKIE_SECURE = True
    # SESSION_USE_SIGNER = True 设置为True session无法读取数据？？



# 开发环境
class DevelopConfig(Config):
    DEBUG = True
    ENV = "development"
    db_info = {
        "ENGINE":"mysql",
        "DRIVER":"pymysql",
        "HOST":"127.0.0.1",
        "PORT":"3306",
        "DATABASE":DATABASE,
        "USERNAME":"root",
        "PASSWORD":"12345"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 测试环境
class TestConfig(Config):
    TESTING = True
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "DATABASE": DATABASE,
        "USERNAME": "root",
        "PASSWORD": "12345"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 演示环境
class StagingConfig(Config):
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "DATABASE": DATABASE,
        "USERNAME": "root",
        "PASSWORD": "12345"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)


# 生产环境
class ProductConfig(Config):
    ENV = "production"
    db_info = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "HOST": "127.0.0.1",
        "PORT": "3306",
        "DATABASE": DATABASE,
        "USERNAME": "root",
        "PASSWORD": "12345"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(db_info)



# 传入 app
envs = {
    "develop":DevelopConfig,
    "testing":TestConfig,
    "staging":StagingConfig,
    "product":ProductConfig,
    "default":DevelopConfig
}