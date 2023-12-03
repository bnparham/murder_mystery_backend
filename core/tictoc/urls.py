from django.urls import path
from .views import *

urlpatterns = [
    path('list',TicTocListView.as_view(),name='tictoc'),
    path('list/<id>',TicTocDetailView.as_view(),name='tictoc'),
    path('startNewGame', StartNewGameAPI.as_view(), name='startNewGame'),
    path('PlayerMoveAPI', MoveAPI.as_view(), name='playermove'),
]
