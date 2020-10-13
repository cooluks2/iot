from pymongo import MongoClient

# db 서버 접속
db_client = MongoClient("mongodb://localhost:27017/")

# 기존 데이터베이스이름 목록 출력
print(db_client.list_database_names())
