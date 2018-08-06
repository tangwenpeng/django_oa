layui.use(['form', 'layer', 'table', 'laytpl','treeGrid'], function () {
    var form = layui.form,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery,
        laytpl = layui.laytpl,
        table = layui.table,
        treeGrid = layui.treeGrid;

    //部门列表
    var table = treeGrid.render({
        elem: '#deptList'
        , url: '/app/dept_list/'
        , cellMinWidth: 100
        , treeId: 'd_id'//树形id字段名称
        , treeUpId: 'higher_id'//树形父id字段名称
        , treeShowName: 'department'//以树形式显示的字段
        , id: "deptListTable"
        , cols: [[
            {type: 'checkbox'},
            {field: 'department', title: '部门名称', width:300},
            {field: 'department_num', title: '部门编号', minWidth: 100, align: "center"},
            {field: 'description', title: '部门简介', align: 'center', minWidth: 150},
            {title: '操作', minWidth: 175, templet: '#deptListBar', fixed: "right", align: "center"}
        ]]
        , page: false


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

    //添加部门
    function addDept(edit) {
        var index = layui.layer.open({
            title: "添加部门",
            type: 2,
            content: "/app/dept_add/",
            success: function (layero, index) {
                var body = layui.layer.getChildFrame('body', index);
                if (edit) {
                    body.find(".department_num").val(edit.department_num); //部门编号
                    body.find(".department").val(edit.department);  //部门名称
                    body.find(".description").val(edit.description); //部门简介
                    body.find('.higher_id').val(edit.higher_id);
                    body.find('.layui-select-title .layui-unselect').val(edit.higher_department);
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
        addDept();
    });


    //列表操作
    table.on('tool(deptList)', function (obj) {
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        var layEvent = obj.event,
            data = obj.data;
        if (layEvent === 'edit') { //编辑
            addDept(data);
        } else if (layEvent === 'del') { //删除
            layer.confirm('确定删除此部门？', {icon: 3, title: '提示信息'}, function (index) {
                $.ajax({
                    url: '/app/dept_del/',
                    type: 'post',
                    dataType: 'json',
                    data: {d_id: data.d_id},
                    headers: {'X-CSRFToken': csrf},
                    success: function (msg) {
                        if (msg.code == 0) {
                            tableIns.reload();
                            layer.close(index);
                        }
                    },
                });
            });
        }
    });

})
