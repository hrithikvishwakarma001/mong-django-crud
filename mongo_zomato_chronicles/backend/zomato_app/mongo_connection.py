from pymongo import MongoClient
from django.conf import settings

client = MongoClient(settings.DATABASES["default"]["CLIENT"]["host"])
db = client.get_database("django")



