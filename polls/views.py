from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return HttpResponse("Hello World! . You're at the polls index.")


def fuck(request):
    host = request.get_host()
    print('fuck !!!!!')
    return HttpResponse(host)
