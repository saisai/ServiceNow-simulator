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

     path('dashboard', UserView.as_view()),
     path('logout', LogoutView.as_view()),
]
