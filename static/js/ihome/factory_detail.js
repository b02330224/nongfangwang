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
    $(".book-factory").show();

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

$.get('/factory/detail/', function(data){
    var search = document.location.search
    id = search.split('=')[1]
    $.get('/factory/detail/' + id + '/', function(data){
        var banner_image = ''
        console.log(data.factory)
        for(var i=0; i<data.factory.images.length; i++){
            banner_li = '<li class="swiper-slide"><img src="' + data.factory.images[i] + '"></li>'
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

        $('.factory-price').html('￥<span>' + data.factory.price + '</span>/晚')

        $('.factory-info-address').html(data.factory.address)

        $('.factory-title').html(data.factory.title)

        $('.landlord-name').html('房东： <span>' + data.factory.user_name + '</span>')

        $('.landlord-pic').html('<img src="' + data.factory.user_avatar + '">')

        $('.factory-type-detail').html('<h3>套房出租' + data.factory.room_count + '</h3><p>厂房面积:' + data.factory.acreage + '平米</p><p>厂房价格:' + data.factory.price+' '+data.factory.unit + '</p>')

        // $('.factory-capacity').html('<h3>宜住' + data.factory.capacity + '人</h3>')
        //
        // $('.factory-bed').html('<h3>卧床配置</h3><p>' + data.factory.beds + '</p>')
        //
        // var factory_info_style1 = '<li>收取押金<span>' + data.factory.deposit + '</span></li>'
        // factory_info_style1 += '<li>最少入住天数<span>' + data.factory.min_days + '</span></li>'
        // factory_info_style1 += '<li>最多入住天数<span>' + data.factory.max_days + '</span></li>'
        // $('.factory-info-style').html(factory_info_style1)


        var factory_info_style = '<li><span class="icon-user" style="float:left"></span></li>'
        factory_info_style += '<li>联系人:<span>' + data.factory.contact_person + '</span></li>'
        factory_info_style += '<li>联系电话: <span>' + data.factory.contact_mobile + '</span></li>'
        $('.factory-info-style').html(factory_info_style)

        var factory_facility_list = ''
        for(var i=0; i<data.facility_list.length; i++){
            factory_facility_list += '<li><span class="' + data.facility_list[i].css + '"></span>' + data.facility_list[i].name + '</li>'
        }
        $('.factory-facility-list').html(factory_facility_list)

        $('.book-factory').attr('href', '/factory/booking/?id=' + data.factory.id)

        //判断是否显示预订按钮
        if(data.booking==1){
            $(".book-factory").show();
        }else{
            $(".book-factory").hide();
        }
    });
});
