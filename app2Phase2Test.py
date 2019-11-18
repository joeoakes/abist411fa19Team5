import socket, ssl, pysftp, sys, hashlib, hmac, base64, json
from datetime import datetime
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-oakes', 'username':'ftpuser', 'password':'test1234', 'port':100}
class TestApp2Phase2(unittest.TestCase):
    def test_sample(self):
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
            signature1 = hmac.new(key, jsonPayload, hashlib.sha256).hexdigest()
            print("Signature1 (sha256): ", signature1)
            sig1 = signature1.encode('utf8')
            signature2 = base64.encodestring(sig1)
            print(type(signature2))
            print("Signature2 (sha256): ", signature2)
            print()
            with open('jsonPayload5.json', 'w') as outFile:
                jsonObj = outFile.write(json.dumps(jsonPayload.decode('utf8')))
                with open('jsonPayload5.json', 'r') as json_data:
                    pyObj = json.load(json_data)
                    print(repr(pyObj))
                    with pysftp.Connection(**cinfo) as sftp:
                        print("putting jsonPayload5.json file")
                        sftp.put('/home/NaharaMelodonascimentodemou/abist411fa19Team5/jsonPayload5.json')
                        print("Signature2 (sha256): ", signature2)
                        print("Signature1 (sha256): ", signature1)
if __name__ == '__main__':
    unittest.main()