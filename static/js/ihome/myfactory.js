//获取用户信息，判断是否进行过实名认证
$.get('/house/my_auth/',function (data) {
    if(data.code== '200'){
        //已经完成实名认证
        $('#houses-list').show();
        var html=template('factory_list',{flist:data.flist});
        $('#houses-list').append(html);
    }else{
        //未实名认证
        $('#auth-warn').show();
    }
});