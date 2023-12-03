from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

from .gameplay import *

# Create your views here.

class TicTocListView(ListCreateAPIView):
    serializer_class = TicTocSerializer
    queryset = tictocModel.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class TicTocDetailView(RetrieveAPIView):
    serializer_class = TicTocSerializer
    queryset = tictocModel.objects.all()
    lookup_field='id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class StartNewGameAPI(CreateAPIView):
    serializer_class = TicTocSerializer
    queryset = tictocModel.objects.all()

    def post(self, request, *args, **kwargs):
        request.data.update(startNewGame_method())
        return self.create(request, *args, **kwargs)
    

class MoveAPI(CreateAPIView):
    serializer_class = TicTocSerializer
    queryset = tictocModel.objects.all()

    def post(self, request, *args, **kwargs):
        last_move = self.queryset.latest('id')

        request.data.update(PlayerMove(
            board=last_move.board,
            action=request.data.get('action'),
            letter=request.data.get('letter'),
        ))
        return self.create(request, *args, **kwargs)