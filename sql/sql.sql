
--插入设备规格参数
INSERT INTO `ihome_city` (`id`, `name`) VALUES (1, '杭州市'),(2, '海宁市');

-- 地区信息
INSERT INTO `ihome_area` (`id`, `name`, `city_id`) VALUES (1, '余杭区', 1),(2, '萧山区', 1);

--  街道
INSERT INTO `ihome_street` (`id`, `name`, `area_id`) VALUES (1, '南苑', 1),(2, '东湖', 1);


INSERT INTO `ihome_village` (`id`, `name`,`other`,`street_id`) VALUES (1, '天万', '',1);
-- 设施信息
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
