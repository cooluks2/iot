# 8

# 여러가지 매서드

# ■ 클래스 메서드
#   ○ 일반적인 메서드는 인스턴스 메서드
#       ● 반드시 인스턴스를 만든 후 사용 가능
#       ● 첫 번째 인자는 항상 인스턴스에 대한 참조 (self)
#   ○ 클래스 메서드는 인스턴스와 무관하게 존재
#       ● 인스턴스 없이도 클래스명을 통해 접근 가능
#       ● 첫 번째 인자는 클래스에 대한 참조 (cls)
# ○ @classmethod로 정의
#
# ■ 클래스 멤버 변수
#   ○ class 안에서 self와 무관하게 정의되는 멤버 변수
#   ○ 인스턴스와 무관하게 존재하며 모든 인스턴스가 공유하는 정보

# 코드를 보는게 낫다.

class Car:
    count = 0  # 클래스 멤버 변수 (클래스 멤버 라인에 있다.)

    def __init__(self, name):
        self.name = name
        Car.count += 1  # 인스턴스와 무관

    @classmethod  # 데코레이터
    def outcount(cls):  # 아래 호출에서 cls에 Car가 넘어간다.
        print(cls.count)

pride = Car("프라이드")
korando = Car("코란도")
Car.outcount()  # 클래스명으로 호출해야한다.

"""
2
"""

# 클래스 변수를 쓸 때 이용한다.

#############################################
# ■ 정적 메서드
#   ○ 단순히 클래스 내에 정의되는 일반함수
#       ● 클래스에 대한 어떠한 정보도 제공하지 않음
#       ● 첫 번째 인자가 정해져 있지 않음
#   ○ 비슷한 성격의 함수를 묶어서 관리하는 역할

class Car:
    @staticmethod
    def hello():
        print("오늘도 안전 운행 합시다.")

    count = 0
    def __init__(self, name):
        self.name = name
        Car.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)

Car.hello()

"""
오늘도 안전 운행 합시다.
"""

# 인스턴스가 없어도 되는 것 : @classmethod, @staticmethod

#############################################
# ■ 연산자 메서드
#     ○ 연산자를 재정의할 수 있는 함수
#     ○ 연산자 별로 함수명이 정해져 있음

# ○ == : __eq__  # object
# ○ != : __ne__  # object
# ○ < : __lt__
# ○ > : __gt__
# ○ <= : __le__
# ○ >= : __ge__
# ○ + : __add__, __radd__
# ○ - : __sub__, __rsub__
# ○ * : __mul__, __rmul__
# ○ / : __div__, __rdiv__
# ○ // : __floordiv__, __rfloordiv__
# ○ % : __mod__, __rmod__
# ○ ** : __pow__, __rpow__
# ○ << : __lshift__ ○ >> : __rshift__



l1 = [1, 2, 3]
l2 = [1, 2, 3]

l1 == l2  # 안에서 루프가 돌아야한다. 즉, == 가 함수의 역할을 해야한다.

h1=Human("kim",29)
h2=Human("kim",29)

h1 == h2  # 이건 어떤걸 비교해야하는지 모른다. (결과는 False)
# 원하는 동작을 만들어 주어야한다.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):  # 왼쪽이 self, 오른쪽이 other
        return self.name == other.name and self.age == other.age

kim = Human("김상형", 29)
sang = Human("김상형", 29)
moon = Human("문종민", 44)

print(kim == sang)  # 왼쪽이 self, 오른쪽이 other로 넘어감
print(kim == moon)

"""
True
False
"""

# 클래스의 상속 중요하다.
