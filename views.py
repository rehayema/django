'''
Return content using HttpResponse
'''
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")

def rehayema(request):
    return HttpResponse("Hello, Rehayema!")

# return dynamic page based on data in url
def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")