from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Manager Home Page'),
    path('about/', views.about, name='Manager About Page'),
]
