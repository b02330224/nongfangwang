
--插入设备规格参数
INSERT INTO `ihome_city` (`id`, `name`) VALUES (1, '杭州市'),(2, '海宁市');

--地区信息
INSERT INTO `ihome_area` (`id`, `name`, `city_id`) VALUES (1, '余杭区', 1),(2, '萧山区', 1);

--  街道
INSERT INTO `ihome_street` (`id`, `name`, `area_id`) VALUES (1, '南苑', 1),(2, '东湖', 1);


INSERT INTO `ihome_village` (`id`, `name`,`other`,`street_id`) VALUES (1, '天万', '',1);
--设施信息
INSERT INTO `ihome_facility` VALUES (null, null, '1', '宽带网络', 'wirelessnetwork-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '2', '热水淋浴', 'shower-ico');
INSERT INTO `ihome_facility` VALUES (null, null, '3', '空调', 'aircondition-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '4', '暖气', 'heater-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '5', '允许吸烟', 'smoke-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '6', '饮水设备', 'drinking-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '7', '牙具', 'brush-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '8', '香皂', 'soap-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '9', '拖鞋', 'slippers-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '10', '手纸', 'toiletpaper-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '11', '毛巾', 'towel-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '12', '沐浴露、洗发露', 'toiletries-ico');
INSERT INTO `ihome_facility` VALUES (null, null, '13', '冰箱', 'icebox-ico');
INSERT INTO `ihome_facility` VALUES (null, null, '14', '洗衣机', 'washer-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '15', '电梯', 'elevator-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '16', '允许做饭', 'iscook-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '17', '允许带宠物', 'pet-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '18', '允许聚会', 'meet-ico');
INSERT INTO `ihome_facility` VALUES (null, null, '19', '门禁系统', 'accesssys-ico');
INSERT INTO `ihome_facility` VALUES (null, null, '20', '停车位', 'parkingspace-ico');
--INSERT INTO `ihome_facility` VALUES (null, null, '21', '有线网络', 'wirednetwork-ico');
INSERT INTO `ihome_facility` VALUES (null, null, '22', '有线电视', 'tv-ico');



INSERT INTO `alembic_version` VALUES ('c21d5c34e89d');
INSERT INTO `ihome_area` VALUES (NULL,NULL,1,'余杭区',1),(NULL,NULL,2,'萧山区',1);
INSERT INTO `ihome_city` VALUES (NULL,NULL,1,'杭州市'),(NULL,NULL,2,'海宁市');
INSERT INTO `ihome_facility` VALUES (NULL,NULL,1,'宽带网络','wirelessnetwork-ico'),(NULL,NULL,3,'空调','aircondition-ico'),(NULL,NULL,13,'冰箱','icebox-ico'),(NULL,NULL,14,'洗衣机','washer-ico'),(NULL,NULL,19,'门禁系统','accesssys-ico'),(NULL,NULL,20,'停车位','parkingspace-ico'),(NULL,NULL,22,'有线电视','tv-ico');
INSERT INTO `ihome_house` VALUES ('2020-07-27 10:41:12','2020-07-27 10:41:25',4,1,'余杭区','杭州市','南苑','天万','套房出租',500,'天万王家塘28号',3,20,'元/月','south','2/4','/static/upload/house\\风景图.jpg','',0),('2020-07-27 14:29:37','2020-07-27 14:29:37',5,1,'余杭区','杭州市','南苑','天万','套房出租',500,'天万王家塘28号',3,20,'元/月','south','2/4','','环境很好',0),('2020-07-27 14:34:58','2020-07-27 14:34:58',6,1,'余杭区','杭州市','南苑','天万','套房出租',500,'天万王家塘28号',3,20,'元/月','south','2/4','','环境很好1',0),('2020-07-27 14:36:35','2020-07-27 14:36:35',7,1,'余杭区','杭州市','南苑','天万','套房出租',500,'天万王家塘28号',3,20,'元/月','south','2/4','','环境很好12',0),('2020-07-27 14:43:09','2020-07-27 14:45:14',8,1,'余杭区','杭州市','南苑','天万','套房出租',500,'天万王家塘28号',3,20,'元/月','south','2/4','','环境很好125',0);
INSERT INTO `ihome_house_image` VALUES ('2020-07-27 10:41:25','2020-07-27 10:41:25',1,4,'/static/upload/house\\风景图.jpg');
INSERT INTO `ihome_street` VALUES (NULL,NULL,1,'南苑',1),(NULL,NULL,2,'东湖',1);
INSERT INTO `ihome_user` VALUES ('2020-07-27 10:40:10','2020-07-27 10:45:21',1,'13003196483','pbkdf2:sha256:150000$HITLXGSe$395f2e0040c3d3d7a866d0663f872055be448a2b65e479341aaa886d9b021b56','13003196483',NULL,'王建','330184198303110035');
INSERT INTO `ihome_village` VALUES (NULL,NULL,1,'天万','',1);
