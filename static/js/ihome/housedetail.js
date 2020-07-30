function hrefBack() {
    history.go(-1);
}

function decodeQuery(){
    var search = decodeURI(document.location.search);
    return search.replace(/(^\?)/, '').split('&').reduce(function(result, item){
        values = item.split('=');
        result[values[0]] = values[1];
        return result;
    }, {});
}

$(document).ready(function(){
    $(".book-house").show();

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
})

$.get('/house/detail/', function(data){
    var search = document.location.search
    id = search.split('=')[1]
    $.get('/house/detail/' + id + '/', function(data){
        var banner_image = ''
        console.log(data.house)
        for(var i=0; i<data.house.images.length; i++){
            banner_li = '<li class="swiper-slide"><img src="' + data.house.images[i] + '"></li>'
            banner_image += banner_li
        }
        $('.swiper-wrapper').html(banner_image)

        var mySwiper = new Swiper ('.swiper-container', {
            loop: true,
            autoplay: 2000,
            autoplayDisableOnInteraction: false,
            pagination: '.swiper-pagination',
            paginationType: 'fraction'
        })

        $('.house-price').html('￥<span>' + data.house.price + '</span>/晚')

        $('.house-info-address').html(data.house.address)

        $('.house-title').html(data.house.title)

        $('.landlord-name').html('房东： <span>' + data.house.user_name + '</span>')

        $('.landlord-pic').html('<img src="' + data.house.user_avatar + '">')

        $('.house-type-detail').html('<h3>出租' + data.house.room_count + '间房</h3>')

        $('.house-capacity').html('<h3>房屋面积:' + data.house.acreage + '平米</h3>')

        var direction
        if (data.house.direction == 'south' ) {
            direction = '南'
        } else if(data.house.direction == 'east') {
             direction = '东'
        } else if(data.house.direction == 'west') {
             direction = '西'
        }  else if(data.house.direction == 'north') {
             direction = '北'
        }

        var house_info_style = '<li>房间朝向: <span>' + direction + '</span></li>'
        house_info_style += '<li>房间楼层: <span>' + data.house.floor.split('/')[0] + '楼 / 共'+ data.house.floor.split('/')[1] +'层'+ '</span></li>'
        if (data.house.cook_bath_room == 'share') {
              house_info_style += '<li>厨卫配置:<span> 独立厨卫 </span></li>'
        } else {
             house_info_style += '<li>厨卫配置:<span> 共享厨卫 </span> </li>'
        }

        $('.house-info-style').append(house_info_style)

        var house_facility_list = ''
        for(var i=0; i<data.facility_list.length; i++){
            house_facility_list += '<li><span class="' + data.facility_list[i].css + '"></span>' + data.facility_list[i].name + '</li>'
        }
        $('.house-facility-list').html(house_facility_list)

        $('.book-house').attr('href', '/house/booking/?id=' + data.house.id)

        //判断是否显示预订按钮
        if(data.booking==1){
            $(".book-house").show();
        }else{
            $(".book-house").hide();
        }
    });
});
