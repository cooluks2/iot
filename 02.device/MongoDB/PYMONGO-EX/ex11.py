from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

query = {"value": {"$lt": 55.1}}
sensors_col.delete_many(query)

sensor_values = sensors_col.find(query)
for x in sensor_values:
    print(x)
