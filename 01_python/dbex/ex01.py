# 맛보기 Python + MariaDB 연동
# >> pip install mysqlclient

import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees',
                     user='root', passwd='1234')

# MySQLdb : 서버, host : 자신, port : (생략, 디폴트), db : 어떤거

cursor = db.cursor()  # SQL 실행을 위한 cursor 객체 실행

print("접속에 성공했습니다.")

# 가장 최근 입사한 순으로 10명 출력해보기

sql = """SELECT * FROM EMPLOYEES
ORDER BY hire_date desc
LIMIT 10
"""

cursor.execute(sql)

rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
db.close()
