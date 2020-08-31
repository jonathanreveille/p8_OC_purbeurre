from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello world, this is project 8 of OC Python course")