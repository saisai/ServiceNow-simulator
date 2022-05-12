from django.shortcuts import render
from .models import CoordinatorRegistration

def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def support(request):
    return render(request, 'contact.html')


def demo_dashboard(request):
    return render(request, 'demo.html')


def coordinator_new_account(request):
    if request.method == "POST":
        if (
                request.POST.get("firstName")
                and request.POST.get("lastName")
                and request.POST.get("email")
                and request.POST.get("password1")
                == request.POST.get("password2")
        ):
            # saverecord = CoordinatorRegistration()
            # saverecord.name = request.POST.get("firstName")
            # saverecord.surname = request.POST.get("lastName")
            # saverecord.email = request.POST.get("email")
            # saverecord.password = request.POST.get("password1")
            # saverecord.save()
            print(request.POST.get("firstName"))
    return render(request, 'auth-register-coordinator.html')


def coordinator_sign_in(request):
    return render(request, 'auth-login-coordinator.html')


def employee_new_account(request):
    if request.method == "POST":
        if (
                request.POST.get("firstName")
                and request.POST.get("lastName")
                and request.POST.get("email")
                and request.POST.get("password1")
                == request.POST.get("password2")
        ):
            # saverecord = EmployeeRegistration()
            # saverecord.name = request.POST.get("firstName")
            # saverecord.surname = request.POST.get("lastName")
            # saverecord.email = request.POST.get("email")
            # saverecord.password = request.POST.get("password1")
            # saverecord.save()
            print(request.POST.get("firstName"))
    return render(request, 'auth-register-employee.html')


def employee_sign_in(request):
    return render(request, 'auth-login-employee.html')
