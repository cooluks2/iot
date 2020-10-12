from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

query = {"value":{"$gt":55.1}}
newvalues = {"$set": { "reg_date": datetime.now() }}
sensors_col.update_one(query, newvalues)

sensor_values = sensors_col.find()
for x in sensor_values:
    print(x)