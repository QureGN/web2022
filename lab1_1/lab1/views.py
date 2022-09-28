from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse

# def hello(request):
#     return HttpResponse('Hello world!')

from datetime import date

def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Услуги', 'id': 1},
            {'title': 'Сотрудники', 'id': 2},
            {'title': 'Пользователи', 'id': 3},
            {'title': 'Животные', 'id': 4},
        ]
    }})

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'description':[{'title':'Хирургия','id': 1},
                       {'title': 'Врач','id': 2},
                       {'title': 'Бубенко','id': 3},
                       {'title': 'Мейн-кун','id': 4}]
    }})
# Create your views here.
