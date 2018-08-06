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
        # 返回json数据
        msg = {
            "code": 0,
            "msg": "",
            "count": len(users),  # 所有部门总数
        }
        for user in users:
            # 循环组装用户json信息
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
    添加/编辑用户
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 添加用户页面渲染岗位
        roles = Role.objects.filter(is_delete=0)
        return render(request, 'user/userAdd.html', {'roles':roles})
    if request.method == 'POST':
        data = request.POST.dict()
        # 通过工号(唯一)查找用户是否存在
        job_number = data['job_number']
        user = User.objects.filter(job_number=job_number).first()
        # 如果不存在，则创建用户
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
        # 获取岗位对象
        role = Role.objects.get(role_id=data['role'])
        if user.user_id:
            # 编辑用户岗位
            # 存在用户则删除表的关联关系
            UserRole.objects.filter(user=user).delete()
        UserRole.objects.create(user=user, role=role)
        # 添加 / 编辑 用户json数据
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
        # 获取顶级部门
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
    """
    部门树
    :param temp:构造部门树字典
    :return:
    """
    # 获取子部门
    child_departs = Department.objects.filter(Q(is_delete=0) & Q(higher_id=temp['id']))
    if child_departs:
        # 如果存在子部门, 循环子部门,存入信息
        child_trees_list = []
        for child_depart in child_departs:
            child_temp = dict()
            child_temp['name'] = child_depart.department
            child_temp['id'] = child_depart.d_id
            child_trees_list.append(child_temp)
            temp['children'] = child_trees_list
            tree(child_temp)


def dept_tree(request):
    """
    构造部门树, 用于部门树显示
    :param request:
    :return:
    """
    if request.method == 'GET':
        trees_list = []
        # 获取顶级部门
        departs = Department.objects.filter(Q(is_delete=0) & Q(higher_id=0))
        if departs:
            for depart in departs:
                temp = dict()
                temp['spread'] = 'true'
                temp['name'] = depart.department
                temp['id'] = depart.d_id
                temp['children'] = []
                # 递归获取子部门
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


def role(request):
    """
    岗位页面
    :param request:
    :return:
    """
    return render(request, 'role/role.html')


def role_list(request):
    if request.method == 'GET':
        roles = Role.objects.filter(is_delete=0)
        roles_list = []
        msg = {
            "code": 0,
            "msg": "",
            "count": len(roles),  # 所有部门总数
        }
        if roles:
            for role in roles:
                role_temp = dict()
                role_temp['post_id'] = role.post_id # 部门编号
                role_temp['post'] = role.post # 部门名称
                role_temp['remark'] = role.remark # 部门名称
                roles_list.append(role_temp)
            msg['data'] = roles_list
        return JsonResponse(msg)

def role_add(request):
    """
    添加/编辑岗位
    :param request:
    :return:
    """
    if request.method == 'GET':
        # 返回添加用户页面
        return render(request, 'role/roleAdd.html')
    if request.method == 'POST':
        data = request.POST.dict()
        # 获取岗位id
        post_id = data['post_id']
        # 获取
        role = Role.objects.filter(post_id=post_id).first()
        if not role:
            role = Role()
        role.post_id = post_id
        role.post = data['post']
        role.remark = data['remark']
        role.save()
        msg = {
            'code':0,
            'msg':'添加成功'
        }
        return JsonResponse(msg)

def role_del(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        role = Role.objects.filter(post_id=post_id).first()
        role.is_delete = 1
        role.save()
        msg = {
            'code':0,
            'msg':'删除成功'
        }
        return JsonResponse(msg)





















