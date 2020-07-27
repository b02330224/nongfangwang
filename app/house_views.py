# -*- coding: utf-8 -*-
# @Time    : 2018/10/16 20:11
# @Author  : G.Hope
# @Email   : 1638327522@qq.com
# @File    : house_views.py
# @Software: PyCharm
import os

from flask import Blueprint, render_template, request, session, jsonify

from app.models import User, House, Facility, Area, HouseImage, Order
from utils import status_code
from utils.config import Config
from utils.funtions import is_login

house_blueprint = Blueprint('house', __name__)


@house_blueprint.route('/my_house/', methods=['GET', 'POST'])
def my_house():
    if request.method == 'GET':
        return render_template('myhouse.html')


@house_blueprint.route('/my_auth/')
def my_auth():
    """
    验证当前用户是否完成实名认证
    """
    user_id = session['user_id']
    user = User.query.get(user_id)
    if user.id_name:
        # 已经完成实名认证，查询当前用户的房屋信息
        house_list = House.query.filter(House.user_id == user_id).order_by(House.id.desc())
        house_list2 = []
        for house in house_list:
            house_list2.append(house.to_dict())
        return jsonify(code='200', hlist=house_list2)
    else:
        # 没有完成实名认证
        return jsonify(status_code.MYHOUSE_USER_IS_NOT_AUTH)


@house_blueprint.route('/area_facility/')
def area_facility():
    # 查询地址
    area_list = Area.query.all()
    area_dict_list = [area.to_dict() for area in area_list]
    # 查询设施
    facility_list = Facility.query.all()
    facility_dict_list = [facility.to_dict() for facility in facility_list]
    # 构造结果并返回
    return jsonify(area=area_dict_list, facility=facility_dict_list)


@house_blueprint.route('/add/', methods=['GET', 'POST'])
@is_login
def new_house():
    if request.method == 'GET':
        return render_template('newhouse.html')

    if request.method == 'POST':
        # 接收用户信息
        params = request.form.to_dict()
        facility_ids = request.form.getlist('facility')

        # 创建用户信息
        house = House()
        house.user_id = session['user_id']
        house.title = params.get('title')
        house.city = params.get('city')
        house.area = params.get('area')
        house.street = params.get('street')
        house.village = params.get('village')
        house.address = params.get('address')
        house.price = params.get('price')
        house.room_count = params.get('room_count')
        house.acreage = params.get('acreage')
        house.unit = params.get('unit')
        house.direction = params.get('direction')
        total_floor = params.get('total-floor')
        house.floor = params.get('floor') + '/' + total_floor
        house.desc = params.get('desc')
        house.have_cook_bath = True if params.get('cook-bath-room')== 'single' else False

        # 根据设施的编号查询设施对象
        if facility_ids:
            facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
            house.facilities = facility_list
        house.add_update()
        # 返回结果
        return jsonify(code='200', house_id=house.id)



@house_blueprint.route('/edit/<int:id>', methods=['GET', 'POST'])
@is_login
def edit_house(id):
    if request.method == 'GET':
        return render_template('newhouse.html',id=id)

    if request.method == 'POST':
        # 接收用户信息
        params = request.form.to_dict()
        facility_ids = request.form.getlist('facility')

        # 创建用户信息
        house = House.query.get(id)
        house.user_id = session['user_id']
        house.title = params.get('title')
        house.city = params.get('city')
        house.area = params.get('area')
        house.street = params.get('street')
        house.village = params.get('village')
        house.address = params.get('address')
        house.price = params.get('price')
        house.room_count = params.get('room_count')
        house.acreage = params.get('acreage')
        house.unit = params.get('unit')
        house.direction = params.get('direction')
        total_floor = params.get('total-floor')
        house.floor = params.get('floor') + '/' + total_floor
        house.desc = params.get('desc')
        house.have_cook_bath = True if params.get('cook-bath-room') == 'single' else False

        # 根据设施的编号查询设施对象
        if facility_ids:
            facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
            house.facilities = facility_list
        house.add_update()
        # 返回结果
        return jsonify(code='200', house_id=house.id)



