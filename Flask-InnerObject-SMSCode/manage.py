# -*- coding:utf-8 -*-
# @Time : 2020/3/8 12:47
# @Author : Bravezhangw
# @File : manage.py.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com
import os

from flask_script import Manager
from flask_migrate import MigrateCommand

from APP import create_app
env = os.environ.get("FLASK_ENV","develop")
app = create_app(env)
manager = Manager(app)
manager.add_command("db",MigrateCommand)

if __name__ == '__main__':
    manager.run()