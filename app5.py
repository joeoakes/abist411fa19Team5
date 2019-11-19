import sys, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo import ASCENDING

try:
	client = MongoClient('localhost', 27017)
	db = client.logTeam5
	collection = db.logs
#	collection.insert(collection)

	for post in db.logs.find():
		print(str(post['_id']))
except:
	e = sys.exc_info()[0]
	print("error: %s" % e)




