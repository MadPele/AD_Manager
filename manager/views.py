from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    metadata = {
        'title': 'Home'
    }
    return render(request, 'manager/home.html', metadata)


def about(request):
    metadata = {
        'title': 'About'
    }
    return render(request, 'manager/about.html', metadata)

