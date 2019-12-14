import Pyro4
from app5 import workflowLog
from Crypto.Cipher import AES

import pika

uri = input("What is the Pyro uri of the greeting object?").strip()
name = input("What is your name?").strip()

greeting_maker = Pyro4.Proxy(uri)
print(greeting_maker.get_fortune(name))
workflowLog('Pass')


""" Encrypt a json payload using a 32-byte key """
def encryptPayload(data, cipher):
	plaintext = data
	print(plaintext)
	length = 16 - (len(plaintext)%16)
	print(length)
	plaintext += length*pad
	print("Plain text: ", plaintext)
	ciphertext = cipher.encrypt(plaintext)
	print(type(ciphertext))
	print("Ciphertext: ", ciphertext)
	return ciphertext

try:
	print("Reading the file Payload to encrypt")
	pad = b' '
	payload = open('jsonPayload5.json', 'rb')
	data = payload.read()
	""" AES cipher using a 32-byte key """
	cipher = AES.new('keykeykeykeykeykeykeykeykeykeyyy'.encode('utf-8'), AES.MODE_CBC, 'This is an IV456'.encode('utf-8'))
	ciphertext = encryptPayload(data, cipher)
	""" Saving  encypted payload to an aes file """
	with open('encryptedPayload5.aes', 'wb') as outFile: outFile.write(ciphertext)
	print("Connecting to Localhost Queue")
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()
	print("Channel Connected")
	channel.queue_declare(queue = 'ist411')
	channel.basic_publish(exchange = '', routing_key = 'ist411', body = ciphertext)
	print("[x] Send Payload")
	connection.close()
except Exception as e:
	print(e)



"""  Benchmarking test to assure type of encypted payload is in bytes """
def testEncrypt(benchmark):
	result = benchmark(encryptPayload, data, cipher)
	assert type(result) is bytes

