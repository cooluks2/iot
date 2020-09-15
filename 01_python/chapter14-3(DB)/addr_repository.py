from addr_models import Addr

class AddressRepositrory:

    def __init__(self, db):        # App은 db객체만 다루게 하기 위해
        self.cursor = db.cursor()  # SQL 실행을 위함

    def close(self):
        self.cursor.close()

    def get_total(self, where=''):  # 디폴드는 where절 없는거
        sql = "SELECT count(*) FROM tblAddr " + where  # 주의! 스페이스
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row[0]

    def get_list(self, where=''):
        sql = "SELECT * FROM tblAddr " + where
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return (Addr(*row) for row in rows)  # 변경


    def get_one(self, name):
        sql = "SELECT * FROM tblAddr WHERE name = %s"
        self.cursor.execute(sql, (name,))
        # return self.cursor.fetchone()
        row = self.cursor.fetchone()
        # addr = Addr(*row)  # 펼쳐준다.
        # return addr
        if row:  # 변경
            return Addr(*row)

    def insert(self, data):
        sql = "INSERT INTO tblAddr VALUES(%s, %s, %s)"
        self.cursor.execute(sql, (data.name, data.phone, data.addr))  # 변경

    def remove(self, name):
        sql = "DELETE FROM tblAddr WHERE name = %s"
        self.cursor.execute(sql, (name,))


    def update(self, data):
        sql = """
            UPDATE tblAddr
            SET
                phone = %s,
                addr = %s
            WHERE name = %s
        """
        self.cursor.execute(sql, (data.phone, data.addr, data.name))