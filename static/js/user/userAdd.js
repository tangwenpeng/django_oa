layui.use(['form', 'layer', 'tree'], function () {
    var form = layui.form,
        tree = layui.tree,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery;

    form.on("submit(addUser)", function (data) {
        //弹出loading
        console.log(data)
        var index = top.layer.msg('数据提交中，请稍候', {icon: 16, time: false, shade: 0.8});
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/app/user_add/',
            type: 'POST',
            data: {
                name: $(".name").val(),  //姓名
                password: $(".password").val(),  //密码
                job_number: $(".job_number").val(),  //工号
                sex: data.field.sex,  //性别
                department: $('.department').val(),  //部门
                role: data.field.role,  //部门
                phone: $(".phone").val(),    // 电话
                office_phone: $(".office_phone").val(),    //办公电话
                email: $(".email").val(),    // 邮箱
            },
            dataType: 'json',
            headers: {'X-CSRFToken': csrf},
            success: function (msg) {
                if (msg.code == 0) {
                    setTimeout(function () {
                        top.layer.close(index);
                        top.layer.msg("用户添加成功！");
                        layer.closeAll("iframe");
                        //刷新父页面
                        parent.location.reload();
                    }, 1000);
                }
            },
            error: function (msg) {
                alert('请求失败');
            },
        });
        return false;
    });



    $.get('/app/dept_tree/', function (msg) {
        tree({
        elem: "#classtree"
        ,
        nodes: msg
        ,
        click: function (node) {
            var $select = $($(this)[0].elem).parents(".layui-form-select");
            $select.removeClass("layui-form-selected").find(".layui-select-title span").html(node.name).end().find("input:hidden[name='department']").val(node.id);
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