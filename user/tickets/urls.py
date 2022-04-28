from django.contrib import admin
from django.urls import path
from .views import TicketViewSet
urlpatterns = [
    path('tickets', TicketViewSet.as_view({
        'get': 'list'
    })),
    path('tickets/<str:pk>', TicketViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    })),
]
