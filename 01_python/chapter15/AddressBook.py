# 2

# 예제
# 주소록 -> 리스트에 인스턴스를 넣기

# 메서드마다 단위 테스트 하자
# 메서드 배치 순서는 상관없다.

import pickle  # 저장,불러오기 용


class UserInfo:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):  # 해당 인스턴스를 print 할 때 (자세하게 해도 좋음)
        return f"<UserInfo {self.name}/{self.email}/{self.phone}>"

    def __repr__(self):  # 컬렉션에 포함되었을 때 print (축약)
        return f"<UserInfo {self.name}>"


class AddressBook:  # 정보 관리 class는 CRUD를 기억하자.
    def __init__(self):
        self.book = []

    def add(self, name, email, phone):  # 주소록 추가
        ui = UserInfo(name, email, phone)
        self.book.append(ui)

    def find_by_name(self, name):  # 이름으로 찾기
        for ui in self.book:
            if ui.name == name:  # 동명이인은 없다는 가정
                return ui        # 이름이 없으면 루프 다 돌고 None을 return

    def update(self, name, email, phone):  # 주소록 업데이트
        ui = self.find_by_name(name)  # self를 꼭 붙여줘야한다!
        if not ui:
            print(f"{name}(은/는) 목록에 없습니다")
            return

        ui.email = email
        ui.phone = phone

    def remove(self, name):  # 이름으로 제거
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name}(은/는) 목록에 없습니다")
            return

        self.book.remove(ui)  # 값으로 삭제

    # def search_by_name(self, name):  # 이름 일부분 포함된 유저 찾기
    #     new_book = []
    #     for ui in self.book:
    #         if ui.name.find(name) > -1:
    #             new_book.append(ui)
    #     return new_book

    # 컴프리헨션으로 변경 가능 ☆☆☆☆☆☆
    def search_by_name(self, name):
        return [ui for ui in self.book if ui.name.find(name) > -1]

    def save(self, fpath):  # 파일 저장
        try:
            with open(fpath,'bw') as file:
                pickle.dump(self.book, file)
        except Exception as e:
            print(f"{fpath} 파일 쓰기에 실패했습니다.")
            print(e)

    def load(self, fpath):  # 파일 불러오기
        try:
            with open(fpath, 'br') as file:
                self.book = pickle.load(file)
        except:
            print(f"{fpath} 파일 읽기에 실패했습니다.")

    def sort(self, reverse=False): # 이름순으로 정렬(reverse 매개변수 디폴트로 준다.)
        self.book.sort(key=lambda u: u.name, reverse=reverse)  # ☆☆☆

    def __str__(self):
        pass

#
# addr_book = AddressBook()
# addr_book.add("홍길동", "hong@naver.com", "010-1111-1111")
# addr_book.add("고길동", "go@naver.com", "010-1111-2222")
#
# print(addr_book.book)
#
#
#
# u1 = addr_book.find_by_name('고길동')
# print(u1)
#
# u2 = addr_book.find_by_name('희동이')
# print(u2)
#
# addr_book.update("고길동", "go@gmail.com", "010-2222-2222")
# u1 = addr_book.find_by_name('고길동')
# print(u1)
# addr_book.update("희동이", "go@gmail.com", "010-2222-2222")
#
# users = addr_book.search_by_name('길동')
# print(users)
# users = addr_book.search_by_name('홍길')
# print(users)
# users = addr_book.search_by_name('희동')
# print(users)
#
# addr_book.remove('고길동')
# u1 = addr_book.find_by_name('고길동')
# print(u1)


# save, load 테스트 위에꺼 주석처리

file_name = 'book1.dat'
addr_book = AddressBook()
#
# addr_book.add('홍길동', 'hong@naver.com', '010-1111-1111')
# addr_book.add('고길동', 'go@naver.com', '010-1111-2222')
# addr_book.save(file_name)
#
# addr_book2 = AddressBook()
# addr_book2.load(file_name)
# print(addr_book2.book)

# Test용 Data 위 주석

for ix in range(1, 100):
    if ix%2 == 0:
        addr_book.add(f"홍길동{ix}", "hong{ix}@naver", "010-1111-1111")
    else:
        addr_book.add(f"고길동{ix}", "go{ix}@naver", "010-2222-2222")
addr_book.save(file_name)

# load용 (위에 주석처리)

addr_book.load(file_name)
print(len(addr_book.book))

addr_book.sort()
print(addr_book.book)