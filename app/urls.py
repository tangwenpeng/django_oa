from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from app import views
from app.salary import salary_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^pay_salary/', salary_views.pay_salary, name='pay_salary'),
    # 薪资展示接口
    url(r'^salary/', salary_views.salary, name='salary'),

]


