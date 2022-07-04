from .producer import publish
from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import TicketSerializer
from .models import Ticket
from rest_framework.response import Response
from django.contrib.auth.models import auth
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.exceptions import AuthenticationFailed
import jwt


class TicketViewSet(viewsets.ViewSet):
    def list(self, request): #/api/tickets
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def create(self, request): #/api/tickets
        serializer = TicketSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('ticket_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #/api/tickets/<str:id>
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, pk=None): #/api/tickets/<str:id>
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('ticket_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #/api/tickets/<str:id>
        ticket = Ticket.objects.get(id=pk)
        ticket.delete()
        publish('ticket_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


class HomeView(viewsets.ViewSet):
    def get(self, request):
        token = request.GET.get('token')
        payload = jwt.decode(jwt=token, key='secret', algorithms=['HS256'])
        print("Name", payload['name'])
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        else:
            return render(request, 'home.html', {'name': payload['name'], 'surname': payload['surname'], 'email': payload['mail']})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('http://127.0.0.1:8002/sign-in')


def account(request):
    context = {}
    return render(request, 'home.html')
