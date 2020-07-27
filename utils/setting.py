# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 11:19
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : setting.py
# @Software: PyCharm

import os

# 项目路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 静态文件
static_dir = os.path.join(BASE_DIR, 'static')

# 模板文件
template_dir = os.path.join(BASE_DIR, 'templates')

# 数据库配置
MYSQL_DATABASES = {
    'DRIVER': 'mysql',
    'DH': 'pymysql',
    'ROOT': 'root',
    'PASSWORD': '123456',
    'HOST': '192.168.184.202',
    'PORT': '3306',
    'NAME': 'nfw'
}

# 会话缓存配置
REDIS_DATABASES = {
    'HOST': '192.168.184.202',
    'PORT': '6379'
}

try:
    from debug_setting import *
except Exception as e:
    print(e)
