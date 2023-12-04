from django.urls import path
from .views import *

urlpatterns = [
    path('list',TicTocListView.as_view(),name='tictoc'),
    path('list/<id>',TicTocDetailView.as_view(),name='tictoc'),
    path('startnewgame', StartNewGameAPI.as_view(), name='startNewGame'),
    path('moveapi', MoveAPI.as_view(), name='playermove'),
    path('lastsessionapi', LastSessionAPI.as_view(), name='lastSession'),
]
