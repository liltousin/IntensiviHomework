# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def item_list(request):
    return HttpResponse('Список элементов')


def item_detail(request, pk: int):
    return HttpResponse('Подробно элемент')
