# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request, pk):
    return HttpResponse(f'Главная {pk}')