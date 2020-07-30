var cur_page = 1; // 当前页
var next_page = 1; // 下一页
var total_page = 1;  // 总页数
var house_data_querying = true;   // 是否正在向后台获取数据

// 解析url中的查询字符串
function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

// 更新用户点选的筛选条件
function updateFilterDateDisplay() {
    var startDate = $("#start-date").val();
    var endDate = $("#end-date").val();
    var $filterDateTitle = $(".filter-title-bar>.filter-title").eq(0).children("span").eq(0);
    if (startDate) {
        var text = startDate.substr(5) + "/" + endDate.substr(5);
        $filterDateTitle.html(text);
    } else {
        $filterDateTitle.html("日期范围");
    }
}


// 更新房源列表信息
// action表示从后端请求的数据在前端的展示方式
// 默认采用追加方式
// action=renew 代表页面数据清空从新展示
function updateHouseData(action) {
    // var areaId = $(".filter-area>li.active").attr("area");
    // if (undefined == areaId){
    //     areaId = location.search.split('&')[0].split('=')[1]
    // };
    var city = $("#city-id").val()
    var area = $("#area-id").val()
    var street = $("#street-id").val()
    var startDate = $("#start-date").val();
    var endDate = $("#end-date").val();
    var sortKey = $(".filter-sort>li.active").attr("sort-key");
    var params = {
        city:city,
        area:area,
        street:street,
        sd:startDate,
        ed:endDate,
        sk:sortKey,
        p:next_page
    };
    //发起ajax请求，获取数据，并显示在模板中
    console.log(params)
    $.ajax({
        url:'/house/list/',
        type:'GET',
        data:params,
        dataType:'json',
        success:function(data){
            if(data.code == '200'){
                var search_html = template('a_script',{hlist: data.hlist})

                 if (action =='renew') {
                    // 刷新
                    $('.house-list').html(search_html);
                 } else {
                    //下拉
                    cur_page=next_page;
                    $('.house-list').append(search_html);
                }

            }
        }
    })
}

 function getCitys() {
         $.get('/factory/citys/',function (data) {
        //城市
        var city_html = '<option value="">请选择</option>'
        for(var i=0; i<data.clist.length; i++){
            city_html += '<option value="' + data.clist[i].name+ '">' + data.clist[i].name + '</option>'
        }
        $('#city-id').html(city_html);

    });
    }

    function getAreas(){
         $.ajaxSettings.async = false;
         $.get('/factory/areas/?city='+$("#city-id").find("option:selected").text(), function(data){
            var area_html = '<option value="">请选择</option>'
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
            var street_html = '<option value="">请选择</option>'
            for(var i=0; i<data.slist.length; i++){
            street_html += '<option value="' + data.slist[i].name + '">' + data.slist[i].name + '</option>'
        }
         $('#street-id').html(street_html)

          });

          $.ajaxSettings.async = true;
    }


