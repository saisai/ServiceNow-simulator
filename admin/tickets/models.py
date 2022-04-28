from django.db import models


class Ticket(models.Model):
    incident_number = models.CharField(max_length=20)
    priority = models.CharField(max_length=10, default=None)
    customer = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    content = models.CharField(max_length=200) # do poprawy - tutaj trzeba dać models.ImageField, żeby przechowywać screeny z Treesize'a
    status = models.CharField(max_length=50, default='Pending Assignment')
    assigned_to = models.CharField(max_length=50, default='')
    current_queue = models.CharField(max_length=50, default='PL.Bridge.BE.Events')


class User(models.Model):
    pass
