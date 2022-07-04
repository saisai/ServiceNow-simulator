from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.utils.http import urlencode
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpResponseRedirect, HttpResponse
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
import jwt, datetime
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect



def index(request):
    return render(request, 'core/index.html')


def about(request):
    return render(request, 'core/about.html')


def support(request):
    return render(request, 'core/contact.html')


def demo_dashboard(request):
    return render(request, 'core/demo.html')


def sign_in(request):
    return render(request, 'core/auth-login.html')


class NewAccountView(viewsets.ViewSet):
    def post(self, request):
        is_coordinator=0
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            is_coordinator = request.POST.getlist('is_coordinator')
            serializer.save()
            messages.success(request, 'Your account has been created')
            return HttpResponseRedirect('/sign-in')
        else:
            messages.error(request, 'Error! User already exists')
            return render(request, 'core/auth-register.html')

    def get(self, request):
        return render(request, 'core/auth-register.html')


class SignInView(viewsets.ViewSet):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            messages.error(request, 'User not found. Please try again')
            return HttpResponseRedirect('/sign-in')

        if not user.check_password(password):
            messages.error(request, 'Invalid password. Please try again')
            return HttpResponseRedirect('/sign-in')

        login(request, user)
        if user.is_coordinator:
            return redirect('/coordinator')
        else:
            return redirect('/employee')

    def get(self, request):
        return render(request, 'core/auth-login.html')


class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return render(request, 'core/auth-login.html')

# ================================================================ #
@login_required(login_url="/sign-in")
def coordinator(request):
    return render(request, 'coordinator/home-coordinator.html')


@login_required(login_url="/sign-in")
def coordinator_simulator(request):
    pass


@login_required(login_url="/sign-in")
def coordinator_team(request):
    return render(request, 'coordinator/coordinator-management-list.html')


@login_required(login_url="/sign-in")
def coordinator_tickets(request):
    return render(request, 'coordinator/coordinator-create-ticket.html')


@login_required(login_url="/sign-in")
def coordinator_statistics(request):
    pass


@login_required(login_url="/sign-in")
def coordinator_profile(request):
    return render(request, 'coordinator/coordinator-profile.html')


@login_required(login_url="/sign-in")
def coordinator_password(request):
    return render(request, 'coordinator/coordinator-password.html')

# =================================================================== #
@login_required(login_url="/sign-in")
def employee(request):
    if request.user.is_authenticated:
        print("User",request.user.username)
    return render(request, 'employee/dashboard-employee.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8002/sign-in')
