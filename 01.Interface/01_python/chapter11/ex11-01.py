# 컬렉션 관리

# 컬렉션 관리 함수
# ■ enumerate
#   ○ enumerate(시퀀스 [, start])
#       ● 시퀀스의 인덱스와 요소를 튜플 묶어서 순회

# 기존 코드(1)
score = [88, 95, 70, 100, 99]
for s in score:
    print("성적 : ", s)
# index에 대한 정보가 없다.

"""
성적 :  88
성적 :  95
성적 :  70
성적 :  100
성적 :  99
"""

# 기존 코드(2)
score = [88, 95, 70, 100, 99]
for no in range(len(score)):
    print(str(no+1) + "번 학생의 성적 : ", score[no])
"""
1번 학생의 성적 :  88
2번 학생의 성적 :  95
3번 학생의 성적 :  70
4번 학생의 성적 :  100
5번 학생의 성적 :  99
"""

# enumerate
race = ['저그', '테란', '프로토스']
print(list(enumerate(race)))
"""
[(0, '저그'), (1, '테란'), (2, '프로토스')]
"""

# enumerate, tuple unpack 이용
score = [88, 95, 70, 100, 99]
for no, s in enumerate(score, 1):
    print(str(no) + "번 학생의 성적 : ", s)

"""
1번 학생의 성적 :  88
2번 학생의 성적 :  95
3번 학생의 성적 :  70
4번 학생의 성적 :  100
5번 학생의 성적 :  99
"""

########################################################
# ■ zip (1)
#   ○ zip(시퀀스1, 시퀀스2) -> [(값1, 값2), ... ]
#   ○ 시퀀스의 길이가 다른 경우 가장 짧은 시퀀스의 길이에 맞춤

# 동일 index 끼리 묶는다.

dates = ["월", "화", "수", "목", "금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]

menu = zip(dates, food)  # <class 'zip'>
for d, f in menu:
    print("%s요일 메뉴: %s" % (d, f))

"""
월요일 메뉴: 갈비탕
화요일 메뉴: 순대국
수요일 메뉴: 칼국수
목요일 메뉴: 삼겹살
"""

########################################################
# ■ zip (2) 시퀀스 3개 (가변인수 처리가 되어있다. 매개변수 제한이 없다.)

dates = ["월", "화", "수", "목", "금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
price = [9000, 8000, 7000, 7500]

menu = zip(dates, food, price)
for d, f, p in menu:
    print(f"{d}요일 메뉴: {f}, {p}원")

"""
월요일 메뉴: 갈비탕, 9000원
화요일 메뉴: 순대국, 8000원
수요일 메뉴: 칼국수, 7000원
목요일 메뉴: 삼겹살, 7500원
"""


# 두 시퀀스에서 하나는 key, 하나는 value로
# 많이 사용 ☆☆☆
menu_dic = dict(zip(dates, food))
print(menu_dic)

"""
{'월': '갈비탕', '화': '순대국', '수': '칼국수', '목': '삼겹살'}
"""

#######################################################
# 가독성, 관례 -> 일관성
# Pascal Case (Python(☆class 이름 정할때))
#   salesrate -> SalesRate
#   menudic -> MenuDic
#   printaverage -> PrintAverage
#
# Snake Case (C/C++, Python(☆☆))
#   salesrate -> sales_rate
#   menudic -> menu_dic
#   printaverage -> print_average
#
# Camel Case (Java, Python)
#   salesrate -> salesRate
#   menudic -> menuDic
#   printaverage -> printAverage
#
# Kebab Case (- 이 문자인지 연산자인지 몰라서 프로그래밍 언어에서는 안씀)
#   salesrate -> sales-rate
#   menudic -> menu-dic
#   printaverage -> print-average
#
# 상수
# SALES_RATE
#
# 변수 -> 명사로 시작, 함수 -> 동사로 시작
#######################################################

########################################################
# ■ any(), all() (중요도x)
# ○ any(시퀀스)
#   ● 시퀀스에 하나라도 True가 있으면 True 리턴
# ○ all(시퀀스)
#   ● 시퀀스의 모든 요소가 True이면 True 리턴
