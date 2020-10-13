from pymongo import MongoClient
from datetime import datetime
import random

db_client = MongoClient("mongodb://192.168.0.11:27017/")

iot_db = db_client['iot_service']  # 데이터베이스 선택, 없으면 자동 생성
sensors_col = iot_db['sensors']  # 컬렉션 선택, 없으면 자동 생성

sensor_value = {
    "topic": "iot/home1/device1/temp",
    "value": 24 + random.random(),
    "reg_date": datetime.utcnow()  # 현재 시간
}

x = sensors_col.insert_one(sensor_value)
print(x.inserted_id)
