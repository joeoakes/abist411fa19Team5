import socket, ssl, urllib.request, json
from pymongo import ASCENDING
import sys, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint


url='https://jsonplaceholder.typicode.com'
param='/posts/1/comments'

try:
	print('Url:', url+param)
	response=urllib.request.urlopen(url+param)
	client = MongoClient()
	db = client.log
	log_collection = db.log
	log_collection.ensure_index([("timestamp", ASCENDING)])
	payload=response.read()
	def workflowLog(msg):
		"""Pass/Fail Log"""
		entry = {}
		entry['timestamp'] = datetime.datetime.utcnow()
		entry['status'] = msg
		log_collection.insert(entry)
	workflowLog('Pass')

	print("Client connecting on port 8080 using SSL")
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c_ssl = ssl.wrap_socket(clientsocket,
		ca_certs="server.crt",
		cert_reqs=ssl.CERT_REQUIRED)
	c_ssl.connect(('localhost', 8080))
	c_ssl.send(payload)
except Exception as e:
	print(e)
	print(c_ssl.cipher())
	c_ssl.close()
	workflowLog('Fail')

with open('curlApp1.json', 'w') as outFile:
	jsonObj = outFile.write(json.dumps(url))

with open('curlApp1.json', 'r') as json_data:
	pyObj = json.load(json_data)
	print(repr(pyObj))

