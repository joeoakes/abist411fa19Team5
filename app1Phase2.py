
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
	client = MongoClient('localhost', 27017)
	db = client.logTeam5
	collection = db.logs
	collection.ensure_index([("timestamp", ASCENDING)])
	payload=response.read()
	def workflowLog(msg):
		"""Workflow Action Status"""
		entry = {}
		entry['timestamp'] = datetime.datetime.utcnow()
		entry['status'] = msg
		collection.insert(entry)

	print("Client connecting on port 8080 using SSL")
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c_ssl = ssl.wrap_socket(clientsocket,
		ca_certs="server.crt",
		cert_reqs=ssl.CERT_REQUIRED)
	c_ssl.connect(('localhost', 8080))
	c_ssl.send(payload)
	workflowLog("Connection to app1 established")
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
