from django.urls import path
from .views import *

urlpatterns = [
    path('person/',PersonApi.as_view(),name='person'),
    path('phone-calls/', PhoneCallsApi.as_view(), name='phone-calls'),
    path('location/', LocationApi.as_view(), name="location"),
    path('street/', StreetApi.as_view(), name="street"),
    path('bank-account/', BankAccountApi.as_view(), name="bank-account"),
    path('atm/', AtmTransactionApi.as_view(), name="atm"),
    path('security-log/', SecurityLogApi.as_view(), name="security-log"),
    path('cime-scene/', CrimeSceneReportApi.as_view(), name="cime-scene"),
    path('item/', ItemApi.as_view(), name="item"),
    path('evidence/', EvidenceApi.as_view(), name="evidence"),
    path('airports/', AirportsApi.as_view(), name="airports"),
    path('flights/', FlightsApi.as_view(), name="flights"),
    path('passengers/', PassengersApi.as_view(), name="passengers"),
    path('interviews/', InterviewsApi.as_view(), name="interviews"),
    path('messageBox/', MessageBoxApi.as_view(), name="messageBox"),
    path('player-reply/', PlayerReplyApi.as_view(), name="player-reply"),
    path('npc-reply/', NpcReplyApi.as_view(), name="npc-reply"),
]
