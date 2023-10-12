from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class PhoneCallsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneCalls
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = '__all__'

class AtmTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtmTransaction
        fields = '__all__'

class SecurityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecurityLog
        fields = '__all__'

class CrimeSceneReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrimeSceneReport
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ClueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clue
        fields = '__all__'

class AirportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airports
        fields = '__all__'

class FlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flights
        fields = '__all__'

class PassengersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passengers
        fields = '__all__'

class InterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviews
        fields = '__all__'

class MessageBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageBox
        fields = '__all__'

class PlayerReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = player_reply
        fields = '__all__'

class NpcReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = npc_reply
        fields = '__all__'