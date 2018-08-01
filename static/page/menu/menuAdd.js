layui.use(['form', 'layer', 'tree'], function () {

    var form = layui.form,
        tree = layui.tree,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery;

    form.on("submit(addUser)", function (data) {
        //弹出loading
        var index = top.layer.msg('数据提交中，请稍候', {icon: 16, time: false, shade: 0.8});
        // 实际使用时的提交信息
        // $.post("上传路径",{
        //     userName : $(".userName").val(),  //登录名
        //     userEmail : $(".userEmail").val(),  //邮箱
        //     userSex : data.field.sex,  //性别
        //     userGrade : data.field.userGrade,  //会员等级
        //     userStatus : data.field.userStatus,    //用户状态
        //     newsTime : submitTime,    //添加时间
        //     userDesc : $(".userDesc").text(),    //用户简介
        // },function(res){
        //
        // })
        setTimeout(function () {
            top.layer.close(index);
            top.layer.msg("用户添加成功！");
            layer.closeAll("iframe");
            //刷新父页面
            parent.location.reload();
        }, 2000);
        return false;
    });
    form.on('radio', function (data) {
        //console.log(data.elem); //得到radio原始DOM对象
        //console.log(data.value); //被点击的radio的value值
        if (data.value == 3) {
            $('#permission_div').show();
        } else {
            $('#permission_div').hide();
        }
    });



    tree({
        elem: "#classtree"
        ,
        nodes: [{
            name: '常用文件夹',
            id: 1,
            children: [{name: '所有未读', id: 11},
                {name: '置顶邮件', id: 12},
                {name: '标签邮件', id: 13}]
            }, {name: '我的邮箱',id: 2,
            spread: true,
            children: [{
                name: 'QQ邮箱',
                id: 21,
                spread: true,
                children: [{
                    name: '收件箱',
                    id: 211,
                    children: [{name: '所有未读', id: 2111}, {name: '置顶邮件', id: 2112}, {name: '标签邮件', id: 2113}]
                }, {name: '已发出的邮件', id: 212}, {name: '垃圾邮件', id: 213}]
            }, {
                name: '阿里云邮',
                id: 22,
                children: [{name: '收件箱', id: 221}, {name: '已发出的邮件', id: 222}, {name: '垃圾邮件', id: 223}]
            }]
        }]
        ,
        click: function (node) {
            var $select = $($(this)[0].elem).parents(".layui-form-select");
            $select.removeClass("layui-form-selected").find(".layui-select-title span").html(node.name).end().find("input:hidden[name='menu_pid']").val(node.id);
        }
    });
    $(".downpanel").on("click", ".layui-select-title", function (e) {
        $(".layui-form-select").not($(this).parents(".layui-form-select")).removeClass("layui-form-selected");
        $(this).parents(".downpanel").toggleClass("layui-form-selected");
        layui.stope(e);
    }).on("click", "dl i", function (e) {
        layui.stope(e);
    });
    $(document).on("click", function (e) {
        $(".layui-form-select").removeClass("layui-form-selected");
    });

});