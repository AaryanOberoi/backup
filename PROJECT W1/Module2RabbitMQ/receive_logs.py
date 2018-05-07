import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='User1',exchange_type='fanout')
#channel.exchange_declare(exchange='User2',exchange_type='fanout')

channel.queue_declare(queue='Device1')
channel.queue_declare(queue='Device2')

channel.queue_bind(exchange='User1',queue='Device1')
channel.queue_bind(exchange='User1',queue='Device2')
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,queue='Device1',no_ack=True)
channel.basic_consume(callback,queue='Device2',no_ack=True)
channel.start_consuming()