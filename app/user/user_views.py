from django.http import JsonResponse
from django.shortcuts import render

from app.models import Department,User,Role,UserRole


def user(request):
    """
    显示用户页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user/user.html')

def user_list(request):
    """
    显示用户列表
    :param request:
    :return:
    """
    if request.method == 'GET':
        users = User.objects.filter(is_delete=0)
        user_list = []
        msg = {
            "code": 0,
            "msg": "",
            "count": len(users),  # 所有部门总数
        }
        for user in users:
            temp = dict()
            temp['name'] = user.name
            temp['sex'] = '女' if user.sex else '男'
            temp['job_number'] = user.job_number
            temp['department'] = Department.objects.get(d_id=user.d_id).department
            temp['email'] = user.email
            temp['phone'] = user.phone
            temp['role'] = user.role.first().post if user.role.all() else None
            temp['office_phone'] = user.office_phone
            user_list.append(temp)
        msg['data'] = user_list
        return JsonResponse(msg)

def user_add(request):
    """
    添加用户
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user/userAdd.html')


def user_info(request):
    """
    显示用户信息
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user/userInfo.html')


def dept(request):
    """
    显示部门页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'dept/dept.html')


def dept_list(request):
    if request.method == 'GET':
        departments = Department.objects.filter(is_delete=0)
        departments_list = []
        msg = {
            "code": 0,
            "msg": "",
            "count": len(departments),  # 所有部门总数
        }
        for depart in departments:
            temp = dict()
            # 部门名称
            temp['department_num'] = depart.department_num
            # 部门编号
            temp['department'] = depart.department
            # 上级部门名称
            if depart.higher_id:
                temp['higher_department'] = Department.objects.get(d_id=depart.higher_id).department
                temp['higher_id'] = depart.higher_id
            else:
                temp['higher_id'] = 0
            # 部门简介
            temp['description'] = depart.description
            departments_list.append(temp)
        # 将部门信息组装成字典格式传至前端
        msg['data'] = departments_list
        return JsonResponse(msg)


def dept_add(request):
    """
    添加部门
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 展示所有部门名称,用于显示上级部门下拉选择框
        departments = Department.objects.filter(is_delete=0)
        return render(request, 'dept/deptAdd.html', {'departments': departments})

    if request.method == 'POST':
        msg = {
            'code': 0,
            'msg': '请求成功'
        }
        data = request.POST.dict()
        # 获取部门编号
        d_num = data.get('department_num')
        # 查询是否已存在此部门
        department = Department.objects.filter(department_num=d_num)
        # 如果存在, 则更改部门信息
        if department:
            department = department.first()
        else:
            # 不存在此部门,则新增一个部门
            department = Department()
        # 保存部门信息
        department.department = data.get('department')
        department.department_num = data.get('department_num')
        department.higher_id = data.get('higher_id')
        department.description = data.get('description')
        department.save()
        return JsonResponse(msg)


def dept_del(request):
    """
    删除部门
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = request.POST.dict()
        # 获取部门编号
        d_num = data.get('department_num')
        # 获取要删除的部门对象
        department = Department.objects.get(department_num=d_num)
        # 更改数据库状态,实现软删除
        department.is_delete = 1
        # 保存更改
        department.save()
        msg = {
            "code": 0,
            "msg": "删除成功",
        }
        return JsonResponse(msg)
