import json

from django.http import JsonResponse
from django.shortcuts import render

from app.models import Menu


def menu_list(request):
    """菜单列表"""
    if request.method == 'GET':
        return render(request, 'menu/menuList.html')


def add_menu(request):
    """添加菜单"""
    if request.method == 'GET':
        return render(request, 'menu/menuAdd.html')



def menu_json_list(request):

    return JsonResponse('404')
