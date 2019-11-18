import sys, pysftp, paramiko, app2Phase2, hashlib, hmac, base64
from email.mime.text import MIMEText
import smtplib

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-oakes', 'username':'ftpuser', 'password':'test1234', 'port':100}

fromAddress = 'nkm5334@psu.edu'
subject = 'JSON Payload'
toAddress =['nkm5334@psu.edu', 'asw5310@psu.edu', 'tpl5148@psu.edu', 'cvp5380@psu.edu', 'bmy5076@psu.edu']

class TestApp3(unittest.TestCase):
    def test_sample(self):
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
            signature1 = hmac.new(key, data, hashlib.sha256).hexdigest()
            print("Signature1 (sha256): ", signature1)
            sig1 = signature1.encode('utf8')
            signature2 = base64.encodestring(sig1)
            print("Signature2 (sha256): ", signature2)
            print()
            sig3 = input("Enter app2 sha256 signature: ")
            signature4 = sig3.encode('utf-8')
            signature5 = base64.encodestring(signature4)
            print(signature5)
            compare = hmac.compare_digest(signature2, signature5)
            print(compare)
            payloadN = data.decode('utf-8')
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
if __name__ == '__main__':
    unittest.main()