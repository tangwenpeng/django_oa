from django.http import JsonResponse
from django.shortcuts import render

from app.models import Department


def user_list(request):
    """
    显示用户页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'user/userList.html')


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


def dept_list(request):
    """
    显示部门页面
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'dept/deptList.html')


def dept(request):
    if request.method == 'GET':
        departments = Department.objects.filter(is_delete=0)
        departments_list = []
        msg = {
            "code": 0,
            "msg": "",
            "count": len(departments),
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

        msg['data'] = departments_list
        return JsonResponse(msg)


def dept_add(request):
    """
    添加部门
    :param request:
    :return:
    """
    if request.method == 'GET':
        departments = Department.objects.filter(is_delete=0)

        return render(request, 'dept/deptAdd.html', {'departments': departments})
    if request.method == 'POST':
        msg = {
            'code': 0,
            'msg': '请求成功'
        }
        data = request.POST.dict()
        d_num = data.get('department_num')
        department = Department.objects.filter(department_num=d_num)
        if department:
            department = department.first()
        else:
            department = Department()
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
        d_num = data.get('department_num')
        department = Department.objects.get(department_num=d_num)
        department.is_delete = 1
        department.save()
        msg = {
            "code": 0,
            "msg": "",
        }
        return JsonResponse(msg)
