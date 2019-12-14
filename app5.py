import sys, datetime
from pymongo import MongoClient
from bson.objectid import ObjectId
from pymongo import ASCENDING



def workflowLog(msg):
	"""Workflow Action Status"""
	client = MongoClient('localhost', 27017)
	db = client.Team5Logs
	collection = db.logs5
	collection.ensure_index([("timestamp", ASCENDING)])
	entry = {}
	entry['timestamp'] = datetime.datetime.utcnow()
	entry['status'] = msg
	collection.insert(entry)


def main():

	try:
		client = MongoClient('localhost', 27017)
		db = client.logTeam5
		collection = db.logs

		for post in db.logs.find():
			print(str(post['_id']))
	except:
		e = sys.exc_info()[0]
		print("error: %s" % e)

if __name__ == "__main__":
	main()



