import Pyro4
from app1Phase2 import workflowLog

import pika

uri = input("What is the Pyro uri of the greeting object?").strip()
name = input("What is your name?").strip()

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune(name))
workflowLog('Pass')

try:
	payload = open('jsonPayload5.json', 'rb')
	data = payload.read()
	print("Connecting to Localhost Queue")
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	print("Channel Connected")
	channel.queue_declare(queue = 'ist411')
	channel.basic_publish(exchange = '', routing_key = 'ist411', body = data)
	print("[x] Send Payload")
	connection.close()
except Exception as e:
	print(e)
