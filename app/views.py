from django.shortcuts import render

# Create your views here.

'''
首页
'''


def index(request):
    """"""
    if request.method == 'GET':
        return render(request, 'index.html')
