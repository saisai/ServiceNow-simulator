from django.contrib import admin
from django.urls import path
from .views import TicketViewSet, HomeView
from . import views

urlpatterns = [
    path('tickets', TicketViewSet.as_view({
        'get': 'list'
    })),
    path('tickets/<str:pk>', TicketViewSet.as_view({
        'get': 'retrieve',
        'put': 'update'
    })),
    path('dashboard-employee', HomeView.as_view({
        'get': 'get',
    }), name='home'),
    path('logout', views.logout, name='logout'),
]
