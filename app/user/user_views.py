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
        msg = {
            "code": 0,
            "msg": "",
            "count": 3,
        }


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
            'code': 200,
            'msg': '请求成功'
        }
        data = request.POST.dict()
        department = Department()
        department.department = data.get('department')
        department.department_num = data.get('department_num')
        department.higher_id = data.get('higher_id')
        department.description = data.get('description')
        department.save()
        return JsonResponse(msg)


def dept_info(request):
    """
    显示用户部门
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'dept/deptInfo.html')
