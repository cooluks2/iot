from addr_models import Addr  # 임폴트

def print_list(total, rows):
    print("=" * 50)
    header = ("이름", "전화번호", "주소")
    print(f"No   {header[0]:10}{header[1]:10}{header[2]:10} ")
    print("-" * 50)
    for ix, row in enumerate(rows, 1):
        print(f"{ix} : {row.name:10} {row.phone:10} {row.addr:10} ")  # 인덱스 대신 필드 변수
    print("=" * 50)
    print(f"(총 {total} 건)")

def input_addr_info():
    name  = input("이름   : ")
    phone = input("전화번호: ")
    addr  = input("주소   : ")
    return Addr(name, phone, addr)  # 튜플 대신

def input_now_addr(data):
    phone = input(f"전화번호({data.phone}): ")  # 튜플 대신
    if not phone:
        phone = data.phone  # 튜플 대신
    addr = input(f"주소({data.addr}): ")  # 튜플 대신
    if not addr:
        addr = data.addr  # 튜플 대신

    return Addr(data.name, phone, addr)  # 튜플 대신