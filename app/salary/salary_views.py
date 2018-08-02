from django.http import JsonResponse
from django.shortcuts import render

from app.models import Salary


def pay_salary(request):
    """工资展示页面"""
    if request.method == 'GET':
        return render(request, 'salary/pay_salary.html')


def salary(request):
    """工资展示接口"""
    if request.method == 'GET':
        salary_info = Salary.objects.all()

        data = {
            'salary_info': [i.to_dict() for i in salary_info]
        }
        count = 0
        if salary_info:
            for i in salary_info:
                count += 1
        return JsonResponse({'code': 0, 'msg': '成功', 'count': count, 'data': data['salary_info']})


def check_salary(request):
    """工资详情页面"""
    if request.method == 'GET':
        return render(request, 'salary/check_salary.html')



