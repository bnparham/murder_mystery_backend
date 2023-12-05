from rest_framework import serializers
from .models import *

class TicTocSerializer(serializers.ModelSerializer):
    class Meta:
        model = tictocModel
        fields = '__all__'
        depth = 1
