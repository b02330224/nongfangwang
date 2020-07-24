# -*- coding: utf-8 -*-
import os

from flask import Blueprint, render_template, request, session, jsonify
from app.models import User, Facility, FactoryImage, Village, Factory, Street, City, Area
from utils import status_code
from utils.funtions import is_login
from utils.config import Config


factory_blueprint = Blueprint('factory', __name__)

'''
首页展示
'''
@factory_blueprint.route('/')
def factoryList():
    return render_template('factorylist.html')

@factory_blueprint.route('/index/')
def factory():
    print('factrotu index')
    return render_template('factory_index.html')


'''
查询数据库中当前用户数据, 最新发布的厂房信息及街道信息
'''


@factory_blueprint.route('/list/', methods=['GET'])
def index():
    # 返回最新的5个房屋信息
    flist = Factory.query.order_by(Factory.id.desc()).all()[:5]
    flist2 = [factory.to_dict() for factory in flist]
    # 查找地区信息
    street_list = Street.query.all()
    street_dict_list = [street.to_dict() for street in street_list]
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        user_name = user.name
        code = status_code.OK
        return jsonify(code=code, name=user_name, flist=flist2, slist=street_dict_list)
    return jsonify(flist=flist2, slist=street_dict_list)

@factory_blueprint.route('/citys/', methods=['GET'])
def city():
    citys = City.query.all()
    city_list = [city.to_dict() for city in citys]
    return jsonify(clist=city_list)

@factory_blueprint.route('/areas/', methods=['GET'])
def area():
    city = request.args.get('city')
    print("city={}".format(city))
    city = City.query.filter_by(name=city).first()
    areas = city.areas
    area_list = [area.to_dict() for area in areas]
    return jsonify(alist=area_list)

@factory_blueprint.route('/streets/', methods=['GET'])
def street():
    area = request.args.get('area')
    area = Area.query.filter_by(name=area).first()
    streets = area.streets
    street_list = [street.to_dict() for street in streets]
    return jsonify(slist=street_list)


@factory_blueprint.route('/villages/', methods=['GET'])
def village():
    street = request.args.get('street')
    street = Street.query.filter_by(name=street).first()
    print("street.villages={}".format(street.villages))
    villages = street.villages

    village_list = [village.to_dict() for village in villages]

    return jsonify(vlist=village_list)

@factory_blueprint.route('/search/', methods=['GET'])
def search():
    return render_template('factory_search.html')

@factory_blueprint.route('/my_factory/', methods=['GET', 'POST'])
def my_factory():
    if request.method == 'GET':
        return render_template('myfactory.html')


@factory_blueprint.route('/my_auth/')
def my_auth():
    """
    验证当前用户是否完成实名认证
    """
    user_id = session['user_id']
    user = User.query.get(user_id)
    if user.id_name:
        # 已经完成实名认证，查询当前用户的房屋信息
        factory_list = Factory.query.filter(Factory.user_id == user_id).order_by(Factory.id.desc())
        factory_list2 = []
        for factory in factory_list:
            factory_list2.append(factory.to_dict())
        return jsonify(code='200', flist=factory_list2)
    else:
        # 没有完成实名认证
        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


@factory_blueprint.route('/add/', methods=['GET', 'POST'])
@is_login
def new_factory():
    if request.method == 'GET':
        return render_template('newfactory.html')

    if request.method == 'POST':
        # 接收用户信息
        params = request.form.to_dict()
        facility_ids = request.form.getlist('facility')

        # 创建用户信息
        fac = Factory()
        fac.user_id = session['user_id']
        fac.city_id = params.get('city_id')
        fac.area_id = params.get('area_id')
        fac.street_id = params.get('street_id')
        fac.village_id = params.get('village_id')
        fac.title = params.get('title')
        fac.price = params.get('price')
        fac.content = params.get('content')
        fac.address = params.get('address')
        fac.room_count = params.get('room_count')
        fac.acreage = params.get('acreage')
        fac.unit = params.get('unit')
        fac.contact_person = params.get('contact_person')
        fac.contact_mobile = params.get('contact_mobile')

        # 根据设施的编号查询设施对象
        if facility_ids:
            facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
            fac.facilities = facility_list
        fac.add_update()
        # 返回结果
        return jsonify(code='200', factory_id=fac.id)


@factory_blueprint.route('/images/', methods=['POST'])
def factory_house():
    if request.method == 'POST':
        # 接收房屋编号
        factory_id = request.form.get('factory_id')
        # 接收图片信息
        f1 = request.files.get('factory_image')
        # 保存到图片
        con = Config()
        url = os.path.join(os.path.join(con.UPLOAD_FOLDER, 'factory'), f1.filename)
        f1.save(url)

        # 保存图片对象
        image = FactoryImage()
        image.factory_id = factory_id
        image.url = os.path.join('/static/upload/factory', f1.filename)
        image.add_update()
        # 房屋的默认图片
        factory = Factory.query.get(factory_id)
        if not factory.index_image_url:
            factory.index_image_url = os.path.join('/static/upload/factory', f1.filename)
            factory.add_update()
        # 返回图片信息
        return jsonify(code='200', url=os.path.join('/static/upload/factory', f1.filename))


@factory_blueprint.route('/area/')
def area_facility():
    # 查询地址
    area_list = Area.query.all()
    area_dict_list = [area.to_dict() for area in area_list]
    # 查询设施
    facility_list = Facility.query.all()
    facility_dict_list = [facility.to_dict() for facility in facility_list]
    # 构造结果并返回
    return jsonify(area=area_dict_list)


@factory_blueprint.route('/facility/')
def facility():

    # 查询设施
    facility_list = Facility.query.all()
    facility_dict_list = [facility.to_dict() for facility in facility_list]
    # 构造结果并返回
    return jsonify(facility=facility_dict_list)