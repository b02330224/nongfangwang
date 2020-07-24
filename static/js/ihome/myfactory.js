//获取用户信息，判断是否进行过实名认证
$.get('/factory/my_auth/',function (data) {
    if(data.code== '200'){
        //已经完成实名认证
        $('#factory-list').show();
        var html=template('factory_list_script',{flist:data.flist});
        $('#factory-list').append(html);
    }else{
        //未实名认证
        $('#auth-warn').show();
    }
});

$(document).ready(function() {
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
});