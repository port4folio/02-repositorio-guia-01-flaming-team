from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def v1_inicio(request):
    return HttpResponse("<h1>Vista 1 App </h1>"
    "<p>Todo a tu alcance</p>" );

def v2_inicio(request):
    return HttpResponse("<h1> Vista 2 App </h1>"
    "<p>Todo a tu alcance</p>" );