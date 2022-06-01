from django.shortcuts import render
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponseRedirect
from .serializers import UserSerializer
from .models import User
from rest_framework import viewsets
import jwt, datetime


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def support(request):
    return render(request, 'contact.html')


def demo_dashboard(request):
    return render(request, 'demo.html')


def sign_in(request):
    return render(request, 'auth-login.html')


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
            return render(request, 'auth-register.html')

    def get(self, request):
        return render(request, 'auth-register.html')


class SignInView(viewsets.ViewSet):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        print(bool(user.is_coordinator))
        if user is None:
            messages.error(request, 'User not found. Please try again')
            return HttpResponseRedirect('/sign-in')

        if not user.check_password(password):
            messages.error(request, 'Invalid password. Please try again')
            return HttpResponseRedirect('/sign-in')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = ({
            'jwt': token
        })
        #tutaj dodać if'a, że jeśli is_coordinator == True to dashboard-coordinator, jeśli nie to do dashboard'u usera
        return render(request, 'dashboard-coordinator.html', {'name': user.name, 'surname': user.surname, 'email': user.email})

    def get(self, request):
        return render(request, 'auth-login.html')


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
        return response
