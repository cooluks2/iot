# 데이터베이스

#  MySQL/MariaDB
# ○ pip install mysqlclient

# import MySQLdb
#
# db = MySQLdb.connect(db="sqldb", host="localhost", user="root", passwd="1234", charset='utf8')
#
# cursor = db.cursor()
#
# # cursor를 통해 SQL 문장 실행
#
# # 자원 해제 및 접속 해제
# cursor.close()
# db.close()

##############################################################
#  테이블 생성 / 데이터 삽입

# import MySQLdb
#
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
#
# cursor = db.cursor()
#
# cursor.execute('DROP TABLE IF EXISTS tblAddr')
#
# cursor.execute("""
# CREATE TABLE tblAddr(
#     name CHAR(16) PRIMARY KEY,
#     phone CHAR(16),
#     addr TEXT
# )
# """)
#
# cursor.execute("INSERT INTO tblAddr VALUES('김상형', '123-4567', '오산')")
# cursor.execute("INSERT INTO tblAddr VALUES('한경은', '555-1004', '수원')")
# cursor.execute("INSERT INTO tblAddr VALUES('한주완', '444-1092', '대전')")
#
# db.commit()
# cursor.close()
# db.close()


##############################################################
#  테이블 조회 .fetchall()

# import MySQLdb
#
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
#
# cursor = db.cursor()
#
# cursor.execute("SELECT * FROM tblAddr")
#
# table = cursor.fetchall()
# for record in table:
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")
#
# cursor.close()
# db.close()

#################################
#  테이블 조회 .fetchone()

# import MySQLdb
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
# cursor = db.cursor()
#
# cursor.execute("SELECT * FROM tblAddr")
# while True:
#     record = cursor.fetchone()
#     if record == None: break
#
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")
#
# cursor.close()
# db.close()

#################################
#  테이블 조회 .fetchall() 자료형

# import MySQLdb
#
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
# cursor = db.cursor()
#
# cursor.execute("SELECT * FROM tblAddr ORDER BY addr")
#
# table = cursor.fetchall()
# print(type(table), table)
# for record in table:
#     print(record)
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")
#
# cursor.close()
# db.close()

#################################
#  테이블 조회 WHERE 절 이용

# import MySQLdb
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
# cursor = db.cursor()
#
# cursor.execute("SELECT addr FROM tblAddr WHERE name = '김상형'")
#
# record = cursor.fetchone()
#
# if record : print(f"김상형은 {record[0]}에 살고 있습니다.")
# else : print("김상형은 없는 이름입니다.")
#
# cursor.close()
# db.close()


#################################
# 검색하는 사람을 사용자로부터 입력 받아서 출력
# import MySQLdb
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
# cursor = db.cursor()
#
# name = input("검색어(이름): ")
#
# # cursor.execute(f"SELECT addr FROM tblAddr WHERE name = '{name}'")
# sql = "SELECT addr FROM tblAddr WHERE name = %s"
# cursor.execute(sql, (name,))  # 요소가 하나일 때 튜플임을 알려줘야한다.
#
# record = cursor.fetchone()
#
# if record : print(f"{name}은 {record[0]}에 살고 있습니다.")
# else : print(f"{name}은 없는 이름입니다.")
#
# cursor.close()
# db.close()

#################################
# 검색하는 사람을 사용자로부터 3가지 정보를 입력 받아서 INSERT

# import MySQLdb
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
# cursor = db.cursor()
#
# try:
#     print("데이터 추가================")
#     name = input("이름: ")
#     phone = input("전화: ")
#     addr = input("주소: ")
#     print("==========================")
#     sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
#     cursor.execute(sql, (name, phone, addr))  # 요소가 하나일 때 튜플임을 알려줘야한다.
#     db.commit()
#
#     print("추가 완료")
# except Exception as e:
#     print(e)
#
# cursor.close()
# db.close()



##############################################################
# ■ 수정 및 삭제

# 수정

# import MySQLdb
#
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
# cursor = db.cursor()
#
# cursor.execute("UPDATE tblAddr SET addr = '제주도' WHERE name = '김상형'")
# db.commit()
#
# cursor.close()
# db.close()

# 삭제

# import MySQLdb
#
# db = MySQLdb.connect(db="sqldb", host="localhost",
#                      user="root", passwd="1234", charset='utf8')
# cursor = db.cursor()
#
# cursor.execute("DELETE FROM tblAddr WHERE name = '김태림'")
# db.commit()
#
# cursor.close()
# db.close()




# C:\PYTHON_LIB 에 myapp.py, util.py 이 있다.
# 전에 PYTHONPATH 환경변수로 C:\PYTHON_LIB Directory를 설정해두었다.