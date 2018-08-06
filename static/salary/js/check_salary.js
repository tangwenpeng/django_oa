layui.use(['form','layer','table','laytpl'],function(){
    var form = layui.form,
        layer = parent.layer === undefined ? layui.layer : top.layer,
        $ = layui.jquery,
        laytpl = layui.laytpl,
        table = layui.table;

    //用户列表
    var tableIns = table.render({
        elem: '#salaryList',
        url : '/app/salary/',
        cellMinWidth : 95,
        page : true,
        height : "full-125",
        limits : [10,15,20,25],
        limit : 20,
        id : "salaryDetailTable",
        cols : [[
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
        ]]
    });

    //搜索【此功能需要后台配合，所以暂时没有动态效果演示】
    $(".search_btn").on("click",function(){
        if($(".searchVal").val() != ''){
            table.reload("salaryDetailTable",{
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
});