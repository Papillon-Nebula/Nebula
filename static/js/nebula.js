function doSendMail(){
    var email = $.trim($("#reqname").val());
    // 对邮箱地址进行校验（ xxx@xxx.xx ）
    if (!email.match(/.+@.+\..+/)){
        bootbox.alert({title:"错误提示", message: "邮箱地址格式不正确！"});
        $("#reqname").focus();
        return false;
    }
    // 如果邮箱格式正确，则让发送邮件按钮变成不可点击，避免二次操作
    $(obj).attr('disabled', true);

    $.post('/ecode', 'email = ' + email, function(data){
        if (data == 'email-invalid'){
            bootbox.alert({title:"错误提示", message: "邮箱地址格式不正确！"});
            $("#reqname").focus();
            return false
        }
        if (data == 'send-pass'){
            bootbox.alert({title:"信息提示", message:"邮箱验证码已发送成功，请查收！"});
            $("//#regname").attr('disabled', true);     // 验证码发送完后禁止修改注册邮箱
            $(obj).attr('disabled',true)        // 发送邮件按钮变成不可用
        }
        else {
            bootbox.alert({title:"错误提示", message:"邮箱验证码未发送成功！"});
            return false;
        }
    })
}


function user_identification(){
    var name = $('input[name=username]').val()
    username = console.log(name);
    if(name!=""){
        $.ajax({
            url:'/login',
            type:'POST',
            data:{"username": $('input[name="username"]').val(),"password":$('input[name="password"]').val()},
            success: function(res){
                alert(res)
            },error:function(){
                alert("系统貌似遇到了一些问题！");
            }
        });
    }
    else
    {alert("请验证你的用户名！")};
}