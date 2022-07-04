from django.contrib import admin
from django.urls import path, re_path
from .views import NewAccountView, SignInView, coordinator_simulator, coordinator_team, coordinator_tickets, coordinator_statistics, coordinator_profile, coordinator_password
from . import views
urlpatterns = [
     path('', views.index, name='index'),
     path('about', views.about, name='about'),
     path('support', views.support, name='support'),
     path('demo', views.demo_dashboard, name='demo_dashboard'),
     path('new-account', NewAccountView.as_view({
         'get': 'get',
         'post': 'post'
     }), name='new_account'),
     path('sign-in', SignInView.as_view({
          'get': 'get',
          'post': 'post'
     }), name='sign_in'),
     path('logout', views.logout, name='logout'),
     path('coordinator', views.coordinator, name='coordinator'),
     path('coordinator/simulator', views.coordinator_simulator, name='coordinator_simulator'),
     path('coordinator/team', views.coordinator_team, name='coordinator_team'),
     path('coordinator/tickets', views.coordinator_tickets, name='coordinator_tickets'),
     path('coordinator/profile', views.coordinator_profile, name='coordinator_profile'),
     path('coordinator/password', views.coordinator_password, name='coordinator_password'),
     path('coordinator/statistics', views.coordinator_statistics, name='coordinator_statistics'),
     path('employee', views.employee, name='employee'),
]
