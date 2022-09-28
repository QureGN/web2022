from django.contrib import admin
from .models import User, Services,Pets, Schedule
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'service')
    list_display_links = ('id', 'service')

admin.site.register(Services, ServicesAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_display_links = ('id', 'username')

admin.site.register( User, UserAdmin)

class PetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'species')
    list_display_links = ('id', 'species')

admin.site.register( Pets, PetsAdmin)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'time')
    list_display_links = ('id', 'time')

admin.site.register( Schedule, ScheduleAdmin)

# Register your models here.
