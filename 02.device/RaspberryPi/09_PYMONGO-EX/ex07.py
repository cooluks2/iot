from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

query = {"value": {"$gt": 55.1}}
projection = { "_id" : 0, "topic":1, "value":1}
# topic과 vale만 출력 "reg_date":0 으로도 가능
list = sensors_col.find(query, projection).sort("value")  # .sort("value", -1)

for x in list:
    print(x)
