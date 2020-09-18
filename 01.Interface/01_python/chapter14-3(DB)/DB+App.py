import sys
from myapp import Application, MenuItem
import MySQLdb
from addr_repository import AddressRepositrory
from addr_ui import *

import sqlite3  # sqlite3

class DBApp(Application):
    def __init__(self):
        super().__init__()
        # self.db = MySQLdb.connect(db="sqldb", host="localhost",
        #                           user="root", passwd="1234", charset='utf8')  # sqlite3

        self.db = sqlite3.connect("c:/temp/test.db")  # sqlite3
        self.repo = AddressRepositrory(self.db)

    def create_menu(self, menu):
        menu.add(MenuItem("목록", self.print_list))
        menu.add(MenuItem("검색", self.search))
        menu.add(MenuItem("추가", self.add))
        menu.add(MenuItem("수정", self.update))
        menu.add(MenuItem("삭제", self.remove))
        menu.add(MenuItem("종료", self.exit))

    def exit(self):
        answer = input("종료하시겠습니까?([y]/n) ")
        if answer in ["y", "Y", ""]:
            self.repo.close()
            self.db.close()
            sys.exit(0)

    def print_list(self):
        total = self.repo.get_total()
        rows = self.repo.get_list()
        print_list(total, rows)


    def add(self):
        data = input_addr_info()
        self.repo.insert(data)
        self.db.commit()
        print("추가 완료")

    def remove(self):
        name  = input("이름: ")
        self.repo.remove(name)
        self.db.commit()
        print("삭제 완료")


    def update(self):
        name  = input("이름: ")
        data = self.repo.get_one(name)
        if not data:
            print(f"{name} 데이터가 없습니다.")
            return

        data = input_now_addr(data)
        self.repo.update(data)
        self.db.commit()
        print("수정 완료")



    def search(self):
        name = input("이름   : ")
        where = f"WHERE name LIKE '%{name}%'"
        total = self.repo.get_total(where)
        rows = self.repo.get_list(where)
        print_list(total, rows)


if __name__ == '__main__':
    app = DBApp()
    app.run()
