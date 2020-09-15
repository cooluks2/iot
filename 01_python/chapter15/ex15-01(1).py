# 4

# ■ 상속
#   ○ 기존 클래스 정의를 그대로 자신의 것으로 취하는 방법
#
#     class 자식클래스명(부모클래스명):
#            ... # 자식 클래스 정의

# 기능의 확장

# UML : 코드를 그림으로 표현


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살 " + self.name + "입니다.")


class Student(Human):
    def __init__(self, name, age, stunum):  # 자신한테 필요한 요소 다 받는다
        super().__init__(name, age)  # super() 부모class의 참조값이 리턴된다.
        self.stunum = stunum

    def intro(self):  # 1. 없으면 부모것 그대로 사용
        super().intro()  # 2. 이줄이 없으면 자기것만 사용 # 3. 이건 method override
        print("학번: " + str(self.stunum))

    def study(self):
        print("하늘천 따지 검을 현 누를 황")


kim = Human("김상형", 29)
kim.intro()
lee = Student("이승우", 45, 930011)
lee.intro()
lee.study()

"""
29살 김상형입니다.
45살 이승우입니다.
학번: 930011
하늘천 따지 검을 현 누를 황
"""

