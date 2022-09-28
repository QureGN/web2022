from django.shortcuts import render
from django.shortcuts import render
from bmstu.models import User
from bmstu.models import Pets
from bmstu.models import Services
from bmstu.models import Sign_up
from bmstu.models import Schedule
from django.http import HttpResponse

menu= [{'title':"Услуги",'url_name':'services'},
       {'title': "Личный кабинет", 'url_name': 'users'},
       {'title': "Записаться", 'url_name': 'reception'}]

def home(request):
    return render(request, 'home.html', {'data': {
        'menu': menu
    }})

def users(request):
    return render(request, 'users.html', {'data': {
        'users': User.objects.all(),
        'menu':  menu
    }})
def userpets(request, id):
    return render(request, 'userpet.html', {'data': {
        'user': User.objects.filter(id=id)[0],
        'pet': Pets.objects.filter(owner=id),
        'menu': menu
    }})

def services(request):
    return render(request, 'services.html', {'data': {
        'services': Services.objects.all(),
        'menu': menu
    }})

def description(request, id):
    return render(request, 'description.html', {'data': {
        'service': Services.objects.filter(id=id)[0],
        'menu': menu
    }})

def schedule(request):
    return render(request, 'reception.html', {'data': {
        'schedule': Schedule.objects.all(),
        'menu': menu
    }})


# Create your views here.
