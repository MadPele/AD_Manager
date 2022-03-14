from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Manager Home Page</h1>')


def about(request):
    return HttpResponse('<h1>Manager About Page</h1>')
