from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'passport_number', 'license_plate']

@admin.register(PhoneCalls)
class PhoneCallsAdmin(admin.ModelAdmin):
    list_display = ['caller', 'reciver', 'date', 'duration']

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']