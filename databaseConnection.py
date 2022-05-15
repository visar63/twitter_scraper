from pymongo.mongo_client import MongoClient

#Establishing a Connection
MONGODB_CONNECTION_STRING = "mongodb://localhost:27017/"
client = MongoClient(MONGODB_CONNECTION_STRING)
