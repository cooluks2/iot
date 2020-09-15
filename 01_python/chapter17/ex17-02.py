# 2

# 데코레이터

# ■ 일급 시민 (First Class Citizen)
#   ○ 함수도 일반 변수와 동일한 특성을 가짐
#       ① 이름을 가진다.
#       ② 다른 변수에 대입할 수 있다 .
#       ③ 인수로 전달할 수 있다 .
#       ④ 리턴값이 될 수 있다 .
#       ⑤ 컬렉션에 저장할 수 있다 .
#       --> 위와 같은 특성을 가지는 것을 일급시민이라고 함

# Python은 지원한다. (Java는 함수가 없어서 지원X)

# funcvalue
def add(a, b):
    print(a + b)

plus = add  # 변수에 저장할 수 있다.
plus(1, 2)

"""
3
"""

# 예제
# funcpara
def calc(op, a, b):  # 함수의 인자로 전달할 수 있다.
    op(a, b)

def add(a, b):
    print(a+b)

def multi(a, b):
    print(a*b)

calc(add, 1, 2)
calc(multi,3,4)

"""
3
12
"""

############################################################
# ■ 지역 함수
#   ○ 함수 안에 함수를 정의해서 사용
#       ● 함수가 정의된 함수 내에서만 사용 가능
#       --> 함수의 이름 충돌 방지
#       ● 함수를 리턴한 경우 함수 밖에서도 사용 가능

# localfunc
def calcsum(n):
    def add(a, b):  # 지역함수  (이름 충돌을 방지하기 위해)
        return a + b

    total = 0
    for i in range(n+1):
        total = add(total, i)

    return total

print("~10 = ", calcsum(10))

"""
~10 =  55
"""

###
# 이렇게하면 같은 결과지만 이름 충돌이 발생할 수 있다.

def add(a, b):
    return a + b

def calcsum(n):

    total = 0
    for i in range(n+1):
        total = add(total, i)

    return total

print("~10 = ", calcsum(10))

############################################################
# 예제 (난이도 上)
# factoryfunc  (closure 변수)
def makeHello(message):  # 이 경우는 message가 Heap에 저장(유지)된다.
    def hello(name):
        print(message + ", " + name)  # 바깥 함수의 매개변수를 쓰고 있다.
    return hello

enghello = makeHello("Good Morning")  # message가 저장된다.
kohello = makeHello("안녕하세요")

enghello("Mr kim")  # name으로 들어간다.
kohello("홍길동")

"""
Good Morning, Mr kim
안녕하세요, 홍길동
"""

# p385 그림 참고
# Python, Jave는 지역변수가 Heap에 생긴다.(사실 Stack 아니였음, 지역변수가 있는 곳을 참조하고 있음)
# enghello,kohello가 message변수와 hello함수가 있는 쪽을 참조하고 있기 때문에 Heap에서 사라지지 않는다.


############################################################
# ■ 함수 데코레이터
#   ○ 이미 만들어진 함수에 동작을 추가하는 파이썬의 고급 기법
#   ○ 함수를 래핑(Wrapping)하여 함수의 앞 또는 뒤에 코드를 자동으로 추가
#   ○ 함수를 호출하면 추가된 앞 ,뒤의 코드도 같이 실행됨

# wrapper (데코레이터를 사용하지 않을 때)
def inner():
    print("결과를 출력합니다.")

def outer(fuc):
    print("-"*20)
    fuc()
    print("-"*20)

outer(inner)

def hello():
    print("안녕하세요")

outer(hello)

"""
--------------------
결과를 출력합니다.
--------------------
--------------------
안녕하세요
--------------------
"""

############################################################
# wrapper2 (조금 더 체계화)
def inner():
    print("결과를 출력합니다.")

def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-" * 20)
    return wrapper

# 아래 한줄이 데코레이터로 간다.
inner = outer(inner)  # 좌변: 원래의 함수 앞뒤에 박스를 그리는 wrapper 함수
inner()               # 우변: 결과를 출력하는 원래의 inner 함수

"""
--------------------
결과를 출력합니다.
--------------------
"""

############################################################
# ■ 함수 데코레이터 @함수명
# 예제1

# decorator
def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-" * 20)
    return wrapper

@outer
def inner():
    print("결과를 출력합니다.")

inner()

"""
--------------------
결과를 출력합니다.
--------------------
"""

############################################################
# 예제2

# tagdeco
def para(func):
    def wrapper():
        return "<p>" + str(func()) + "</p>"
    return wrapper

@para  # decorator 명
def outname():
    return "김상형"

@para  # 리턴하는 값에 대해서 넘겨줌
def outage():
    return "29"

print(outname())
print(outage())

"""
<p>김상형</p>
<p>29</p>
"""


############################################################
# ■ 클래스 데코레이터
#   ○ __callable__ 메서드
#       ● 클래스를 함수 호출하듯이 사용했을 때 호출되는 메서드

# __가 앞뒤로 붙은 함수들의 특징은 직접 메서드를 호출하지 않는다. (호출되는 시점이 정해져있다.)

# classwrapper (deco X)
class Outer:
    def __init__(self, func):
        self.func = func

    def __call__(self):
        print("-"*20)
        self.func()
        print("-"*20)

def inner():
    print("결과를 출력합니다.")

inner = Outer(inner)  # inner가 Outer의 객체가 되었다.
inner()  # 함수호출처럼 보이지만 실제 변수는 객체이다.

"""
--------------------
결과를 출력합니다.
--------------------
"""

############################################################
# classdeco

class Outer:
    def __init__(self, func):  # class decorator가 되려면 생성자의 매개변수로 함수가 있어야한다.
        self.func = func

    def __call__(self):
        print("-"*20)
        self.func()
        print("-"*20)

@Outer      # inner = Outer(inner)
def inner():
    print("결과를 출력합니다.")

inner()

"""
--------------------
결과를 출력합니다.
--------------------
"""

# Class decorator는 callable 객체이기도 하다.
# 역은 성립하지 않는다.

