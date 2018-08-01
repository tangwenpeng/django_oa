layui.use(['form','layer','laydate','table','laytpl'],function(){
    var form = layui.form,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery,
        laydate = layui.laydate,
        laytpl = layui.laytpl,
        table = layui.table;

    //添加验证规则
    form.verify({
        oldPwd : function(value, item){
            if(value != "123456"){
                return "密码错误，请重新输入！";
            }
        },
        newPwd : function(value, item){
            if(value.length < 6){
                return "密码长度不能小于6位";
            }
        },
        confirmPwd : function(value, item){
            if(!new RegExp($("#oldPwd").val()).test(value)){
                return "两次输入密码不一致，请重新输入！";
            }
        }
    })

    //用户等级
    table.render({
        elem: '#userGrade',
        url : '../../json/userGrade.json',
        cellMinWidth : 95,
        cols : [[
            {field:"id", title: 'ID', width: 60, fixed:"left",sort:"true", align:'center', edit: 'text'},
            {field: 'gradeIcon', title: '图标展示', templet:'#gradeIcon', align:'center'},
            {field: 'gradeName', title: '等级名称', edit: 'text', align:'center'},
            {field: 'gradeValue', title: '等级值', edit: 'text',sort:"true", align:'center'},
            {field: 'gradeGold', title: '默认金币', edit: 'text',sort:"true", align:'center'},
            {field: 'gradePoint', title: '默认积分', edit: 'text',sort:"true", align:'center'},
            {title: '当前状态',minWidth:100, templet:'#gradeBar',fixed:"right",align:"center"}
        ]]
    });

    form.on('switch(gradeStatus)', function(data){
        var tipText = '确定禁用当前会员等级？';
        if(data.elem.checked){
            tipText = '确定启用当前会员等级？'
        }
        layer.confirm(tipText,{
            icon: 3,
            title:'系统提示',
            cancel : function(index){
                data.elem.checked = !data.elem.checked;
                form.render();
                layer.close(index);
            }
        },function(index){
            layer.close(index);
        },function(index){
            data.elem.checked = !data.elem.checked;
            form.render();
            layer.close(index);
        });
    });

    //控制表格编辑时文本的位置【跟随渲染时的位置】
    $("body").on("click",".layui-table-body.layui-table-main tbody tr td",function(){
        $(this).find(".layui-table-edit").addClass("layui-"+$(this).attr("align"));
    });

})