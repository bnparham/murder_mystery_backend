from django.shortcuts import render
from rest_framework import generics
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
    queryset = SecurityLog.objects.all()

class CrimeSceneReportApi(generics.ListAPIView):
    serializer_class = CrimeSceneReportSerializer
    queryset = CrimeSceneReport.objects.all()

class ItemApi(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()

class EvidenceApi(generics.ListAPIView):
    serializer_class = ClueSerializer
    queryset = Clue.objects.all()

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

