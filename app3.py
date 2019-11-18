import sys, pysftp, paramiko, app2Phase2, hashlib, hmac, base64, app1Phase2, zlib, gzip
from email.mime.text import MIMEText
import smtplib
import Pyro4

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-oakes', 'username':'ftpuser', 'password':'test1234', 'port':100}

fromAddress = 'nkm5334@psu.edu'
subject = 'JSON Payload'
toAddress =['nkm5334@psu.edu', 'asw5310@psu.edu', 'tpl5148@psu.edu', 'cvp5380@psu.edu', 'bmy5076@psu.edu']

@Pyro4.expose
class GreetingMaker(object):
	def get_fortune(self, name):
		payload = open("jsonPayload5.json", 'rb')
		data = payload.read()
		return data

try:
	with pysftp.Connection(**cinfo) as sftp:
		print("Connection made")
		print("getting jsonPayload5.json file")
		sftp.get('/home/ftpuser/jsonPayload5.json')
		sftp.remove('/home/ftpuser/jsonPayload5.json')
		print("Reading the file Payload")
		payload = open('jsonPayload5.json', 'rb')
		data = payload.read()
		payload.close()
		key = "5411"
		key = bytes(key, 'UTF-8')
		signature  = hmac.new(key, data, hashlib.sha256).hexdigest()
		print("Signature1 (sha256): ", signature)
		sig1 = signature.encode('utf8')
		signature_ = base64.encodestring(sig1)
		print("Signature2 (sha256): ", signature)
		print()
		sig3 = input("Enter app2 sha256 signature: ")
		signature4 = sig3.encode('utf-8')
		signature5 = base64.encodestring(signature4)
		print(signature5)
		compare = hmac.compare_digest(signature_, signature5)
		print(compare)
		payloadN = data.decode('utf-8')
		app1Phase2.log("Pass")
		def compressPayload(data):
			payloadComp = gzip.compress(data)
			return payloadComp
		compressPayload(data)
		print("JSON Payload Compressed")
		def sendEmail(payload,subject, fromAddress, toAddress):
			email_msg=payload
			msg = MIMEText(email_msg)
			msg['Subject'] = subject
			msg['From'] = fromAddress
			msg['To'] = ", ".join(toAddress)
			print("Sending a message")
			s = smtplib.SMTP_SSL('authsmtp.psu.edu', 465)
			s.sendmail(fromAddress, toAddress, msg.as_string())
		sendEmail(payloadN, subject, fromAddress, toAddress)
		daemon = Pyro4.Daemon()
		uri = daemon.register(GreetingMaker)
		print("Ready. Object uri = ", uri)
		daemon.requestLoop()
except:
	print("Log exception 2:", sys.exc_info()[0])
	app1Phase2.log("Fail")
