import random
from rest_framework import viewsets, status
from .models import Ticket, User
from .serializers import TicketSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .producer import publish


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


class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