$(document).ready(function(){
    var queryData = decodeQuery();
    var startDate = queryData["sd"];
    var endDate = queryData["ed"];
    $("#start-date").val(startDate);
    $("#end-date").val(endDate);
    updateFilterDateDisplay();
    var areaName = queryData["aname"];
    if (!areaName) areaName = "位置区域";
    $(".filter-title-bar>.filter-title").eq(1).children("span").eq(0).html(areaName);


    // 获取筛选条件中的城市区域信息

    // $(".input-daterange input").datepicker({
    //     format: "yyyy-mm-dd",
    //     startDate: "today",
    //     language: "zh-CN",
    //     autoclose: true,
    //     orientation: "bottom right"
    // });

     $("#start-date").datepicker({
        format: "yyyy-mm-dd",
        startDate: "2020-07-01",
        language: "zh-CN",
        autoclose: true,
        orientation: "bottom right"
    });

     $("#end-date").datepicker({
        format: "yyyy-mm-dd",
        startDate: "2020-07-01",
        language: "zh-CN",
        autoclose: true,
        orientation: "bottom right"
    });

    var $filterItem = $(".filter-item-bar>.filter-item");
    $(".filter-title-bar").on("click", ".filter-title", function(e){
        var index = $(this).index();
        if (!$filterItem.eq(index).hasClass("active")) {
            $(this).children("span").children("i").removeClass("fa-angle-down").addClass("fa-angle-up");
            $(this).siblings(".filter-title").children("span").children("i").removeClass("fa-angle-up").addClass("fa-angle-down");
            $filterItem.eq(index).addClass("active").siblings(".filter-item").removeClass("active");
            $(".display-mask").show();
        } else {
            $(this).children("span").children("i").removeClass("fa-angle-up").addClass("fa-angle-down");
            $filterItem.eq(index).removeClass('active');
            $(".display-mask").hide();
            updateFilterDateDisplay();
        }
    });
    $(".display-mask").on("click", function(e) {
        $(this).hide();
        $filterItem.removeClass('active');
        updateFilterDateDisplay();
        cur_page = 1;
        next_page = 1;
        total_page = 1;
        updateHouseData("renew");

    });
    $(".filter-item-bar>.filter-area").on("click", "li", function(e) {
        if (!$(this).hasClass("active")) {
            $(this).addClass("active");
            $(this).siblings("li").removeClass("active");
            $(".filter-title-bar>.filter-title").eq(1).children("span").eq(0).html($(this).html());
        } else {
            $(this).removeClass("active");
            $(".filter-title-bar>.filter-title").eq(1).children("span").eq(0).html("位置区域");
        }

    });
    $(".filter-item-bar>.filter-sort").on("click", "li", function(e) {
        if (!$(this).hasClass("active")) {
            $(this).addClass("active");
            $(this).siblings("li").removeClass("active");
            $(".filter-title-bar>.filter-title").eq(2).children("span").eq(0).html($(this).html());
        }
    })

    $.get('/house/area_facility/', function(data){
        if(data.code == '200'){
            for(var i=0;i<data.area_info.length;i++){
                var area_li = '<li area-id="' + data.area_info[i].id + '">' + data.area_info[i].name + '</li>'
                $('.filter-area').append(area_li)
            }
        }
    })

    var search_path = location.search
    console.log('search_path', search_path)
    $.get('/house/my_search/' + search_path, function(data){
        if(data.code == '200'){
            var search_html = template('search_house_script',{ohouse: data.house_info})
            $('.house-list').append(search_html)
        }
    });

     $.get('/house/list/', function(data){

        if(data.code == 200){
            console.log('get house lsit ok');
            console.log(data.flist);
             $('.register-login').hide()
             $('.user-info').show().find('.user-name').text(data.name)
             for(obj of data.hlist) {
                 let floors = obj.floor.split('/')
                 obj.floor = floors[0]+'楼'
                 if(obj.direction=='east') {
                     obj.direction = '朝东'
                 } else if(obj.direction=='south') {
                     obj.direction = '朝南'
                 } else if(obj.direction=='west') {
                     obj.direction = '朝西'
                 }
                 else if(obj.direction=='north') {
                     obj.direction = '朝北'
                 }
                 if(obj.have_cook_bath == 'single'){
                     obj.have_cook_bath = '独立厨卫'
                 } else {
                     obj.have_cook_bath = '公用厨卫'
                 }
             }
              var house_html = template('a_script',{hlist: data.hlist})
            console.log('house_html', house_html)
            $('#house-list').append(house_html)
        }else{
            $('.user-info').hide()
            $('.register-login').show()
        }


    });


      getCitys()
      $('#city-id').change(function () {
            getAreas()

      });

      $('#area-id').change(function () {
       getStreets()
      });

       function adjustWidth() {
       var parentwidth = $(".container").width();
       $(".top-bar").width(parentwidth);
        $(".footer").width(parentwidth);
     }

     $(window).resize(
     function() {
       adjustWidth();
     });

     adjustWidth();


});

 function logout() {
         $.ajax({
             url: '/user/logout/',
             type: 'DELETE',
             success: function (data) {
                 if (data.code == '200') {
                     $(".user-info").hide();
                     $(".register-login").show();
                 }
             }
         });

     }