from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

query = {"topic": "iot/home1/device1/humi"}
list = sensors_col.find(query).sort("value")  # .sort("value", -1)

for x in list:
    print(x)

print(type(list))
