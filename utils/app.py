# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 15:07
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : app.py
# @Software: PyCharm
from flask import Flask

from app.house_views import house_blueprint
from app.factory_views import factory_blueprint
from app.order_views import order_blueprint
from app.user_views import user_blueprint
from utils.config import Config
from utils.funtions import init_ext
from utils.setting import static_dir,template_dir


def create_app():

    app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

    # 注册蓝图
    app.register_blueprint(blueprint=user_blueprint, url_prefix='/user')
    app.register_blueprint(blueprint=house_blueprint, url_prefix='/house')
    app.register_blueprint(blueprint=factory_blueprint, url_prefix='/factory')
    app.register_blueprint(blueprint=order_blueprint, url_prefix='/order')

    # 配置
    app.config.from_object(Config)
    app.debug = True

    # 初始化第三方库
    init_ext(app)

    return app