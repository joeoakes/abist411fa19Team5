# Project: App1Test - Project Diamond

# Purpose Details: To retrieve and send a JSON payload

# Course: IST 411

# Author: Team 5

# Date Developed: 10/12/2019

# Last Date Changed:11/17/2019

import unittest

class TestApp1(unittest.TestCase):
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
if __name__ == '__main__':
    unittest.main()

