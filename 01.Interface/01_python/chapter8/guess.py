# 2
# 함수 만들기 연습

import random

start = 1
rng = 6

number = int(random.random()*(rng)) + start

##########################################################
# 위에 것을 함수로

import random

start = 1
rng = 6

def rand(start, rng):
    number = int(random.random()*(rng)) + start
    return number

number = rand(start,rng)
print(number)

# Python에서는 이미 만들어진 함수를 변수로 쓸 수 있다.
# 다만 다시 함수를 이용할 수 없다.
# ex) range=10 이후 range(10) X

##########################################################
# rand(start, end) 로 해보자

def rand(start, end):
    return int(random.random()*(end-start)) + start  # 위에서 number는 필요없는 변수

##########################################################
# 앞으로 시작 함수를 만들자.

def main():
    start = 1
    end =6
    number = rand(start, end)
    print(number)

main()

# 전역변수를 다 지역변수로 옮긴 것 (전역변수의 사용을 최대한 자제하자.)


##########################################################
# 랜덤한 숫자 5개 뽑아보기(main함수 내에서)

def main():
    start = 1
    end =6
    for i in range(5):
        number = rand(start, end)
        print(number)

main()

# entry point (다른 언어의 main 함수와 같음)

##########################################################

import random

def main():
    com=rand(1, 100)
    print(com)

    for i in range(5):

        print(i+1,'번째 추측값: ', end='')
        me = int(input())
        if i == 4:
            print("실패했습니다.\n정답은",com)
        else:
            if com == me:
                print("정답입니다.")
                break
            elif com < me:
                print(me, "보다는 작습니다.")
            else:
                print(me, "보다는 큽니다.")

main()

############################################################
# 강사님 풀이

import random

def rand(start, end):
    return int(random.random()*(end-start)) + start

def main():
    number = rand(1, 100)
    print(number)
    for i in range(1, 6):
        num = int(input(str(i)+ "번째 추측값: "))
        result = number - num
        if result == 0: # 정답
            print("정답입니다.")
            break
        elif result > 0:
            print(num, "보다는 큽니다.")
        else:
            print(num, "보다는 작습니다.")

    if result != 0:
        print('실패했습니다.\n정답은 ', number)

main()

# 정렬이 되어있다면 위 경우는 7번 (∵log_2 100 = 6.xxx)
# 40억개 데이터면 32번
############################################################
