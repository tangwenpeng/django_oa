layui.use(['form', 'layer', 'tree'], function () {
    var form = layui.form,
        tree = layui.tree,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery;

    form.on("submit(addUser)", function (data) {
        // 弹出loading
        var index = top.layer.msg('数据提交中，请稍候', {icon: 16, time: false, shade: 0.8});
        // 实际使用时的提交信息
        $.post("/app/user_add", {
            userName: $(".userName").val(),  //登录名
            userEmail: $(".userEmail").val(),  //邮箱
            userSex: data.field.sex,  //性别
            userGrade: data.field.userGrade,  //会员等级
            userStatus: data.field.userStatus,    //用户状态
            newsTime: submitTime,    //添加时间
            userDesc: $(".userDesc").text(),    //用户简介
        }, function (res) {

        });
        setTimeout(function () {
            top.layer.close(index);
            top.layer.msg("用户添加成功！");
            layer.closeAll("iframe");
            //刷新父页面
            parent.location.reload();
        }, 2000);
        return false;
    })

    $.get('/app/dept_tree/', function (msg) {
        tree({
        elem: "#classtree"
        ,
        nodes: Array(msg)
        ,
        click: function (node) {
            var $select = $($(this)[0].elem).parents(".layui-form-select");
            $select.removeClass("layui-form-selected").find(".layui-select-title span").html(node.name).end().find("input:hidden[name='higher_id']").val(node.id);
        }
    });
    });


    $(".downpanel").on("click", ".layui-select-dept", function (e) {
        $(".layui-form-select").not($(this).parents(".layui-form-select")).removeClass("layui-form-selected");
        $(this).parents(".downpanel").toggleClass("layui-form-selected");
        layui.stope(e);
    }).on("click", "dl i", function (e) {
        layui.stope(e);
    });
    $(document).on("click", function (e) {
        $(".select-dept").removeClass("layui-form-selected");
    });

})