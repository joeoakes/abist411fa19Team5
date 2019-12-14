# Project: App2 - Phase2  Project Diamond
# Course: IST 411
# Author: Team 5
# Date Developed: 11/16/2019
# Last Date Changed:11/17/2019

import socket, ssl, pysftp, sys, hashlib, hmac, base64, json
from datetime import datetime
from app1Phase2 import workflowLog

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-oakes', 'username':'ftpuser', 'password':'test1234', 'port':100}
try:
	print("create an INET, STREAMing socket using SSL")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	ssl_sock = ssl.wrap_socket(s,
                server_side=True,
		ssl_version=ssl.PROTOCOL_TLSv1,
                certfile="server.crt",
                keyfile="server.key")
	print("bind the socket to a public host, and a well-known port 8080")
	ssl_sock.bind(("localhost", 8080))
	ssl_sock.listen(5)
	print("ciphers: " + str(ssl_sock.cipher()))
	while True:
		print("accept connections from outside")
		(c_ssl, address) = ssl_sock.accept()
		jsonPayload = c_ssl.recv(157778)
		print("json payload received: ", jsonPayload)
		key = "5411"
		key=bytes(key, 'UTF-8')
		print()
		workflowLog("Pass Connection")
		with open('jsonPayload5.json', 'w') as outFile:
			jsonObj = outFile.write(json.dumps(jsonPayload.decode('utf8')))
		with open('jsonPayload5.json', 'r') as json_data:
			pyObj = json.load(json_data)
#			print(repr(pyObj))
		payload = open('jsonPayload5.json', 'rb')
		data = payload.read()
		payload.close()
		signature1 = hmac.new(key, data, hashlib.sha256).hexdigest()
		sig1 = signature1.encode('utf8')
		signature2 = base64.encodestring(sig1)
		with pysftp.Connection(**cinfo) as sftp:
			try:
				print("putting jsonPayload5.json file")
				sftp.put('/home/NaharaMelodonascimentodemou/abist411fa19Team5/jsonPayload5.json')
				print("Signature1 (sha256): ", signature1)
				print("Signature2 (sha256): ", signature2)
				workflowLog("Pass")
			except:
				print("Log exception 2:", sys.exc_info()[0])
#				app1Phase2.workflowLog("Fail")
except Exception as e:
		print(e)
#		ssl_sock.close()
#	app1Phase2.workflowLog('Fail')
