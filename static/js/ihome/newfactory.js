function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}

$(document).ready(function(){
    //查询地区、设施信息
    // $.get('/factory/area_facility/',function (data) {
    //     //地区
    //     var area_html = ''
    //     for(var i=0; i<data.area.length; i++){
    //         area_html += '<option value="' + data.area[i].id + '">' + data.area[i].name + '</option>'
    //     }
    //     $('#area-id').html(area_html);
    //     //设施
    //     var facility_html_list = ''
    //     for(var i=0; i<data.facility.length; i++){
    //         var facility_html = '<li><div class="checkbox"><label><input type="checkbox" name="facility"'
    //         facility_html += ' value="' + data.facility[i].id + '">' + data.facility[i].name
    //         facility_html += '</label></div></li>'
    //
    //         facility_html_list += facility_html
    //     }
    //     $('.factory-facility-list').html(facility_html_list);
    // });


      $.get('/factory/citys/',function (data) {
        //城市
        var city_html = '<option value="0">请选择</option>'
        for(var i=0; i<data.clist.length; i++){
            city_html += '<option value="' + data.clist[i].id + '">' + data.clist[i].name + '</option>'
        }
        $('#city-id').html(city_html);

    });


    $.get('/factory/facility/',function (data) {

        //设施
        var facility_html_list = ''
        for(var i=0; i<data.facility.length; i++){
            var facility_html = '<li><div class="checkbox"><label><input type="checkbox" name="facility"'
            facility_html += ' value="' + data.facility[i].id + '">' + data.facility[i].name
            facility_html += '</label></div></li>'

            facility_html_list += facility_html
        }
        $('.factory-facility-list').html(facility_html_list);
    });

    $('#city-id').change(function () {
        $.get('/factory/areas/?city='+$("#city-id").find("option:selected").text(), function(data){
            var area_html = '<option value="0">请选择</option>'
            for(var i=0; i<data.alist.length; i++){
            area_html += '<option value="' + data.alist[i].id + '">' + data.alist[i].name + '</option>'
        }
         $('#area-id').html(area_html)

          });

    });

    $('#area-id').change(function () {
        $.get('/factory/streets/?area='+$("#area-id").find("option:selected").text(), function(data){
            var street_html = '<option value="0">请选择</option>'
            for(var i=0; i<data.slist.length; i++){
            street_html += '<option value="' + data.slist[i].id + '">' + data.slist[i].name + '</option>'
        }
         $('#street-id').html(street_html)

          });

    });

     $('#street-id').change(function () {
        $.get('/factory/villages/?street='+$("#street-id").find("option:selected").text(), function(data){
            var village_html = '<option value="0">请选择</option>'
            for(var i=0; i<data.vlist.length; i++){
            village_html += '<option value="' + data.vlist[i].id + '">' + data.vlist[i].name + '</option>'
        }
         $('#village-id').html(village_html)

          });

    });
    //为图片表单绑定事件
    $('#form-factory-image').submit(function (e) {
        e.preventDefault();
        $(this).ajaxSubmit({
            url: "/factory/images/",
            type: "post",
            dataType: "json",
            success: function (data) {
                if (data.code == '200') {
                    $('.factory-image-cons').append('<img src="'+data.url+'"/>');
                }
            }
        });
        return false;
    });

    //为房屋表单绑定提交事件
    $('#form-factory-info').submit(function () {
        $('.error-msg text-center').hide();
        console.log($(this).serialize());
        $.post('/factory/add/',$(this).serialize(),function (data) {
            if(data.code== '200'){
                $('#form-factory-info').hide();
                $('#form-factory-image').show();
                $('#factory-id').val(data.factory_id);
            }else{
                $('.error-msg text-center').show().find('span').html(ret_map[data.code]);
            }
        });
        return false;
    });


     function adjustWidth() {
       var parentwidth = $(".container").width();
       $(".top-bar").width(parentwidth);
     }

     $(window).resize(
     function() {
       adjustWidth();
     });

     adjustWidth();

})