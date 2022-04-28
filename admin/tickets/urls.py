from django.contrib import admin
from django.urls import path
from .views import TicketViewSet, UserAPIView
urlpatterns = [
    path('tickets', TicketViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('tickets/<str:pk>', TicketViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', UserAPIView.as_view()),
]
