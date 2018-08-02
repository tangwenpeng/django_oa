layui.use(['form', 'layer'], function () {
    var form = layui.form
    layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery;

    form.on("submit(addDept)", function (data) {
        //弹出loading
        var index = top.layer.msg('数据提交中，请稍候', {icon: 16, time: false, shade: 0.8});
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/app/dept_add/',
            type: 'POST',
            data: {
                description: $('.description').val(),    //部门简介
                department_num: $(".department_num").val(),  //部门编号
                department: $(".department").val(),  //部门名称
                higher_id: data.field.higher_id,  //上级部门id
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

});