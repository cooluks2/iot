from pymongo import MongoClient
from datetime import datetime
import random

mongodb = MongoClient("mongodb://localhost:27017/")
db = mongodb.iot_service

slist = db.sensors.find()

for x in slist:
    print(x)
