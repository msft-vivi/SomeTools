# -*- coding:utf-8 -*-
# @Time : 2020/3/1 17:18
# @Author : TianWei
# @File : manage.py
# @Software: PyCharm
# @Organization : NJU
# @email : cleverzhangw@qq.com

from APP import create_app
from flask_migrate import MigrateCommand
from flask_script import Manager
from APP.models import User,Student


import os
env = os.environ.get("FLASK_ENV","develop") # 获取默认FLASK 环境，如果未配置，默认为develop
app = create_app(env=env)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

# TODO 必须先创建上下文，然后操作（就是告诉db，现在在哪个application下面操作，因为一次可能有多个app）
# with app.app_context():
#     db.create_all()

if __name__ == '__main__':
    manager.run()



# Q&A
'''
    Q:  RuntimeError: No application found. Either work inside a view function or push an applicati
    A:  https://blog.csdn.net/zhongqiushen/article/details/79162792
'''