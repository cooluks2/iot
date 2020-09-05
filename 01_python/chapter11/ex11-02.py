# 람다 함수

# ■ filter
#   ○ filter(판정함수, 시퀀스) -> 시퀀스 (<class 'filter'>)
#       ● 시퀀스의 각 요소를 판정함수에 전달하여
#          True를 리턴하는 요소로만 구성된 새로운 시퀀스 리턴

# 판정함수 : True, False를 판정할 수 있는 함수

def flunk(s):
    return s < 60

score = [ 45, 89, 72, 53, 94 ]
for s in filter(flunk, score):  # 함수의 이름만 전달한다.
    print(s)

"""
45
53
"""

# filter 함수의 메거니즘
def filter( fn, lst ):
    new_list=[]
    for a in lst:
        if fn(a):  # 함수 fn의 return 값이 True인 요소만 리스트에 추가
            new_list.append(a)
    return new_list

prn = print  # 됨. print 함수 대신 prn를 쓸 수 있다는 뜻
print = 10  # 됨. 하지만 print 함수 이용 못함
list = [1, 2] # 됨. 하지만 list 함수 이용 못함

########################################################
# 리스트 중 짝수만 프린트 하기
# 내 풀이
def odd_print(s):
    return s % 2 == 0

score = [ 45, 89, 72, 53, 94 ]
for s in filter(odd_print, score):  # 함수의 이름만 전달한다.
    print(s)
"""
72
94
"""

# 강사님
def is_even(s):
    return  s % 2 == 0

score = [ 45, 89, 72, 53, 94 ]
even_list = list(filter(is_even, score))
print(even_list)
"""
[72, 94]
"""

########################################################
# ■ map(1)
#   ○ map(변환함수, 시퀀스 [,...] ) -> 시퀀스
#       ● 시퀀스의 각 요소를 변환함수에 전달하고,
#          그 함수의 리턴값으로 구성된 새로운 시퀀스 리턴

def half(s):
    return s/2

score = [ 45, 89, 72, 53, 94 ]
for s in map(half, score):
    print(s, end=", ")

"""
22.5, 44.5, 36.0, 26.5, 47.0, 
"""

########################################################
# ■ map(2) : 두 시퀀스의 각 요소를 이용

def total(s, b):
    return s + b

score = [ 45, 89, 72, 53, 94 ]
bonus = [ 2, 3, 0, 0, 5 ]
for s in map(total, score, bonus):
    print(s, end = ", ")

"""
47, 92, 72, 53, 99, 
"""


########################################################
# ■ 람다 함수(1)
#   ○ 한 줄로 정의되는 함수의 축약 표현
#   ○ 함수의 이름이 없음
#       ● 변수에 대입해서 사용
#   ○ lambda 인수 : 식(코드 블럭)

# sort, map, filter 에서 이용하는 함수

# 전에 list에서 sort할 때 key=str.lower 함수를 인수로 사용한 적이 있었다.

lambda x: x + 1  # 인수가 2개면 lambda x, y :
# 위 아래 같다.
def increase(x):
    return x + 1


# 위에서 한 flunk 함수와 같다.
score = [ 45, 89, 72, 53, 94 ]
for s in filter(lambda x: x < 60, score): # filter 함수 이용
    print(s)

"""
45
53
"""

########################################################
# ■ 람다 함수(2)

score = [ 45, 89, 72, 53, 94 ]
for s in map(lambda x: x / 2, score): # map 함수 이용
    print(s, end = ", ")

"""
22.5, 44.5, 36.0, 26.5, 47.0, 
"""

########################################################
# ■ 람다 함수(3) 예제
