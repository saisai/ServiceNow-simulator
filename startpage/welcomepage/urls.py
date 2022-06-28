from django.contrib import admin
from django.urls import path
from .views import NewAccountView, SignInView, UserView, LogoutView
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
     path('dashboard-coordinator/<str:user>', views.dashboard_coordinator, name='dashboard_coordinator'),
     path('dashboard-employee', views.dashboard_employee, name='dashboard_employee'),
     path('account-profile', views.account, name='account'),
]
