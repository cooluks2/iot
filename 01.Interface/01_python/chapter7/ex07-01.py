# 함수

# ■ 반복되는 코드
#   ○ 함수로 정의하여 반복을 없앰


# def 함수명(인수 목록):   # 정의
#   본체
#
#   함수(인수 목록)   # 호출

# 1~n 합 함수
def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num
    return total  # 나를 부른 곳으로 다시 돌아간다. 명시적 return
                  # 없으면 None

print("~4 =", calcsum(4))
print("~10 =", calcsum(10))

# 변수와 함수는 이름을 지어준다. 식별자(identifier)

#######################################################
# ■ 인수
#   ○ 함수로 값을 전달했을 때 이를 저장하는 변수

# begin ~ end 합 함수(인수 2개, 위치기반)
def calcrange(begin, end):
    total = 0
    for num in range(begin, end+1):
        total += num
    return total

print("3 ~ 7 =", calcrange(3, 7))

#######################################################
# ■ 리턴값
#   ○ 함수의 실행결과를 호출한 곳으로 넘기는 값

# 리턴 없어서 None 리턴한 상황 (출력만)
def printsum(n):
    total = 0
    for num in range(n+1):
        total += num
    print("~", n, "=", total)

printsum(4)
printsum(10)
a=printsum(4)
print(a)

# 함수 하나는 한가지 일만 해야한다. 위는 2가지 일(계산, 출력)





#######################################################
# ■ pass
#   ○ 아무것도 안하고 넘어감
#   ○ 함수는 반드시 코드 블럭이 있어야 함
#       ● 실제 구현을 나중으로 미루고자 할 때 pass 지정


def calctotal():
    # 나중에 완성할 것
    pass

# 무조건 함수 만드는 습관을 갖자.
