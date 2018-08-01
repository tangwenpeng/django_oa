from rest_framework import viewsets
from .serializers import MenuSerializer
from .models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
