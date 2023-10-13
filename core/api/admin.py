from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'passport_number', 'license_plate']


@admin.register(PhoneCalls)
class PhoneCallsAdmin(admin.ModelAdmin):
    list_display = ['id', 'caller', 'reciver', 'date', 'duration']


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(BankAccount)
class BankaccountAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_number', 'person_id']


@admin.register(AtmTransaction)
class AtmTransactionAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_number', 'atm_location', 'amount']


@admin.register(SecurityLog)
class SecurityLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'license_plate', 'street_id', 'activity', 'date', 'time']


@admin.register(CrimeSceneReport)
class CrimeSceneReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'location_id', 'description', 'date']


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Clue)
class ClueAdmin(admin.ModelAdmin):
    list_display = ['id', 'crime_id', 'item_id']


@admin.register(Airports)
class AirportsAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'city']


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ['id', 'origin_airport_id', 'destination_airport_id', 'date', 'time']


@admin.register(Passengers)
class PassengersAdmin(admin.ModelAdmin):
    list_display = ['id', 'flight_id', 'person_id', 'seat']


@admin.register(Interviews)
class InterviewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'street_id', 'transcript', 'date']


@admin.register(MessageBox)
class MessageBoxAdmin(admin.ModelAdmin):
    list_display = ['id', 'person_id', 'body', 'date']


@admin.register(PlayerReply)
class PlayerReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'message_id', 'body']


@admin.register(NpcReply)
class NpcReplyAdmin(admin.ModelAdmin):
    list_display = ['id', 'PlayerReply_id', 'body']
