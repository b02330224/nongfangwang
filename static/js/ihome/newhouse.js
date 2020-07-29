function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

function del_img(id,that) {
     $.ajax({
            url:'/house/images/'+id,
            type:'delete',
            success:function (data) {
                if(data.code== '200'){
                     console.log($(that).parent());
                    $(that).parent().remove();
                    if ($(".image_btn_cons").length <= 3) {
                        $('.upload-msg').hide()
                    }

                }else{
                    $('.error_msg2').html('<i class="fa fa-exclamation-circle"></i>' +data.msg);
                    $('.error_msg2').show();
                }
            }
        });
}


function sel_img() {
    if ($(".image_btn_cons").length >= 3) {
        console.log($(".image_btn_cons").length);

        $('.upload-msg').show().find('span').html('上传图片超过3张了！');
        return false
    }
}

$(document).ready(function(){
    //查询地区、设施信息

    var id= $('#form-house-info input[name="id"]').val()
    console.log('house id', id);
    getCitys()
    if (id!=''){
         $('.page-title').text('修改房源');
          $('input[type="submit"]').val('修改房源');
         $.get('/house/detail/'+ id,function (data) {
             console.log(data.house);
             var house = data.house;
             $('#house-title').val(house.title);
             $('#house-price').val(house.price);
             $('#house-acreage').val(house.acreage);
             $('#pre_unit').val(house.unit);
             $('#house-address').val(house.address);
             $('#house-room-count').val(house.room_count);
             $('#cook-bath-room-id').val(house.cook_bath_room);
             $('#direction-id').val(house.direction);
             var floors = house.floor.split('/')
             console.log(floors);
             $('#floor-id').val(floors[0]);
             $('#total-floor-id').val(floors[1]);
             $('#house-desc').val(house.desc);


             $('#city-id').val(house.city);
             getAreas()
             $('#area-id').val(house.area);
             getStreets()
             $('#street-id').val(house.street);
             getVillages()
             $('#village-id').val(house.village);




        });
    }

    function getCitys() {
         $.get('/factory/citys/',function (data) {
        //城市
        var city_html = '<option value="0">请选择</option>'
        for(var i=0; i<data.clist.length; i++){
            city_html += '<option value="' + data.clist[i].name+ '">' + data.clist[i].name + '</option>'
        }
        $('#city-id').html(city_html);

    });
    }



    function getAreas(){
         $.ajaxSettings.async = false;
         $.get('/factory/areas/?city='+$("#city-id").find("option:selected").text(), function(data){
            var area_html = '<option value="0">请选择</option>'
            for(var i=0; i<data.alist.length; i++){
                area_html += '<option value="' + data.alist[i].name + '">' + data.alist[i].name + '</option>'
            }
             $('#area-id').html(area_html)

              });

          $.ajaxSettings.async = true;
    }

    function getStreets() {
         $.ajaxSettings.async = false;
         $.get('/factory/streets/?area='+$("#area-id").find("option:selected").text(), function(data){
            var street_html = '<option value="0">请选择</option>'
            for(var i=0; i<data.slist.length; i++){
            street_html += '<option value="' + data.slist[i].name + '">' + data.slist[i].name + '</option>'
        }
         $('#street-id').html(street_html)

          });

          $.ajaxSettings.async = true;
    }

    function getVillages() {
         $.ajaxSettings.async = false;
         $.get('/factory/villages/?street='+$("#street-id").find("option:selected").text(), function(data){
            var village_html = '<option value="0">请选择</option>'
            for(var i=0; i<data.vlist.length; i++){
            village_html += '<option value="' + data.vlist[i].name + '">' + data.vlist[i].name + '</option>'
        }
         $('#village-id').html(village_html)

          });
          $.ajaxSettings.async = true;
    }

    $('#city-id').change(function () {
            getAreas()

    });

   $('#area-id').change(function () {
       getStreets()

    });

     $('#street-id').change(function () {
        getVillages()

    });


    $.get('/factory/areas/',function (data) {
        //地区
        var area_html = ''
        for(var i=0; i<data.area.length; i++){
            area_html += '<option value="' + data.area[i].name + '">' + data.area[i].name + '</option>'
        }
        $('#area-id').html(area_html);
        //设施
        var facility_html_list = ''
        for(var i=0; i<data.facility.length; i++){
            var facility_html = '<li><div class="checkbox"><label><input type="checkbox" name="facility"'
            facility_html += ' value="' + data.facility[i].id + '">' + data.facility[i].name
            facility_html += '</label></div></li>'

            facility_html_list += facility_html
        }
        $('.house-facility-list').html(facility_html_list);
    });

    //为图片表单绑定事件
    $('#form-house-image').submit(function (e) {
        e.preventDefault();
        if ($(".image_btn_cons").length >= 3) {
            console.log('image length=', $(".image_btn_cons").length);
            return false
        }
        $(this).ajaxSubmit({
            url: "/house/image_house/",
            type: "post",
            dataType: "json",
            success: function (data) {
                if (data.code == '200') {
                    $('.house-image-cons').append('<div class="image_btn_cons"><img src="'+data.url+'"/><button type="button" class="del_img btn btn-danger" onclick="del_img('+ data.id +',this)">删除</button></div>');
                }
            }
        });
        return false;
    });

    //为房屋表单绑定提交事件
    $('#form-house-info').submit(function () {
        $('.error-msg text-center').hide();
        console.log('form data', $(this).serialize());
        var id= $('#form-house-info input[name="id"]').val()
        console.log('id',id)
        if (id!= '' && id != undefined){
             $.post('/house/edit/'+id, $(this).serialize(),function (data) {
            if(data.code== '200'){
                $('#form-house-info').hide();
                $('#form-house-image').show();
                $('#house-id').val(data.house_id);
                for(image of data.house_images) {
                    $('.house-image-cons').append('<div class="image_btn_cons"><img src="'+image.url+'"/><button type="button" class="del_img btn btn-danger" onclick="del_img('+ image.id + ',this)">删除</button></div>');
                }

            }else{
                $('.error-msg text-center').show().find('span').html(ret_map[data.code]);
            }
        });
        }
        else{
           $.post('/house/add/',$(this).serialize(),function (data) {
            if(data.code== '200'){
                $('#form-house-info').hide();
                $('#form-house-image').show();
                $('#house-id').val(data.house_id);
            }else{
                $('.error-msg text-center').show().find('span').html(ret_map[data.code]);
            }
        });
        }

        return false;
    });

    function adjustWidth() {
        var parentwidth = $(".container").width();
        $(".top-bar").width(parentwidth);
        $(".footer").width(parentwidth);
    }

    $(window).resize(
        function () {
            adjustWidth();
        });

    adjustWidth();


})