//模态框居中的控制
function centerModals(){
    $('.modal').each(function(i){   //遍历每一个模态框
        var $clone = $(this).clone().css('display', 'block').appendTo('body');    
        var top = Math.round(($clone.height() - $clone.find('.modal-content').height()) / 2);
        top = top > 0 ? top : 0;
        $clone.remove();
        $(this).find('.modal-content').css("margin-top", top-30);  //修正原先已经有的30个像素
    });
}

function setStartDate() {
    var startDate = $("#start-date-input").val();
    if (startDate) {
        $(".search-btn").attr("start-date", startDate);
        $("#start-date-btn").html(startDate);
        $("#end-date").datepicker("destroy");
        $("#end-date-btn").html("离开日期");
        $("#end-date-input").val("");
        $(".search-btn").attr("end-date", "");
        $("#end-date").datepicker({
            language: "zh-CN",
            keyboardNavigation: false,
            startDate: startDate,
            format: "yyyy-mm-dd"
        });
        $("#end-date").on("changeDate", function() {
            $("#end-date-input").val(
                $(this).datepicker("getFormattedDate")
            );
        });
        $(".end-date").show();
    }
    $("#start-date-modal").modal("hide");
}

function setEndDate() {
    var endDate = $("#end-date-input").val();
    if (endDate) {
        $(".search-btn").attr("end-date", endDate);
        $("#end-date-btn").html(endDate);
    }
    $("#end-date-modal").modal("hide");
}

function goToSearchPage(th) {
    var url = "/factory/search/?";
    url += ("sid=" + $(th).attr("street-id"));
    url += "&";
    var streetName = $(th).attr("street-name");
    if (undefined == streetName) streetName="";
    url += ("name=" + streetName);
    url += "&";
    url += ("sd=" + $(th).attr("start-date"));
    url += "&";
    url += ("ed=" + $(th).attr("end-date"));
    alert(url)
    location.href = url;
}


$(document).ready(function(){
    $('.modal').on('show.bs.modal', centerModals);      //当模态框出现的时候
    $(window).on('resize', centerModals);               //当窗口大小变化的时候
    $("#start-date").datepicker({
        language: "zh-CN",
        keyboardNavigation: false,
        startDate: "today",
        format: "yyyy-mm-dd"
    });
    $("#start-date").on("changeDate", function() {
        var date = $(this).datepicker("getFormattedDate");
        $("#start-date-input").val(date);
    });

//  首页获取区域信息
     $.get('/factory/citys/', function(data) {

         var city_html = template('home-city-list', {citys:data.clist})
        $('.city-list').html(city_html)

        $(".city-list a").click(function(e){
            $("#city-btn").html($(this).html());
           // $(".search-btn").attr("city-id", $(this).attr("city-id"));
           // $(".search-btn").attr("city-name", $(this).html());
            $("#city-modal").modal("hide");
        });
     });



     $('#area-modal').on('shown.bs.modal', function () {
          console.log('选择区..')
          $.get('/factory/areas/?city='+$("#city-btn").html(), function(data){
              var area_html = template('home-area-list', {areas:data.alist})
                $('.area-list').html(area_html)

                $(".area-list a").click(function(e){
                    $("#area-btn").html($(this).html());
                    $("#area-modal").modal("hide");
                });
          });
    });


        $('#street-modal').on('shown.bs.modal', function () {
          console.log('选择街道..')
          $.get('/factory/streets/?area='+$("#area-btn").html(), function(data){
              var street_html = template('home-street-list', {streets:data.slist})
                $('.street-list').html(street_html)

                $(".street-list a").click(function(e){
                    $("#street-btn").html($(this).html());
                    $("#street-modal").modal("hide");
                });
          });
    });


    $.get('/factory/findex/', function(data){

        if(data.code == '200'){
             $('.register-login').hide()
             $('.user-info').show().find('.user-name').text(data.name)
        }else{
            $('.user-info').hide()
            $('.register-login').show()
        }

        // var street_html = template('home-street-list', {streets:data.slist})
        // $('.street-list').html(street_html)
        //
        // $(".street-list a").click(function(e){
        //     $("#street-btn").html($(this).html());
        //
        //     $("#street-modal").modal("hide");
        // });

        var swiper_html = template('factory_list', {flist:data.flist})
        $('.swiper-wrapper').html(swiper_html)

        var mySwiper = new Swiper ('.swiper-container', {
            loop: true,
            autoplay: 2000,
            autoplayDisableOnInteraction: false,
            pagination: '.swiper-pagination',
            paginationClickable: true
        });

    });



})

function logout(){
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