@house_blueprint.route('/image_house/', methods=['POST'])
def image_house():
    if request.method == 'POST':
        # 接收房屋编号
        house_id = request.form.get('house_id')
        # 接收图片信息
        f1 = request.files.get('house_image')
        # 保存到图片
        con = Config()
        url = os.path.join(os.path.join(con.UPLOAD_FOLDER, 'house'), f1.filename)
        f1.save(url)

        # 保存图片对象
        image = HouseImage()
        image.house_id = house_id
        image.url = os.path.join('/static/upload/house', f1.filename)
        image.add_update()
        # 房屋的默认图片
        house = House.query.get(house_id)
        if not house.index_image_url:
            house.index_image_url = os.path.join('/static/upload/house', f1.filename)
            house.add_update()
        # 返回图片信息
        return jsonify(code='200', url=os.path.join('/static/upload/house', f1.filename))


@house_blueprint.route('/detail/')
def detail():
    return render_template('detail.html')


@house_blueprint.route('/detail/<int:id>/')
def house_detail(id):
    # 查询房屋信息
    house = House.query.get(id)
    # 查询设施信息
    facility_list = house.facilities
    facility_dict_list = [facility.to_dict() for facility in facility_list]
    # 判断当前房屋信息是否为当前登录的用户发布，如果是则不显示预订按钮
    booking = 1
    if 'user_id' in session:
        if house.user_id == session['user_id']:
            booking = 0

    return jsonify(house=house.to_full_dict(), facility_list=facility_dict_list, booking=booking)


'''
首页展示
'''


@house_blueprint.route('/index/')
@house_blueprint.route('/')
def house():
    print('house index')
    return render_template('houselist.html')


'''
查询数据库中当前用户数据
'''


@house_blueprint.route('/list/', methods=['GET'])
def index():
    # 返回最新的5个房屋信息
    hlist = House.query.order_by(House.id.desc()).all()[:5]
    hlist2 = [house.to_dict() for house in hlist]
    # 查找地区信息
    area_list = Area.query.all()
    area_dict_list = [area.to_dict() for area in area_list]
    if 'user_id' in session:
        user = User.query.filter_by(id=session['user_id']).first()
        user_name = user.name
        code = status_code.OK
        return jsonify(code=code, name=user_name, hlist=hlist2, alist=area_dict_list)
    return jsonify(hlist=hlist2, alist=area_dict_list)


'''
房间预约
'''


@house_blueprint.route('/booking/')
def booking():
    return render_template('booking.html')


'''
房间预约,房屋详细信息获取
'''


@house_blueprint.route('/get_booking_by_id/<int:id>/')
def get_booking_by_id(id):
    house = House.query.get(id)
    return jsonify(house=house.to_dict())


'''
搜索界面
'''


@house_blueprint.route('/search/', methods=['GET'])
def search():
    return render_template('search.html')


'''
搜索功能
'''


@house_blueprint.route('/my_search/', methods=['GET'])
def my_search():
    # 先获取区域id，订单开始时间，结束时间
    aid = request.args.get('aid')
    sd = request.args.get('sd')
    ed = request.args.get('ed')
    sk = request.args.get('sk')
    # 获取某个区域的房屋信息
    houses = House.query.filter(House.area_id == aid)
    # 订单的三种情况，查询出的房屋都不能展示
    order1 = Order.query.filter(Order.end_date >= ed, Order.begin_date <= ed)
    order2 = Order.query.filter(Order.begin_date <= sd, Order.end_date >= sd)
    order3 = Order.query.filter(Order.begin_date >= sd, Order.end_date <= ed)
    house1 = [order.house_id for order in order1]
    house2 = [order.house_id for order in order2]
    house3 = [order.house_id for order in order3]
    # 去重
    not_show_house_id = list(set(house1 + house2 + house3))
    # 最终展示的房屋信息
    houses = houses.filter(House.id.notin_(not_show_house_id))
    # 排序
    if sk == 'new':
        houses = houses.order_by('-id')
    elif sk == 'booking':
        houses = houses.order_by('-order_count')
    elif sk == 'price-inc':
        houses = houses.order_by('price')
    elif sk == 'price-des':
        houses = houses.order_by('-price')

    house_info = [house.to_dict() for house in houses]
    return jsonify(code=status_code.OK, house_info=house_info)
