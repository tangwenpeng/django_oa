from django.conf.urls import url

from app import views
from app.meeting import meeting_views
from app.menu import menu_views
from app.salary import salary_views
from app.user import user_views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^pay_salary/', salary_views.pay_salary, name='pay_salary'),
    # 薪资模块
    url(r'^salary/', salary_views.salary, name='salary'),
    url(r'check_salary/', salary_views.check_salary, name='check_salary'),
    url(r'change_status/', salary_views.change_status, name='change_status'),


    # 用户模块
    url(r'^user/$', user_views.user, name='user'), # 用户页面
    url(r'^user_list/$', user_views.user_list, name='user_list'), # 用户信息
    url(r'^user_add/$', user_views.user_add, name='user_add'), # 添加用户
    url(r'^user_info/$', user_views.user_info, name='user_info'),
    url(r'^user_del/$', user_views.user_del, name='user_del'),

    # 部门模块
    url(r'^dept/$', user_views.dept, name='dept'),  # 部门页面
    url(r'^dept_list/$', user_views.dept_list, name='dept_list'),  # 部门信息
    url(r'^dept_add/$', user_views.dept_add, name='dept_add'),  # 添加部门
    url(r'^dept_del/$', user_views.dept_del, name='dept_del'),  # 部门详细信息
    url(r'^dept_tree/$', user_views.dept_tree, name='dept_tree'),  # 部门详细信息

    # 岗位管理
    url(r'^role/$', user_views.role, name='role'),  # 岗位页面
    url(r'^role_list/$', user_views.role_list, name='role_list'),  # 岗位信息
    url(r'^role_add/$', user_views.role_add, name='role_add'),  # 添加岗位
    url(r'^role_del/$', user_views.role_del, name='role_del'),  # 删除岗位





    url(r'^menu_list/', menu_views.menu_list, name='menu_list'),
    url(r'^add_menu/', menu_views.add_menu, name='add_menu'),
    url(r'^menu_json_list/', menu_views.menu_json_list, name='menu_json_list'),

    # 会议模块
    url(r'my_meeting/$', meeting_views.my_meeting, name='my_meeting'),  # 我的会议页面
    url(r'meeting_list/$', meeting_views.meeting_list, name='meeting_list'),  # 我的会议信息
    url(r'meeting_appointment/$', meeting_views.meeting_appointment, name='meeting_appointment'),  # 会议预约

]

