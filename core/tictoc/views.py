from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework import status

from .serializers import *

from .gameplay import *
from .ai import actions


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

        # first player should play then ai play
        if request.data.get('letter') == 'X' :
            playerMove = PlayerMove(
                board=last_move.board,
                action=request.data.get('action'),
                letter=request.data.get('letter'),
            )

            # check actions
            if len(actions(extractBoard(last_move.board))) > 1 :
                aiMove = PlayerMove(
                    board=playerMove['board'],
                    action=playerMove['action'],
                    letter=request.data.get('letter'),
                )
            else :
                # we are in last move and there is one empty slot.
                aiMove = playerMove

            request.data.update(aiMove)
        # first ai should play (as X), then when player insert data, ai result will appear too
        else :
            # check we are in init game status :
            if last_move == initial_state() :
                aiMove = PlayerMove(
                board=last_move.board,
                action=request.data.get('action'),
                letter=request.data.get('letter'),
            )
            else :
                # now we can play and after that ai playing too
                playerMove = PlayerMove(
                board=last_move.board,
                action=request.data.get('action'),
                letter=request.data.get('letter'),
                )
                aiMove = PlayerMove(
                    board=playerMove['board'],
                    action=playerMove['action'],
                    letter=request.data.get('letter'),
                )

            request.data.update(aiMove)

        return self.create(request, *args, **kwargs)
    

class LastSessionAPI(ListAPIView):
    serializer_class = TicTocSerializer

    def get_queryset(self):
        # Customize the queryset to get the last item
        return tictocModel.objects.order_by('-id')[:1]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)