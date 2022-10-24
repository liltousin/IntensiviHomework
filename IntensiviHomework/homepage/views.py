# from django.shortcuts import render

# Create your views here.

from http import HTTPStatus

from django.http import HttpResponse


def home(request):
    return HttpResponse('Главная', status=HTTPStatus.IM_A_TEAPOT)
