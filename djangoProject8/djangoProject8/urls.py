"""djangoProject8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bmstu import views
urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('services/', views.services, name = 'services'),
    path('users/', views.users, name='users'),
    path('pets/', views.userpets, name='pets'),
    path('user/<int:id>/', views.userpets, name = 'user_url'),
    path('services/<int:id>/', views.description, name = 'description_url'),
    path('reception/', views.schedule, name = 'reception'),

]
