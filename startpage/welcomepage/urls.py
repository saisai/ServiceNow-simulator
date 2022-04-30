from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('coordinator/new-account', views.coordinator_new_account, name='coordinator_new_account'),
    path('coordinator/sign-in', views.coordinator_sign_in, name='coordinator_sign_in'),
    path('employee/new-account', views.employee_new_account, name='employee_new_account'),
    path('employee/sign-in', views.employee_sign_in, name='employee_sign_in'),

]
