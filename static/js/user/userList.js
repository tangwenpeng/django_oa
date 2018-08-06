layui.use(['form', 'layer', 'table', 'laytpl'], function () {
    var form = layui.form,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery,
        laytpl = layui.laytpl,
        table = layui.table;

    //用户列表
    var tableIns = table.render({
        elem: '#userList',
        url: '/app/user_list/',
        cellMinWidth: 95,
        page: true,
        height: "full-125",
        limits: [10, 15, 20, 25],
        limit: 20,
        id: "userListTable",
        cols: [[
            {type: "checkbox", fixed: "left", width: 50},
            {field: 'job_number', title: '工号', width: 60, align: "center"},
            {field: 'name', title: '姓名', width: 100, align: "center"},
            {field: 'sex', title: '性别', width: 60, align: 'center'},
            {field: 'department', title: '所在部门', minWidth: 100, align: "center"},
            {field: 'role', title: '职位', minWidth: 100, align: "center"},
            {field: 'phone', title: '手机号码', minWidth: 130, align: 'center'},
            {field: 'office_phone', title: '办公电话', minWidth: 130, align: 'center'},
            {
                field: 'email', title: '电子邮箱', minWidth: 150, align: 'center', templet: function (d) {
                    return '<a class="layui-blue" href="mailto:' + d.email + '">' + d.email + '</a>';
                }
            },

            {title: '操作', minWidth: 175, templet: '#userListBar', fixed: "right", align: "center"}
        ]]
    });

    //搜索【此功能需要后台配合，所以暂时没有动态效果演示】
    $(".search_btn").on("click", function () {
        if ($(".searchVal").val() != '') {
            table.reload("newsListTable", {
                page: {
                    curr: 1 //重新从第 1 页开始
                },
                where: {
                    key: $(".searchVal").val()  //搜索的关键字
                }
            })
        } else {
            layer.msg("请输入搜索的内容");
        }
    });

    //添加用户
    function addUser(edit) {
        var index = layui.layer.open({
            title: "添加用户",
            type: 2,
            content: "/app/user_add/",
            success: function (layero, index) {
                var body = layui.layer.getChildFrame('body', index);
                if (edit) {
                    body.find(".name").val(edit.name);  // 姓名
                    body.find(".password").val(edit.password);  // 密码
                    body.find(".userSex input[value=" + edit.userSex + "]").prop("checked", "checked");  //性别
                    body.find(".job_number").val(edit.job_number);  // 工号
                    body.find("#treeclass").text(edit.department);    // 部门
                    body.find("input:hidden[name='department']").val(edit.d_id);
                    body.find(".phone").val(edit.phone);    // 电话号码
                    body.find(".office_phone").val(edit.office_phone);    // 办公电话
                    body.find(".email").val(edit.email);    // 邮箱
                    body.find('.layui-select-title .layui-unselect').val(edit.role);

                    form.render();
                }

                setTimeout(function () {
                    layui.layer.tips('点击此处返回用户列表', '.layui-layer-setwin .layui-layer-close', {
                        tips: 3
                    });
                }, 500)
            }
        });
        layui.layer.full(index);
        window.sessionStorage.setItem("index", index);
        //改变窗口大小时，重置弹窗的宽高，防止超出可视区域（如F12调出debug的操作）
        $(window).on("resize", function () {
            layui.layer.full(window.sessionStorage.getItem("index"));
        })
    }

    $(".addNews_btn").click(function () {
        addUser();
    })

    //批量删除
    $(".delAll_btn").click(function () {
        var checkStatus = table.checkStatus('userListTable'),
            data = checkStatus.data,
            newsId = [];
        if (data.length > 0) {
            for (var i in data) {
                newsId.push(data[i].newsId);
            }
            layer.confirm('确定删除选中的用户？', {icon: 3, title: '提示信息'}, function (index) {
                // $.get("删除文章接口",{
                //     newsId : newsId  //将需要删除的newsId作为参数传入
                // },function(data){
                tableIns.reload();
                layer.close(index);
                // })
            })
        } else {
            layer.msg("请选择需要删除的用户");
        }
    });

    //列表操作
    table.on('tool(userList)', function (obj) {
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        var layEvent = obj.event,
            data = obj.data;
        console.log(data)
        if (layEvent === 'edit') { //编辑
            addUser(data);
        } else if (layEvent === 'del') { //删除
            layer.confirm('确定删除此用户？', {icon: 3, title: '提示信息'}, function (index) {
                $.ajax({
                    url: "/app/user_del/",
                    type: 'post',
                    dataType: 'json',
                    data: {job_no: data.job_number},
                    headers: {'X-CSRFToken': csrf},
                    success: function (msg) {
                        if (msg.code == 0){
                            tableIns.reload();
                            layer.close(index);
                        }
                    }
                });
            });
        }
    });

})
