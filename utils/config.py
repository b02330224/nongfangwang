# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 11:09
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : config.py
# @Software: PyCharm
import os
import redis

from utils.setting import BASE_DIR
from utils.funtions import get_mysqldb_url,get_redis_url


class Config():

    SECRET_KEY = 'secret_key'

    # 配置数据库
    SQLALCHEMY_DATABASE_URI = get_mysqldb_url()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # session的配置
    SESSION_TYPE = 'redis'
    SESSION_REDIS = get_redis_url()

    # 上传图片地址
    UPLOAD_FOLDER = os.path.join(os.path.join(BASE_DIR, 'static'), 'upload')
