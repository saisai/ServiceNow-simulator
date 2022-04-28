
import json
from os import environ
from sys import path
import pika
import django


path.append('/app/user/settings.py') #Your path to settings.py file
environ.setdefault('DJANGO_SETTINGS_MODULE', 'user.settings')
django.setup()
from tickets.models import Ticket

params = pika.URLParameters('amqps://jlhbcjsi:AXEem1APWOncJtrSTqopVQ3ierxtQ8BS@sparrow.rmq.cloudamqp.com/jlhbcjsi')
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='user')


def callback(ch, method, properties, body):
    print('Received in user')
    print('------------')
    data = json.loads(body)
    print(data)
    print("--------------------")
    print(properties.content_type)

    if properties.content_type == 'ticket_created':
        ticket = Ticket.objects.create(id=data['id'], incident_number=data['incident_number'], priority=data['priority'], customer=data['customer'],
                        short_description=data['short_description'], description=data['description'], content=data['content'])
        ticket.save()
        print("Ticket stworzony")

    elif properties.content_type == 'ticket_updated':
        ticket = Ticket.objects.get(id=data['id'])
        ticket.incident_number = data['incident_number']
        ticket.priority = data['priority']
        ticket.customer = data['customer']
        ticket.short_description = data['short_description']
        ticket.description = data['description']
        ticket.content = data['content']
        ticket.save()

    elif properties.content_type == 'ticket_deleted':
        ticket = Ticket.objects.get(id=data)
        ticket.delete()


channel.basic_consume(queue='user', on_message_callback=callback, auto_ack=True)
print('Started consuming')
channel.start_consuming()
channel.close()
