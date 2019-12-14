
import socket, ssl, urllib.request, json
from app5 import workflowLog
from pymongo import ASCENDING
import sys, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import pika
from Crypto.Cipher import AES


url='https://jsonplaceholder.typicode.com'
param='/posts/1/comments'

try:
	print('Url:', url+param)
	response=urllib.request.urlopen(url+param)
	client = MongoClient('localhost', 27017)
	db = client.logTeam5
	collection = db.logs
	collection.ensure_index([("timestamp", ASCENDING)])
	payload=response.read()

	print("Client connecting on port 8080 using SSL")
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c_ssl = ssl.wrap_socket(clientsocket,
		ca_certs="server.crt",
		cert_reqs=ssl.CERT_REQUIRED)
	c_ssl.connect(('localhost', 8080))
	c_ssl.send(payload)
	workflowLog("Connection to app1 established")
	def decryptPayload(data, cipher):
		decrypted = cipher.decrypt(data)
		return decrypted
	print("Connection to localhost")
	connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
	channel = connection.channel()
	print("Queue ist411 created")
	channel.queue_declare(queue = 'ist411')
#	aesFile = open('encryptedPayloadMelo.aes', 'rb')
	cipher = AES.new('keykeykeykeykeykeykeykeykeykeyyy'.encode('utf-8'), AES.MODE_CBC, 'This is an IV456'.encode('utf-8'))
	def callback(ch, method, properties, body):
		print("[x] Received %r" % body)
#		decryptPayload(data, cipher)
		print("Decrypted Payload: ", decryptPayload(body, cipher))
		workflowLog("Pass Decryption")
	channel.basic_consume(queue = 'ist411', on_message_callback = callback, auto_ack = True)
	print(' [*] Waiting for messages. To exit press CTRL + C')
	channel.start_consuming()

except Exception as e:
	print(e)
	print(c_ssl.cipher())
	c_ssl.close()
	workflowLog('Fail')


with open('curlApp3.json', 'w') as outFile:
	jsonObj = outFile.write(json.dumps(payload.decode('utf8')))
with open('curlApp3.json', 'r') as json_data:
	pyObj = json.load(json_data)
	print(repr(pyObj))
