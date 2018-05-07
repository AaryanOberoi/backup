#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='Device1')
channel.queue_declare(queue='Device2')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(callback,queue='Device2',no_ack=True)
channel.basic_consume(callback, queue='Device3',no_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
