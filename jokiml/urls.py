from django.urls import path
from . import views

urlpatterns = [
    path('jokiml/', views.jokiml, name='jokiml'),
]