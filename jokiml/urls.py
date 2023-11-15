from django.urls import path
from . import views

urlpatterns = [
    path('', views.jokiml, name='jokiml'),
    path('menu/', views.menu, name='menu'),
]