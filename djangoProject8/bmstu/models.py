from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    phone = models.CharField(max_length= 20)
    login = models.CharField(max_length= 100)
    password = models.CharField(max_length= 100)

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Services(models.Model):
    service = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'services'
        verbose_name = "Сервис"
        verbose_name_plural = "Сервисы"


class Pets(models.Model):
    owner = models.ForeignKey(User, on_delete = models.CASCADE)
    type = models.CharField(max_length=20)
    sex = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    year = models.DateField()

    class Meta:
        managed = False
        db_table = 'pets'
        verbose_name = "Животное"
        verbose_name_plural = "Животные"


class Schedule(models.Model):
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'schedule'
        verbose_name = "Расписание"
        verbose_name_plural = "Расписания"


class Sign_up(models.Model):
    time1 = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    client_user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_pet = models.ForeignKey(Pets, on_delete=models.CASCADE)
    service1 = models.ForeignKey(Services, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'sign_up'
# Create your models here.
