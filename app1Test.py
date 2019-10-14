# Project: App1Test - Project Diamond

# Purpose Details: To retrieve and send a JSON payload

# Course: IST 411

# Author: Team 5

# Date Developed: 10/12/2019

# Last Date Changed:10/12/2019

import app1, app1Client

import unittest

def test_if_payload_is_recieved(self):
	a1 = app1()
	a1client = app1Client()
	payload = {"message": "This is a test"}
	a1client.c_ssl.send(payload)
	result = a1.c_ssl.recv(157778)
	assertTrue(result)
