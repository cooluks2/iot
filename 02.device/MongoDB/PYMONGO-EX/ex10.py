from pymongo import MongoClient
from datetime import datetime
from bson.objectid import ObjectId
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

query = {"value":{"$gt":24.1}}

# query = {"_id" : ObjectId("5f83e7547d80e57f631da801")}
# 일반적으로 데이터를 삭제할 땐 id를 받아 삭제를 진행

sensors_col.delete_one(query) # 한개삭제

sensor_values = sensors_col.find()
for x in sensor_values:
    print(x)