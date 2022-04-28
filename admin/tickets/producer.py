import json
import pika

params = pika.URLParameters('amqps://jlhbcjsi:AXEem1APWOncJtrSTqopVQ3ierxtQ8BS@sparrow.rmq.cloudamqp.com/jlhbcjsi')
connection = pika.BlockingConnection(params)
channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='user', body=json.dumps(body), properties=properties)
