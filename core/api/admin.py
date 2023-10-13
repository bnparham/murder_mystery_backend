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


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(BankAccount)
class BankaccountAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'person_id']


@admin.register(AtmTransaction)
class AtmTransactionAdmin(admin.ModelAdmin):
    list_display = ['account_number', 'atm_location', 'amount']


@admin.register(SecurityLog)
class SecurityLogAdmin(admin.ModelAdmin):
    list_display = ['license_plate', 'street_id', 'activity', 'date', 'time']


@admin.register(CrimeSceneReport)
class CrimeSceneReportAdmin(admin.ModelAdmin):
    list_display = ['location_id', 'description', 'date']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Clue)
class ClueAdmin(admin.ModelAdmin):
    list_display = ['crime_id', 'item_id']


@admin.register(Airports)
class AirportsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'city']


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ['origin_airport_id', 'destination_airport_id', 'date', 'time']


@admin.register(Passengers)
class PassengersAdmin(admin.ModelAdmin):
    list_display = ['flight_id', 'person_id', 'seat']


@admin.register(Interviews)
class InterviewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'street_id', 'transcript', 'date']


@admin.register(MessageBox)
class MessageBoxAdmin(admin.ModelAdmin):
    list_display = ['person_id', 'body', 'date']


@admin.register(PlayerReply)
class PlayerReplyAdmin(admin.ModelAdmin):
    list_display = ['message_id', 'body']


@admin.register(NpcReply)
class NpcReplyAdmin(admin.ModelAdmin):
    list_display = ['PlayerReply_id', 'body']
