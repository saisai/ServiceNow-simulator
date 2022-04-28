from django.db import models
from django.db.models import UniqueConstraint


class Ticket(models.Model):
    id = models.IntegerField(primary_key=True)
    incident_number = models.CharField(max_length=20)
    priority = models.CharField(max_length=10, default=None)
    customer = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    content = models.CharField(max_length=200) # do poprawy - tutaj trzeba dać models.ImageField, żeby przechowywać screeny z Treesize'a
    # status = models.CharField(max_length=50, default='New')
    # assigned_to = models.CharField(max_length=50, default='')
    # current_queue = models.CharField(max_length=50, default='PL.Bridge.BE.Events')
    def __str__(self):
        return self.incident_number

class TicketUser(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    ticket_id = models.IntegerField()

    UniqueConstraint(fields=['user_id', 'ticket_id'], name='user_ticket_unique')
