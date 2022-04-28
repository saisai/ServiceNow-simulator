from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import TicketSerializer
from .models import Ticket
from rest_framework.response import Response


class TicketViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/tickets
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None): #/api/tickets/<str:id>
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(ticket)
        return Response(serializer.data)

    def update(self, request, pk=None): #/api/tickets/<str:id>
        ticket = Ticket.objects.get(id=pk)
        serializer = TicketSerializer(instance=ticket, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
