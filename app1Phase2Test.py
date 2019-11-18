import socket, ssl, urllib.request, json
from pymongo import ASCENDING
import sys, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint


url='https://jsonplaceholder.typicode.com'
param='/posts/1/comments'

class TestApp1Phase2(unittest.TestCase):
    def test_sample(self):
        print('Url:', url+param)
        response=urllib.request.urlopen(url+param)
        client = MongoClient()
        db = client.logs
        log_collection = db.log
        log_collection.ensure_index([("timestamp", ASCENDING)])
        payload=response.read()
        def log(msg):
            """Workflow Action Status"""
            entry = {}
            entry['timestamp'] = datetime.datetime.utcnow()
            entry['status'] = msg
            log_collection.insert(entry)
            log('Pass')
            print("Client connecting on port 8080 using SSL")
            clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c_ssl = ssl.wrap_socket(clientsocket,
                                    ca_certs="server.crt",
                                    cert_reqs=ssl.CERT_REQUIRED)
            c_ssl.connect(('localhost', 8080))
            c_ssl.send(payload)
with open('curlApp3.json', 'w') as outFile:
	jsonObj = outFile.write(json.dumps(payload.decode('utf8')))
with open('curlApp3.json', 'r') as json_data:
	pyObj = json.load(json_data)
	print(repr(pyObj))
if __name__ == '__main__':
    unittest.main()

