from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Home, Menu

def home(request):
    data = Home.objects.all()
    template = loader.get_template('menu.html')
    print(data)
    context = {
        'contoh': 'uji coba nanti mau diganti',
        'home': data
    }
    return HttpResponse(template.render(context, request))

def menu(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())