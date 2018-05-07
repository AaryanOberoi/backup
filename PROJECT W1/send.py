import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='Device1')
channel.queue_declare(queue='Device2')
channel.queue_declare(queue='Device3')
channel.queue_declare(queue='Device4')
channel.queue_declare(queue='Device5')
channel.exchange_declare(exchange='User1',exchange_type='fanout')
channel.exchange_declare(exchange='User2',exchange_type='fanout')
channel.exchange_declare(exchange='User3',exchange_type='fanout')
channel.basic_publish(exchange='User1',routing_key='Device2',body='Message on Device2 of User1')
channel.basic_publish(exchange='User2',routing_key='Device3',body='Message on Device3 of User2')

print(" [x] Sent Message")
connection.close()

