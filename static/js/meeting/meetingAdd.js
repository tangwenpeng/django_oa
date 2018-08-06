layui.use(['form', 'layer'], function () {
    var form = layui.form
    layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery;

    form.on("submit(addDept)", function (data) {
        //弹出loading
        var index = top.layer.msg('数据提交中，请稍候', {icon: 16, time: false, shade: 0.8});
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/app/meeting_appointment/',
            type: 'GET',
            data: {
                department_id: $("select[name='department_num']").val() //参会部门
            },
            dataType: 'json',
            success: function () {
                return data;
            }

        });

        $.ajax({
            url: '/app/meeting_appointment/',
            type: 'POST',
            data: {
                meeting_room: $("select[name='meeting_room']").val(),  //会议室
                meeting_id: $("input[name='meeting_id']").val(),  //会议id
                meeting_date: $("input[name='meeting_date']").val(),  //预约时间
                meeting_title: $("input[name='meeting_title']").val(),  //会议主题
                department_id: $("select[name='department_num']").val(),  //参会部门
                job_number: $("select[name='job_number']").val(),  //参会人员
            },
            dataType: 'json',
            headers: {'X-CSRFToken': csrf},
            success: function (msg) {
                if (msg.code == 0) {
                    setTimeout(function () {
                        top.layer.close(index);
                        top.layer.msg("预约成功！");
                        layer.closeAll("iframe");
                        //刷新父页面
                        parent.location.reload();
                    }, 2000);
                }
            },
            error: function (msg) {
                alert('请求失败');
            },
        });
        return false;
    })

    //格式化时间
    function filterTime(val) {
        if (val < 10) {
            return "0" + val;
        } else {
            return val;
        }
    }

    //定时发布
    var time = new Date();
    var submitTime = time.getFullYear() + '-' + filterTime(time.getMonth() + 1) + '-' + filterTime(time.getDate()) + ' ' + filterTime(time.getHours()) + ':' + filterTime(time.getMinutes()) + ':' + filterTime(time.getSeconds());

})