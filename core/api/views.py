from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import *
from .models import *

class PersonApi(generics.ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PhoneCallsApi(generics.ListAPIView):
    serializer_class = PhoneCallsSerializer
    queryset = PhoneCalls.objects.all()

class LocationApi(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class StreetApi(generics.ListAPIView):
    serializer_class = StreetSerializer
    queryset = Street.objects.all()

class BankAccountApi(generics.ListAPIView):
    serializer_class = BankAccountSerializer
    queryset =BankAccount.objects.all()

class AtmTransactionApi(generics.ListAPIView):
    serializer_class = AtmTransactionSerializer
    queryset = AtmTransaction.objects.all()

class SecurityLogApi(generics.ListAPIView):
    serializer_class = SecurityLogSerializer
    queryset = SecurityLog.objects.all().select_related('license_plate')
    filter_backends = (filters.SearchFilter, )
    search_fields = ('street_id__name',)

class CrimeSceneReportApi(generics.ListAPIView):
    serializer_class = CrimeSceneReportSerializer
    queryset = CrimeSceneReport.objects.all().select_related('location_id')
    filter_backends = (filters.SearchFilter, )
    search_fields = ('description','date','street_id',)
    
class ItemApi(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class ClueApi(generics.ListAPIView):
    serializer_class = ClueSerializer
    queryset = Clue.objects.all().select_related('crime_id')
    filter_backends = (filters.SearchFilter,)
    # search field by foreignKey should use __ after key name and then select attribue of model
    search_fields = ('crime_id__id',)

class AirportsApi(generics.ListAPIView):
    serializer_class = AirportsSerializer
    queryset = Airports.objects.all()

class FlightsApi(generics.ListAPIView):
    serializer_class = FlightsSerializer
    queryset = Flights.objects.all()

class PassengersApi(generics.ListAPIView):
    serializer_class = PassengersSerializer
    queryset = Passengers.objects.all()

class InterviewsApi(generics.ListAPIView):
    serializer_class = InterviewsSerializer
    queryset = Interviews.objects.all()

class MessageBoxApi(generics.ListAPIView):
    serializer_class = MessageBoxSerializer
    queryset = MessageBox.objects.all()

class PlayerReplyApi(generics.ListAPIView):
    serializer_class = PlayerReplySerializer
    queryset = PlayerReply.objects.all()

class NpcReplyApi(generics.ListAPIView):
    serializer_class = NpcReplySerializer
    queryset = NpcReply.objects.all()

