class Addr:
    def __init__(self, name, phone, addr):
        self.name = name     # 테이블의 컬럼명과 같다.
        self.phone = phone   # 테이블의 컬럼명과 같다.
        self.addr = addr     # 테이블의 컬럼명과 같다.

    def __str__(self):
        return f"<Addr {self.name}/{self.phone}/{self.addr}>"

    def __repr__(self):
        return f"<Addr {self.name}>"


