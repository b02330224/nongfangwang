# -*- coding: utf-8 -*-
import os

from flask import Blueprint, render_template, request, session, jsonify
from app.models import User, Facility, FactoryImage, Village, Factory, Street, City, Area
from utils import status_code


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


@factory_blueprint.route('/findex/', methods=['GET'])
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


@factory_blueprint.route('/new_factory/', methods=['GET', 'POST'])
def new_house():
    if request.method == 'GET':
        return render_template('newfactory.html')

    if request.method == 'POST':
        # 接收用户信息
        params = request.form.to_dict()
        facility_ids = request.form.getlist('facility')

        # 创建用户信息
        fac = Factory()
        fac.user_id = session['user_id']
        fac.area_id = params.get('area_id')
        fac.title = params.get('title')
        fac.price = params.get('price')
        fac.address = params.get('address')
        fac.room_count = params.get('room_count')
        fac.acreage = params.get('acreage')
        fac.beds = params.get('beds')
        fac.unit = params.get('unit')
        fac.capacity = params.get('capacity')
        fac.deposit = params.get('deposit')

        # 根据设施的编号查询设施对象
        if facility_ids:
            facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
            fac.facilities = facility_list
        fac.add_update()
        # 返回结果
        return jsonify(code='200', house_id=fac.id)


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