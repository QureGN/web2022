from stocks.models import User, Sign_up, Services
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = User
        # Поля, которые мы сериализуем
        fields = ["pk", "username", "phone", "login", "password"]

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Services
        # Поля, которые мы сериализуем
        fields = ["pk", "service", "description"]

class Sign_upSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Sign_up
        # Поля, которые мы сериализуем
        fields = ["pk", "time1", "date1", "service1", "client_user"]


