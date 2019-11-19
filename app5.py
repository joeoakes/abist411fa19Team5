import sys
from pymongo import MongoClient

try:
	client = MongoClient('localhost', 27017)
	db = client.log
	log_collection = db.log
	collection.insert_many(log_collection)

	for post in db.log.find():
		print(str(post['_id']))
except:
	e = sys.exc_info()[0]
	print("error: %s" % e)




