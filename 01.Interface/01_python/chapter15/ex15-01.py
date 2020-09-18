# 1
# 클래스 (가장 중요한 파트, 객체 지향 프로그래밍)

# ■ 클래스
#   ○ 관련 정보와 정보의 조작 함수(메서드)를 묶어서 관리

# 예제 - 기존 (두 함수가 독립적)

balance = 8000
def deposit(money):
    global balance
    balance += money

def inquire():
    print("잔액은 %d원 입니다."%balance)

deposit(1000)
inquire()

"""
잔액은 9000원 입니다.
"""

# 정보가 많아지면 불편하다. (누구, 언제, 이자율, ...)

#########################################################
# ■ 클래스 정의
#   ○ class 키워드로 정의 (관례 파스칼)
#       ● 사용하기 위해서는 인스턴스를 생성한 후 사용

class Account:
    def __init__(self, balance):  # 생성자 함수 (초기화한다.)
        self.balance = balance  # 인스턴스 변수

    def deposit(self, money):  # 클래스의 종속된 함수 : 메서드
        self.balance += money

    def inquire(self):  # slef -> 관례
        print("잔액은 %d원 입니다."%self.balance)

account = Account(8000)  # Account의 인스턴스 생성 (참조 메커니즘)
account.deposit(1000)
account.inquire()

sinhan = Account(8000)
sinhan.deposit(1000)
sinhan.inquire()

nonghyup = Account(1200000)
nonghyup.inquire()

"""
잔액은 9000원 입니다.
잔액은 9000원 입니다.
잔액은 1200000원 입니다.
"""

# 정보를 인스턴스마다 초기화 해야한다.
# 고유하게 가지는 값을 설정해야한다.


#########################################################
# 비교!

l_data = [1, 2, 3]  # list의 인스턴스 생성
t_data = (1, 2, 3)  # tuple의 인스턴스 생성
d_data = { 'a':1, 'b':2 }  # dictionary의 인스턴스 생성
a = Account(100)  # Account의 인스턴스 생성


#########################################################
# ■ 생성자
#   ○ __init__(self)
#       ● 클래스의 인스턴스를 생성할 때 자동으로 호출 (클래스명을 함수처럼 호출했을 때)
#       ● 멤버 변수 정의 및 초기화 역할
#
# class 이름:
#   def __init__(self, 초기값):
#       멤버 초기화
#
#   메서드 정의
#
# 객체 = 객체명(인수)  # 인스턴스 생성

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")


kim = Human("김상형", 29)
kim.intro()

lee = Human("이승우", 45)
lee.intro()

kim2 = kim  # 참조값을 대입 ∴ 같은 인스턴스를 가르킴

"""
29살 김상형입니다.
45살 이승우입니다.
"""

#########################################################
# 연습 (이름과 나이를 사용자로 부터 입력 받아 인스턴스 생성)

name = input("이름 : ")
age = int(input("나이 : "))
h1 = Human(name, age)
h1.intro()


# 언제 인스턴스 데이터가 사라지나
# 참조 변수가 사라져 참조하지 않으면 gabege collector가 제거

#########################################################
#########################################################
# 연습 Stack class 만들기!!!


class Stack:
    def __init__(self, size=5):  # 디폴드 5로 설정해보자. s2=Stack() 이런것도 가능하게
        self.data = []
        self.size = size

    def push(self, data):
        if len(self.data) == self.size:   # FULL
            return  # return!!!!!☆☆☆
        self.data.append(data)

    def pop(self):
        if len(self.data) == 0:  # EMPTY
            return   # return!!!!!☆☆☆
        return self.data.pop()  # return!!!!!☆☆☆

    def clear(self):
        self.data = []

    def __str__(self):  # 출력 메서드 (15장 21p)
        return f"<Stack size: {self.size}, data: {self.data} >"  # 관례

def main():
    s1 = Stack(10)
    s1.push(10)
    s1.push(20)
    s1.push(30)
    print(s1)

    print(s1.pop())
    print(s1.pop())
    print(s1.pop())
    print(s1.pop())

main()

"""
<Stack size: 10, data: [10, 20, 30] >
30
20
10
None
"""

#########################################################
# 전 예제 출력 메서드 사용

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")

    def __str__(self):
        return f"<{self.age}살 {self.name}>"


kim = Human("김상형", 29)
kim.intro()
print(kim)  # __str__ 메서드 이용
lee = Human("이승우", 45)
lee.intro()

info = lee.__str__()  # 메서드 접근
print(info)

print(kim.name)  # 메서드 접근 가능
kim.age = 20  # 변경 가능
kim.intro()

"""
29살 김상형입니다.
<29살 김상형>
45살 이승우입니다.
<45살 이승우>
김상형
20살 김상형입니다.
"""

#########################################################
# 예제 - 주소록 클라스 정의

class UserInfo:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"<UserInfo {self.name}>"


#########################################################
# def __str__(self): 이용

class UserInfo:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"<UserInfo {self.name}>"


l = [
    UserInfo("홍길동", "hong@naver.com", "010-1111-2222"),
    UserInfo("고길동", "go@naver.com", "010-1111-1111"),
]

print(l)

u1 = UserInfo("홍길동", "hong@naver.com", "010-1111-2222")
u2 = UserInfo("고길동", "go@naver.com", "010-1111-1111")

l = [u1, u2]  # 위와 같다.

print(l)
print(l[0])
print(u1)

"""
[<__main__.UserInfo object at 0x000001504BE99788>, <__main__.UserInfo object at 0x000001504BE997C8>]
[<__main__.UserInfo object at 0x000001504BE99888>, <__main__.UserInfo object at 0x000001504BE99848>]
<UserInfo 홍길동>
<UserInfo 홍길동>
"""

#########################################################
# def __repr__(self): 이용


class UserInfo:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"<UserInfo {self.name} {self.phone}>"

    def __repr__(self):  # 컬렉션에 담긴 출력 (축약된 정보)  # 추가
        return f"<UserInfo {self.name}>"                 # 추가


l = [
    UserInfo("홍길동", "hong@naver.com", "010-1111-2222"),
    UserInfo("고길동", "go@naver.com", "010-1111-1111"),
]

print(l)

u1 = UserInfo("홍길동", "hong@naver.com", "010-1111-2222")
u2 = UserInfo("고길동", "go@naver.com", "010-1111-1111")

l = [u1, u2]  # 위와 같다.

print(l)
print(l[0])
print(u1)

"""
[<UserInfo 홍길동>, <UserInfo 고길동>]
[<UserInfo 홍길동>, <UserInfo 고길동>]
<UserInfo 홍길동 010-1111-2222>
<UserInfo 홍길동 010-1111-2222>
"""



