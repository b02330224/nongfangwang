# -*- coding: utf-8 -*-
# @Time    : 2018/10/13 11:12
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : manager.py
# @Software: PyCharm


from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand
from app.models import db

from utils.app import create_app

# 创建app
app = create_app()

# 使用Manger管理app
manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
