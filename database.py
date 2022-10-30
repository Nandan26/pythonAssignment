from pymongo import MongoClient
import settings

client = MongoClient(settings.mongodb_uri, settings.port)

#database with name data will be created
db = client["data"]

#collection with name user_data will be created
user_info = db["client_data"]