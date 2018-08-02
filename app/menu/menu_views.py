from rest_framework import viewsets
from app.menu.serializers import MenuSerializer
from app.models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
