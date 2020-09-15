# Chater 07-02 이후

def int_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    return total


def main():
    print(int_sum(1, 2, 3, 4, 5))
    print(int_sum())  # 인수 없이 호출이 된다. 루프를 돌지 않는다.

main()

"""
15
0
"""
#########################################################
# 함수

# 인수의 형식
# ■ 키워드 인수(1)
#   ○ 일반적으로 함수 호출시 인수의 배치 순서대로 매칭
#   ○ 인수 순서가 아닌 인수의 명칭으로 매칭하는 방법

def calcstep(begin, end, step):
    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total

print("3 ~ 5 =", calcstep(3, 5, 1))
print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
print("3 ~ 5 =", calcstep(3, 5, step=1))
print("3 ~ 5 =", calcstep(3, step=1, end=5))

# 왼쪽부터 채워나가야함( 앞 = 위치기반, 뒤 = 키워드기반 )

"""
3 ~ 5 = 12
3 ~ 5 = 12
3 ~ 5 = 12
3 ~ 5 = 12
3 ~ 5 = 12
"""

#########################################################
# ■ 키워드 인수(2)

a = 10
b = 20
print(a, b)
print(a, b, sep=',')
print(a, b, sep=',', end='$')
print(a, b, end='$', sep=',')

"""
10 20
10,20
10,20$10,20$
"""

#########################################################
# ■ 키워드 가변 인수(1)
#   ○ 키워드 인수를 가변 개수로 전달할 때 사용하는 방법
#   ○ **기호로 지정하여 타입은 사전 (dictionary)이 됨
#       def 함수명(**인수명):
#           명령 블럭

# * : 위치기반의 가변인수(튜플), ** : 키워드 가변인수(사전)

def calcstep(**args):  # <class 'dict'>
    begin = args['begin']
    end = args['end']
    step = args['step']

    total = 0
    for num in range(begin, end+1, step):
        total += num

    return total


print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
print("3 ~ 5 =", calcstep(begin=1, end=5))  # args['step']에서 예외 발생
print("3 ~ 5 =", calcstep(end=10, step=2))  # args['begin']에서 예외 발생

"""
3 ~ 5 = 12
3 ~ 5 = 12
"""


#########################################################
# ■ 키워드 가변 인수(1)

# default 값을 주고 싶을 때!!! -> get 함수 이용

def calcstep(**args):  # <class 'dict'>
    begin = args.get('begin', 1)  # default 값으로 1
    end = args['end']  # 필수 요소
    step = args.get('step', 1)  # default 값으로 1

    total = 0
    for num in range(begin, end+1, step):
        total += num

    return total


print("3 ~ 5 =", calcstep(begin=3, end=5, step=1))
print("3 ~ 5 =", calcstep(step=1, end=5, begin=3))
print("3 ~ 5 =", calcstep(begin=1, end=5))
print("3 ~ 5 =", calcstep(end=10, step=2))

"""
3 ~ 5 = 12
3 ~ 5 = 12
3 ~ 5 = 15
3 ~ 5 = 25
"""

#########################################################
# 정리 예제

# ■ 가변인수 정의할 때는 보통 *args로
def fun(*args):
    lst=[2, 5, 7]
    fun(lst)
# 이 경우는 매개변수 1개 준 것 *args에 [2, 5, 7]

def fun(*args):
    lst=[2, 5, 7]
    fun(1, lst)
# 이 경우는 매개변수 2개 준 것 *args에 [1, [2, 5, 7]]

def fun(*args):
    lst=[2, 5, 7]
    fun(1, *lst, 2)
# 이 경우는 매개변수 5개 준것 *args에 [1, 2, 5, 7, 2] -> 펼치기



# ■ 키워드 가변인수 정의할 때는 보통 **kwargs로
def fun(**kwargs):
    dic = {'a':1, 'b':2}
    fun(dic)
# 이것은 위치기반의 매개변수이다.

def fun(**kwargs):
    dic = {'a':1, 'b':2}
    fun(**dic) # ( = fun(a=dic['a'], b=dic['b'])  )
# ** 사전을 펼치는 것 ☆☆☆


#########################################################
# ■ 일반 변수, 가변 변수, 키워드 가변 변수 모두 사용
#   ○ 일반 변수, 가변 변수, 키워드 가변 변수 순서로 배치

# calcstep("김한슬", 99, 98, 95, 89, avg = False):
# calcstep(name, *score, **option):

