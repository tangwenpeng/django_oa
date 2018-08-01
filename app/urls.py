from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from app import views
from app.salary import salary_views
from app.menu.menu_views import MenuViewSet

router = SimpleRouter()
router.register(r'^menu', MenuViewSet, base_name='menu')
urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^pay_salary/', salary_views.pay_salary, name='pay_salary'),
    # 薪资展示接口
    url(r'^salary/', salary_views.salary, name='salary'),

]
urlpatterns += router.urls

