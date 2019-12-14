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


try:
	print("Reading the file Payload to encrypt")
	pad = b' '
	payload = open('jsonPayload5.json', 'rb')
	data = payload.read()
	jsonPayload = data.decode('utf-8')

	payload.close()
	cipher = AES.new('keykeykeykeykeykeykeykeykeykeyyy'.encode('utf-8'), AES.MODE_CBC, 'This is an IV456'.encode('utf-8'))
	print("Cipher: ", cipher)
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
	def testEncrypt(benchmark):
		result = benchmark(encryptPayload, data, cipher)
		assert type(result) is bytes
	ciphertext = encryptPayload(data, cipher)
	with open('encryptedPayloadMelo.aes', 'wb') as outFile: outFile.write(ciphertext)

except:
	e = sys.exc_info()[0]
	print("error: %s" % e)
