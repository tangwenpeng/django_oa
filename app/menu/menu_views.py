from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from app.menu.serializers import MenuSerializer
from app.models import Menu
from app.plugin.auth.permissions import check_permission


# @check_permission
class MenuViewSet(APIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self, request):
        menu_list = MenuSerializer(self.queryset)
        return Response(menu_list.data)