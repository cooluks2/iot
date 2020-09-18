# 지역 변수
#   ○ 함수 내에서 사용된 변수
#   ○ 함수 내에서 만 사용 가능
#      ● 함수 밖에서 사용 불가

###########################################################
# 예제1

def calsum(n): # 변수 n은 호출에서 초기화
    total = 0  # 변수 total은 함수 내에서 초기화
    for num in range(n+1):  # 변수 num 또한 함수 내에서 초기화
        total += num

    return total

# 세 변수 n, total, num 은 모두 지역변수


###########################################################
# 예제2(오류)

# def kim():
#     temp = '김과장의 함수'
#     print(temp)
#
# kim()
# print(temp)  # name 'temp' is not defined


###########################################################
# 예제3

def kim():
    temp = '김과장의 함수'
    print(temp)

def lee():
    temp = 2**10
    return temp

def park(a):
    temp = a*2
    print(temp)

kim()
print(lee())
park(6)

# 김과장의 함수
# 1024
# 12

###########################################################
# 전역 변수
#   ○ 어디서든 접근 가능한 변수
#   ○ 탑 레벨에서 사용된 변수

###########################################################
# 예제1

salerate = 0.9

def kim():
    print("오늘의 할인율:", salerate)

def lee():
    price = 1000
    print("가격 :", price * salerate)

kim()
salerate = 1.1
lee()

# 오늘의 할인율: 0.9
# 가격 : 1100.0

###########################################################
# 예제2

price = 1000
def sale():
    price = 500

sale()
print(price)

# price 두 변수는 다르다.

# 1000


###########################################################
# 예제3

price= 1000
def sale():
    price = 500
    print("sale", id(price))

sale()
print("global", id(price))

# sale 2097613157520
# global 2097613157264

대입연산의 우선 순위 -> 지역변수가 높다. 함수 안에서 읽을 때 쓸 때 다르다.
id() : 동일한 객체 여부를 판별하는 연산자
test -> 전역변수에서 두 값이 같으면 id가 같다.


###########################################################
# 예제4 (전역변수에 대하여 쓰기 연산을 하고 싶을 때)

price = 1000

def sale():
    global price
    price = 500

sale()
print(price)

# 500

# 추천사항 : 전역변수는 가급적 사용하지마라 -> 지역변수 지향
# 전역변수는 오작동의 근원이다. 상수처럼 읽기용으로는 써라.


###########################################################
# docstring
#   ○ 함수의 도움말
#   ○ 함수의 코드 블록 앞에 문자열로 지정 (위치가 고정되어 있다.)
#   ○ help(함수명) 호출 시 출력될 문자열

def calcsum(n):
    """1 ~ n까지의 합계를 구해 리턴한다."""
    total = 0
    for i in range(n+1):
        total += i

    return total

help(calcsum)

# Help on function calcsum in module __main__:
#
# calcsum(n)
#     1 ~ n까지의 합계를 구해 리턴한다.


###########################################################
# min = FindMin(2, 7, 5, -1, 20) 해보기 (내 풀이)

def FindMin(int1, *ints):
    temp = int1
    for num in ints:
        if temp >= num : temp = num
    return temp

min = FindMin(2, 7, 5, -1, 20)
print('최소값:', min)

###########################################################
# 강사님 : 수가 10000 이하라 가정

def FindMin(*numbers):
    min = 999999
    for num in numbers:
        if num < min:
            min = num
    return min

min = FindMin(2, 7, 5, -1, 20)
print('최소값:', min)


###########################################################
# max = FindMax(2, 7, 5, -1, 20) 해보기

def FindMax(int1, *ints):
    temp = int1
    for num in ints:
        if temp < num : temp = num
    return temp

max = FindMax(2, 7, 5, -1, 20)
print('최대값:', max)
