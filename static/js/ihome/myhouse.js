//获取用户信息，判断是否进行过实名认证
$.get('/house/my_auth/',function (data) {
    if(data.code== '200'){
        //已经完成实名认证
        $('#houses-list').show();
        var html=template('house_list',{hlist:data.hlist});
        $('#houses-list').append(html);
    }else{
        //未实名认证
        $('#auth-warn').show();
    }
});

function delConfirm(url) {
     $('#url').val(url);//给会话中的隐藏属性URL赋值
  $('#delcfmModel').modal();
}

function urlSubmit(){
   var url=$.trim($("#url").val());//获取会话中的隐藏属性URL
   console.log(url)
    $.get(url, function (data) {
        if (data.code==200){
            window.location.href = '/house/my_house'
        }
    })
}

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
})