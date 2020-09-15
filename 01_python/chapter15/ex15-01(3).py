# 7

# ■ 액세스(1)
#   ○ 파이썬은 기본적으로 정보 은폐 기능 지원하지 않음
#
#   ○ getter/setter로 정보(프로퍼티)를 보호 (데코레이터)
#       ● @property
#           – 함수명이 프로퍼티명이 되며 getter 함수로 동작
#       ● @프로퍼티명.setter
#           – 프로퍼티의 setter() 함수 정의

class Date:
    def __init__(self, month):
        self.inner_month = month  # 외부에서 접근할때 month라는 이름으로 읽거나 쓰겠다.

    @property  # 읽는 용도
    def month(self):
        return self.inner_month

    @month.setter  # 설정 용도
    def month(self, month):  # 잘못된 설정을 방지하는 코드
        if 1 <= month <= 12:
            self.inner_month = month

    # 함수명이 같아도 다르게 식별

today = Date(8)
today.month = 15  # 모양은 field 변수에 write 하는 건데 실제로는 함수가 호출됨

# today.inner_month=15  # 잘못된 행위

print(today.month)

"""
8
"""


# ■ 액세스(2)
#   ○ 프라이빗 멤버 변수
#       ● 멤버 변수 앞에 __을 붙이면 외부에서 바로 접근 불가

class Date:
    def __init__(self, month):
        self.__month = month  # 외부에서 접근할때 month라는 이름으로 읽거나 쓰겠다.

    # @property  # 읽는 용도
    def getmonth(self):
        return self.__month

    # @month.setter  # 설정 용도
    def setmonth(self, month):  # 잘못된 설정을 방지하는 코드
        if 1 <= month <= 12:
            self.__month = month

    month = property(getmonth, setmonth)  # method 위치

today = Date(8)
today.month = 15

print(today.month)
# print(today.__month)  # 예외 발생

"""
8
"""