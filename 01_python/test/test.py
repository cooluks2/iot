# DB+App.py

import sys
from myapp import Application, MenuItem
import MySQLdb


class DBApp(Application):
    def __init__(self):
        super().__init__()
        self.db = MySQLdb.connect(db="sqldb", host="localhost",
                                  user="root", passwd="1234", charset='utf8')
        self.cursor = self.db.cursor()

    def create_menu(self, menu):
        menu.add(MenuItem("목록", self.print_list))
        menu.add(MenuItem("검색", self.search))  # 검색 메뉴 추가
        menu.add(MenuItem("추가", self.add))
        menu.add(MenuItem("수정", self.update))
        menu.add(MenuItem("삭제", self.remove))
        menu.add(MenuItem("종료", self.exit))

    def exit(self):
        answer = input("종료하시겠습니까?([y]/n) ")
        if answer in ["y", "Y", ""]:
            self.cursor.close()
            self.db.close()
            sys.exit(0)

    def print_list(self):
        try:
            sql = "SELECT count(*) from tblAddr"
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            total = row[0]

            sql = "SELECT * FROM tblAddr"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()

            print("=" * 50)
            print("No  이름          전화번호    주소")
            print("-" * 50)
            for ix, row in enumerate(rows, 1):
                print(f"{ix} : {row[0]:10} {row[1]:10} {row[2]} ")
            print("=" * 50)
            print(f"(총 {total} 건)")
        except Exception as e:
            print(e)

    def add(self):
        try:
            name = input("이름   : ")
            phone = input("전화번호: ")
            addr = input("주소   : ")
            sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
            self.cursor.execute(sql, (name, phone, addr))
            self.db.commit()
            print("추가 완료")
        except Exception as e:
            print(e)

    def remove(self):
        try:
            name = input("이름: ")
            sql = "DELETE FROM tblAddr WHERE name = %s"
            self.cursor.execute(sql, (name,))
            self.db.commit()
            print("삭제 완료")
        except Exception as e:
            print(e)

    def update(self):
        try:
            name = input("이름: ")
            sql = "SELECT * FROM tblAddr WHERE name = %s"
            self.cursor.execute(sql, (name,))
            data = self.cursor.fetchone()
            if not data:
                print(f"{name} 데이터가 없습니다.")
                return

            phone = input(f"전화번호({data[1]}): ")
            if not phone:
                phone = data[1]
            addr = input(f"주소({data[2]}): ")
            if not addr:
                addr = data[2]

            sql = """
            UPDATE tblAddr SET
                phone = %s,
                addr = %s
            WHERE name = %s
            """

            self.cursor.execute(sql, (phone, addr, name))
            self.db.commit()
            print("수정 완료")

        except Exception as e:
            print(e)

    def search(self):
        try:
            name = input("이름   : ")
            sql = f"SELECT count(*) from tblAddr WHERE name LIKE '%{name}%'"
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            total = row[0]

            sql = f"SELECT * from tblAddr WHERE name LIKE '%{name}%'"
            self.cursor.execute(sql)
            rows = self.cursor.fetchall()

            print("=" * 50)
            header = ("이름", "전화번호", "주소")
            print(f"No   {header[0]:10}{header[1]:10}{header[2]:10} ")
            print("-" * 50)

            for ix, row in enumerate(rows, 1):  # No을 위해 enumerate 이용
                print(f"{ix} : {row[0]:10} {row[1]:10} {row[2]} ")  # ★★★ : 뒤는 폭을 의미
            print("=" * 50)
            print(f"(총 {total} 건)")

        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = DBApp()
    app.run()
