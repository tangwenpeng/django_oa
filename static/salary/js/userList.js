layui.use(['form','layer','table','laytpl'],function(){
    var form = layui.form,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery,
        laytpl = layui.laytpl,
        table = layui.table;

    //用户列表
    var tableIns = table.render({
        elem: '#userList',
        url : '/app/salary/',
        cellMinWidth : 95,
        page : true,
        height : "full-125",
        limits : [10,15,20,25],
        limit : 20,
        id : "salaryListTable",
        cols : [[
            {type: "checkbox", fixed:"left", width:50},
            {field: 'time', title: '时间', minWidth:120, align:"center"},
            {field: 'jobNumber', title: '员工编号', minWidth:100, align:"center"},
            {field: 'userName', title: '员工姓名', minWidth:100, align:"center"},
            {field: 'staff_department', title: '所属部门', minWidth:100, align:"center"},
            {field: 'basic_salary', title: '基础薪资', minWidth:100, align:"center"},
            {field: 'deduct_salary', title: '应扣工资', minWidth:100, align:"center"},
            {field: 'allowance', title: '津贴', minWidth:100, align:"center"},
            {field: 'award', title: '奖金', minWidth:100, align:"center"},
            {field: 'five_insurance', title: '五险一金', minWidth:100, align:"center"},
            {field: 'provident_fund', title: '公积金', minWidth:100, align:"center"},
            {field: 'real_salary', title: '实际工资', minWidth:100, align:"center"},
            {field: 'real_salary', title: '实际工资', minWidth:100, align:"center"},
            {field: 'salary_status', title: '发放状态', minWidth:100, align:"center"},
            // {field: 'userEmail', title: '用户邮箱', minWidth:200, align:'center',templet:function(d){
            //     return '<a class="layui-blue" href="mailto:'+d.userEmail+'">'+d.userEmail+'</a>';
            // }},
            // {field: 'userSex', title: '用户性别', align:'center'},
            // {field: 'userStatus', title: '用户状态',  align:'center',templet:function(d){
            //     return d.userStatus == "0" ? "正常使用" : "限制使用";
            // }},
            // {field: 'userGrade', title: '用户等级', align:'center',templet:function(d){
            //     if(d.userGrade == "0"){
            //         return "注册会员";
            //     }else if(d.userGrade == "1"){
            //         return "中级会员";
            //     }else if(d.userGrade == "2"){
            //         return "高级会员";
            //     }else if(d.userGrade == "3"){
            //         return "钻石会员";
            //     }else if(d.userGrade == "4"){
            //         return "超级会员";
            //     }
            // }},
            // {field: 'userEndTime', title: '最后登录时间', align:'center',minWidth:150},
            {title: '操作', minWidth:180, templet:'#userListBar',fixed:"right",align:"center"}
        ]]
    });

    //搜索【此功能需要后台配合，所以暂时没有动态效果演示】
    $(".search_btn").on("click",function(){
        if($(".searchVal").val() != ''){
            table.reload("newsListTable",{
                page: {
                    curr: 1 //重新从第 1 页开始
                },
                where: {
                    key: $(".searchVal").val()  //搜索的关键字
                }
            })
        }else{
            layer.msg("请输入搜索的内容");
        }
    });
    //添加用户
    function addUser(edit){
        var index = layui.layer.open({
            title : "添加用户",
            type : 2,
            content : "/static/page/user/userAdd.html",
            success : function(layero, index){
                var body = layui.layer.getChildFrame('body', index);
                if(edit){
                    body.find(".userName").val(edit.userName);  //登录名
                    body.find(".userEmail").val(edit.userEmail);  //邮箱
                    body.find(".userSex input[value="+edit.userSex+"]").prop("checked","checked");  //性别
                    body.find(".userGrade").val(edit.userGrade);  //会员等级
                    body.find(".userStatus").val(edit.userStatus);    //用户状态
                    body.find(".userDesc").text(edit.userDesc);    //用户简介
                    form.render();
                }
                setTimeout(function(){
                    layui.layer.tips('点击此处返回用户列表', '.layui-layer-setwin .layui-layer-close', {
                        tips: 3
                    });
                },500)
            }
        });
        layui.layer.full(index);
        window.sessionStorage.setItem("index",index);
        //改变窗口大小时，重置弹窗的宽高，防止超出可视区域（如F12调出debug的操作）
        $(window).on("resize",function(){
            layui.layer.full(window.sessionStorage.getItem("index"));
        })
    }
    $(".addNews_btn").click(function(){
        addUser();
    })

    //批量删除
    $(".delAll_btn").click(function(){
        var checkStatus = table.checkStatus('userListTable'),
            data = checkStatus.data,
            newsId = [];
        if(data.length > 0) {
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
        }else{
            layer.msg("请选择需要删除的用户");
        }
    });
    //列表操作
    table.on('tool(userList)', function(obj){
        var layEvent = obj.event,
            data = obj.data;

        if(layEvent === 'edit'){ //编辑
            addUser(data);
        }else if(layEvent === 'pay_salary'){ //启用禁用

            var salary_status = data['salary_status'];
            btnText = data['salary_status'];
            var _this = $(this),
                pay_salaryText = '工资已发放',
                btnText = '已发放';
            if(_this.text()=="未发放"){
                pay_salaryText = "是否发放工资？";
                btnText = "已发放";
            }
            layer.confirm(pay_salaryText, {
                    icon: 3,
                    title: '系统提示',
                    cancel: function (index) {
                        layer.close(index);
                    }
                },function (index) {
                    _this.text(btnText)
                    layer.close(index)
                }
            );
            // var salary_status = data['salary_status'];
            // var _this = $(this),
            //     usableText = "工资已发放",
            //     btnText = "已发放";
            // if(_this.text()=="未发放"){
            //     usableText = "是否发放工资？";
            //     btnText = "已发放";
            //
            // }
            // layer.confirm(usableText,{
            //     icon: 3,
            //     title:'系统提示',
            //     cancel : function(index){
            //         layer.close(index);
            //     }
            // },function(index){
            //     _this.text(btnText);

                // var csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
                // $.ajax({
                //     url: '/app/change_status/',
                //     type: 'post',
                //     dataType: 'json',
                //     data: {'status': btnText, 'data': data},
                //     headers: {'X-CSRFToken': csrf_token},
                //     success: function (resp) {
                //         if (resp.code == 200){
                //             usableText = "工资已发放";
                //             btnText = "已发放";
                //             location.href = '/app/pay_salary/';
                //         }
                //     }
                // });
                // layer.close(index);
            // },function(index){
            //     layer.close(index);
            // });
        }else if(layEvent === 'del'){ //删除
            layer.confirm('确定删除此用户？',{icon:3, title:'提示信息'},function(index){
                // $.get("删除文章接口",{
                //     newsId : data.newsId  //将需要删除的newsId作为参数传入
                // },function(data){
                    tableIns.reload();
                    layer.close(index);
                // })
            });
        }else if(layEvent === 'check'){
            var index = layui.layer.open({
            title : "查看工资",
            area: ['900px', '500px'],
            // area: ['auto'],
            type : 2,
            content : "/app/check_salary/",
            success : function(layero, index){
                // var body = layui.layer.getChildFrame('body', index);
                // if(edit){
                //     body.find(".userName").val(edit.userName);  //登录名
                //     body.find(".userEmail").val(edit.userEmail);  //邮箱
                //     body.find(".userSex input[value="+edit.userSex+"]").prop("checked","checked");  //性别
                //     body.find(".userGrade").val(edit.userGrade);  //会员等级
                //     body.find(".userStatus").val(edit.userStatus);    //用户状态
                //     body.find(".userDesc").text(edit.userDesc);    //用户简介
                //     form.render();
                // }
                setTimeout(function(){
                    layui.layer.tips('点击此处返回薪资列表', '.layui-layer-setwin .layui-layer-close', {
                        tips: 3
                    });
                },500)
            }
        })
        }
    });

});