from django.contrib import admin
from django.urls import path, re_path
from .views import NewAccountView, SignInView, coordinator_team, coordinator_tickets, \
     coordinator_statistics, coordinator_profile, coordinator_password, employee_profile, employee_password, ticket_creating, queue_creating, profile_update
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
     path('coordinator/team', views.coordinator_team, name='coordinator_team'),
     path('coordinator/tickets', views.coordinator_tickets, name='coordinator_tickets'),
     path('coordinator/profile', views.coordinator_profile, name='coordinator_profile'),
     path('coordinator/password', views.coordinator_password, name='coordinator_password'),
     path('coordinator/statistics', views.coordinator_statistics, name='coordinator_statistics'),
     path('employee', views.employee, name='employee'),
     path('employee/simulator', views.employee_simulator, name='employee_simulator'),
     path('employee/profile', views.employee_profile, name='employee_profile'),
     path('employee/password', views.employee_password, name='employee_password'),
     path('coordinator/ticket_creating', views.ticket_creating, name='ticket_creating'),
     path('coordinator/queue_creating', views.queue_creating, name='queue_creating'),
     path('coordinator/profile_update', views.profile_update, name='profile_update'),
]
