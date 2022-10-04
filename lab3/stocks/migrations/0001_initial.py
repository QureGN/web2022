# Generated by Django 4.1.1 on 2022-10-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20, verbose_name='Тип')),
                ('sex', models.CharField(max_length=100, verbose_name='Пол')),
                ('species', models.CharField(max_length=100, verbose_name='Порода')),
                ('year', models.DateField(verbose_name='Год рождения')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
                'db_table': 'pets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=30, verbose_name='Услуга')),
                ('description', models.CharField(max_length=100, verbose_name='Описание услуги')),
            ],
            options={
                'verbose_name': 'Сервис',
                'verbose_name_plural': 'Сервисы',
                'db_table': 'services',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sign_up',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time1', models.CharField(max_length=10, verbose_name='Назначенное время')),
                ('date1', models.DateField(verbose_name='Назначенная дата')),
            ],
            options={
                'verbose_name': 'Животное',
                'verbose_name_plural': 'Животные',
                'db_table': 'pets',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='Пользователь')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон пользователя')),
                ('login', models.CharField(max_length=100, verbose_name='Логин')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]