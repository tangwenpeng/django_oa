from django.db.models import Q
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
            temp['user_id'] = user.user_id
            temp['name'] = user.name
            temp['password'] = user.password
            temp['sex'] = '男' if user.sex else '女'
            temp['job_number'] = user.job_number
            temp['department'] = Department.objects.get(d_id=user.d_id).department
            temp['d_id'] = user.d_id
            temp['email'] = user.email
            temp['phone'] = user.phone
            temp['role'] = user.role.first().post if user.role.all() else None
            temp['role_id'] = user.role.first().role_id if user.role.all() else None
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
        roles = Role.objects.filter(is_delete=0)
        return render(request, 'user/userAdd.html', {'roles':roles})
    if request.method == 'POST':
        data = request.POST.dict()
        job_number = data['job_number']
        user = User.objects.filter(job_number=job_number).first()
        if not user:
            user = User()
        user.name = data['name']
        user.password = data['password']
        user.sex = data['sex']
        user.phone = data['phone']
        user.office_phone = data['office_phone']
        user.email = data['email']
        department = Department.objects.get(d_id = data['department'])
        user.d = department
        user.save()
        role = Role.objects.get(role_id=data['role'])
        if user.user_id:
            UserRole.objects.filter(user=user).delete()
        UserRole.objects.create(user=user, role=role)

        msg = {
            'code' : 0,
            'msg' : '添加成功'
        }
        return JsonResponse(msg)

def user_del(request):
    """
    删除用户
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = request.POST.dict()
        # 获取用户编号
        job_no = data.get('job_no')
        # 获取要删除的用户对象
        user = User.objects.get(job_number=job_no)
        # 更改数据库状态,实现软删除
        user.is_delete = 1
        # 保存更改
        user.save()
        msg = {
            "code": 0,
            "msg": "删除成功",
        }
        return JsonResponse(msg)

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
            # 部门id
            temp['d_id'] = depart.d_id
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

def tree(temp):
    child_departs = Department.objects.filter(Q(is_delete=0) & Q(higher_id=temp['id']))
    if child_departs:
        child_trees_list = []
        for child_depart in child_departs:
            child_temp = dict()
            child_temp['name'] = child_depart.department
            child_temp['id'] = child_depart.d_id
            child_trees_list.append(child_temp)
            temp['children'] = child_trees_list
            tree(child_temp)


def dept_tree(request):
    if request.method == 'GET':
        trees_list = []
        departs = Department.objects.filter(Q(is_delete=0) & Q(higher_id=0))
        if departs:
            for depart in departs:
                temp = dict()
                temp['spread'] = 'true'
                temp['name'] = depart.department
                temp['id'] = depart.d_id
                temp['children'] = []
                tree(temp)
                trees_list.append(temp)
        return JsonResponse(trees_list,safe=False)




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
        d_id = data.get('d_id')
        # 查询是否已存在此部门
        department = Department.objects.filter(d_id=d_id)
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
