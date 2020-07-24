# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 10:22
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : funtions.py
# @Software: PyCharm
import functools
import redis

from flask import session
from flask_session import Session
from werkzeug.utils import redirect

from app.models import db
from utils.setting import MYSQL_DATABASES, REDIS_DATABASES

'''
初始化第三方库
'''
def init_ext(app):

    db.init_app(app)

    sess = Session()
    sess.init_app(app)

'''
装饰器（验证登录状态）
'''
def is_login(view_fun):
    @functools.wraps(view_fun)
    def decorator():
        try:
            if 'user_id' in session:
                return view_fun()
            else:
                print("session not found user_id")
                return redirect('/user/login/')
        except Exception as e:
            print("exception:{}".format(e))

    return decorator


'''
配置数据库
'''
def get_mysqldb_url():
    DRIVER = MYSQL_DATABASES['DRIVER']
    DH = MYSQL_DATABASES['DH']
    ROOT = MYSQL_DATABASES['ROOT']
    PASSWORD = MYSQL_DATABASES['PASSWORD']
    HOST = MYSQL_DATABASES['HOST']
    PORT = MYSQL_DATABASES['PORT']
    NAME = MYSQL_DATABASES['NAME']
    return '{}+{}://{}:{}@{}:{}/{}'.format(DRIVER,DH,ROOT,PASSWORD,HOST,PORT,NAME)

'''
配置缓存
'''
def get_redis_url():
    host = REDIS_DATABASES['HOST']
    port = REDIS_DATABASES['PORT']
    return redis.Redis(host=host, port=port)