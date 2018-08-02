from django.conf.urls import url

from app import views
from app.menu import menu_views
from app.salary import salary_views
from app.user import user_views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^pay_salary/', salary_views.pay_salary, name='pay_salary'),
    # 薪资模块
    url(r'^salary/', salary_views.salary, name='salary'),
    url(r'check_salary/', salary_views.check_salary, name='check_salary'),

    # 用户模块
    url(r'^user/$', user_views.user, name='user'),
    url(r'^user_list/$', user_views.user_list, name='user_list'),
    url(r'^user_add/$', user_views.user_add, name='user_add'),
    url(r'^user_info/$', user_views.user_info, name='user_info'),

    # 部门模块
    url(r'^dept/$', user_views.dept, name='dept'),  # 部门页面
    url(r'^dept_list/$', user_views.dept_list, name='dept_list'),  # 部门信息
    url(r'^dept_add/$', user_views.dept_add, name='dept_add'),  # 添加部门
    url(r'^dept_del/$', user_views.dept_del, name='dept_del'),  # 部门详细信息

    url(r'^menu_list/', menu_views.menu_list, name='menu_list'),
    url(r'^add_menu/', menu_views.add_menu, name='add_menu'),
    url(r'^menu_json_list/', menu_views.menu_json_list, name='menu_json_list')

]

