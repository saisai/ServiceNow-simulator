from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def coordinator_new_account(request):
    return render(request, 'auth-register-coordinator.html')


def coordinator_sign_in(request):
    return render(request, 'auth-login-coordinator.html')


def employee_new_account(request):
    return render(request, 'auth-register-employee.html')


def employee_sign_in(request):
    return render(request, 'auth-login-employee.html')
