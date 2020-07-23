# -*- coding: utf-8 -*-
# @Time    : 2018/10/15 11:32
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : user_views.py
# @Software: PyCharm
import os
import random
import re

from flask import Blueprint, render_template, request, session, jsonify

from app.models import db, User
from utils import status_code
from utils.config import Config
from utils.funtions import is_login

user_blueprint = Blueprint('user', __name__)


'''
创建数据表
'''
@user_blueprint.route('/create_db/', methods=['GET'])
def create_db():
    db.create_all()
    return '创建成功'

@user_blueprint.route('/drop_db/', methods=['GET'])
def drop_db():
    db.drop_all()
    return '删除数据库成功'

'''
生成验证码
'''
@user_blueprint.route('/get_code/', methods=['GET'])
def get_code():
    code = ''
    s = '1234567890qwertyuiopasdfghjklzxcvbnm'
    for i in range(4):
        code += random.choice(s)
    session['code'] = code
    return jsonify(code=200, msg='请求成功', data=code)


'''
注册
'''
@user_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        """
        跳转至注册页面
        """
        return render_template('register.html')

    if request.method == 'POST':
        """
        注册用户
        """
        mobile = request.form.get('mobile')
        imageCode = request.form.get('imageCode')
        password = request.form.get('password')
        password2 = request.form.get('password2')

        # 效验参数完整
        if not all([mobile, imageCode, password, password2]):
            return jsonify(status_code.USER_NOT_ALL)
        # 效验手机号是否合法
        if not re.match(r'^1[3456789]\d{9}$', mobile):
            return jsonify(status_code.USER_MOBILE_ERROR)
        # 效验验证码是否正确
        if session.get('code') != imageCode:
            return jsonify(status_code.USER_IMAGECODE_ERROR)
        # 效验密码一致性
        if password != password2:
            return jsonify(status_code.USER_PASSWORD_ERROR)
        # 效验用户是否已存在
        if User.query.filter(User.phone == mobile).count():
            return jsonify(status_code.USER_ERROR)
        # 创建用户信息
        user = User()
        user.phone = mobile
        user.password = password
        user.name = mobile
        try:
            user.add_update()
            return jsonify(status_code.SUCCESS)
        except:
            return jsonify(status_code.DATABASE_ERROR)


'''
登录
'''
@user_blueprint.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        """
        跳转至登录界面
        """
        return render_template('login.html')

    if request.method == 'POST':
        """
        登录验证
        """
        mobile = request.form.get('mobile')
        password = request.form.get('password')
        # 效验信息完整
        if not all([password, mobile]):
            return jsonify(status_code.USER_NOT_ALL)
        # 效验手机号是否合法
        if not re.match(r'^1[3456789]\d{9}$', mobile):
            return jsonify(status_code.USER_MOBILE_ERROR)
        user = User.query.filter(User.phone == mobile).first()
        # 效验用户是否存在
        if user:
            if user.check_pwd(password):
                # 效验密码是否正确
                session['user_id'] = user.id
                return jsonify(status_code.SUCCESS)
            else:
                return jsonify(status_code.USER_PASSWORD_ERROR)
        else:
            return jsonify(status_code.USER_ERROR)


'''
退出
'''
@user_blueprint.route('/logout/', methods=['DELETE'])
@is_login
def user_logout():
    session.clear()
    return jsonify(status_code.SUCCESS)


'''
登录之后进入用户首页
'''
@user_blueprint.route('/my/')
@is_login
def my():
    return render_template('my.html')


'''
修改用户信息
'''
@user_blueprint.route('/profile/', methods=['GET', 'PUT'])
@is_login
def profile():
    if request.method == 'GET':
        """
        跳转至修改用户信息界面
        """
        return render_template('profile.html')
    if request.method == 'PUT':
        """
        处理用户提出的修改请求
        """
        name = request.form.get('name')
        avatar = request.files.get('avatar')
        if avatar:
            try:
                # mime-type:国际规范，表示文件的类型，如text/html,text/xml,image/png,image/jpeg..
                if not re.match('image/.*', avatar.mimetype):
                    return jsonify(status_code.USER_PROFILE_IMAGE_UPDATE_ERROR)
            except:
                return jsonify(code=status_code.PARAMS_ERROR)
            # 保存到media中
            con = Config()
            url = os.path.join(con.UPLOAD_FOLDER, avatar.filename)
            avatar.save(url)
            # 保存用户的头像信息
            try:
                user = User.query.get(session['user_id'])
                user.avatar = os.path.join('/static/upload', avatar.filename)
                user.add_update()
            except:
                return jsonify(status_code.DATABASE_ERROR)
            # 返回图片信息
            return jsonify(code='200', url=os.path.join('/static/upload', avatar.filename))
        elif name:
            # 判断用户名是否存在
            if User.query.filter_by(name=name).count():
                return jsonify(status_code.USER_REGISTER_USER_IS_EXSITS)
            else:
                user = User.query.get(session['user_id'])
                user.name = name
                user.add_update()
                return jsonify(status_code.SUCCESS)
        else:
            return jsonify(status_code.PARAMS_ERROR)


'''
返回用户数据
'''
@user_blueprint.route('/user/')
@is_login
def get_user_profile():
    """
    返回用户数据
    :return: 数据库中当前用户信息
    """
    # 获取当前登录的用户
    user_id = session['user_id']
    # 查询当前用户的头像、用户名、手机号，并返回
    user = User.query.get(user_id)
    return jsonify(user=user.to_basic_dict())


'''
展示实名认证的界面
'''
@user_blueprint.route('/auth/')
@is_login
def auth():
    return render_template('auth.html')


'''
实名认证
'''
@user_blueprint.route('/auths/', methods=['GET', 'PUT'])
@is_login
def auth_info():
    if request.method == 'GET':
        """
        返回认证信息
        """
        # 获取当前登录用户的编号
        user_id = session['user_id']
        # 根据编号查询当前用户
        user = User.query.get(user_id)
        # 返回用户的真实姓名、身份证号
        return jsonify(user.to_auth_dict())

    if request.method == 'PUT':
        """
        处理认证请求
        """
        id_name = request.form.get('id_name')
        id_card = request.form.get('id_card')
        # 验证参数完整性
        if not all([id_card, id_name]):
            return jsonify(status_code.PARAMS_ERROR)
        # 验证身份证号合法
        if not re.match(r'^[1-9]\d{17}$', id_card):
            return jsonify(status_code.USER_REGISTER_AUTH_ERROR)
        # 修改数据对象
        try:
            user = User.query.get(session['user_id'])
        except:
            return jsonify(status_code.DATABASE_ERROR)

        try:
            user.id_card = id_card
            user.id_name = id_name
            user.add_update()
        except:
            return jsonify(status_code.DATABASE_ERROR)
        # 返回数据
        return jsonify(status_code.SUCCESS)


