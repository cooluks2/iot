from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://localhost:27017/")

iot_db = db_client['iot_service']
sensors_col = iot_db['sensors']

sensor_values = [
    {
        "topic": "iot/home1/device1/temp",
        "value": 24 + random.random(),
        "reg_date": datetime.utcnow()  # 현재 시간
    },
    {
        "topic": "iot/home1/device1/humi",
        "value": 55 + random.random(),
        "reg_date": datetime.utcnow()  # 현재 시간
    },
    {
        "topic": "iot/home2/device1/temp",
        "value": 24 + random.random(),
        "reg_date": datetime.utcnow()  # 현재 시간
    },
    {
        "topic": "iot/home2/device1/humi",
        "value": 55 + random.random(),
        "reg_date": datetime.utcnow()  # 현재 시간
    }
]
x = sensors_col.insert_many(sensor_values)  # 여러 문서 삽입
print(x.inserted_ids)
