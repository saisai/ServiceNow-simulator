from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from .views import TicketViewSet, HomeView, account
from . import views
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
    url(r'dashboard-coordinator/$', HomeView.as_view({
        'get': 'get',
    })),
    path('logout', views.logout, name='logout'),
    path('dashboard-coordinator', views.account, name='account'),
]
