from django.contrib import admin
from django.urls import path,include
from .views import *
from .views import Datascience
from.views import Destination

urlpatterns = [
    path('Datascience/',Datascience.as_view()),
    path('Datascience/<str:account_name>/', Datascience.as_view() , name='Datascience-detail'),
    path('Datascience/delete/<str:account_name>/', Datascience.as_view(), name='Datascience/delete'),
    path('destination/destinations/<int:account_id>/', Destination.as_view(), name='destination/destinations'),
    path('server/incoming_data/', IncomingDataAPIView.as_view(), name='incoming-data'),
]