# 복습
###########################

# x와 y의 값을 교환하세요.
# x=10
# y=20
# print("x: ", x)
# print("y: ", y)
#
# a=x
# x=y
# y=a
# print("x: ", x)
# print("y: ", y)

###########################
# 가위1 바위0 보2 게임

# com=0
# me=1
# if com==me:
#     print("비겼습니다.")
# elif com==1:
#     if me==2: print("컴퓨터가 이겼습니다.")
#     else: print("내가 이겼습니다.")
# elif com==2:
#     if me==0: print("컴퓨터가 이겼습니다.")
#     else: print("내가 이겼습니다.")
# else:
#     if me==1: print("컴퓨터가 이겼습니다.")
#     else: print("내가 이겼습니다.")

# 유지보수관리 측면에서 좋지 않다. 뒤를 해석하기 위해 앞을 봐야한다.

import random

ROCK = 0
SCISSORS = 1
PAPER = 2

com = int(random.random()*10)%3
me = int(input('0:주먹, 1:가위, 2:보 \n'))

if com == me: print("비겼습니다.")
elif com == SCISSORS:
    if me == PAPER: print("컴퓨터가 이겼습니다.")
    else: print("내가 이겼습니다.")
elif com == PAPER:
    if me == ROCK: print("컴퓨터가 이겼습니다.")
    else: print("내가 이겼습니다.")
else:
    if me == SCISSORS: print("컴퓨터가 이겼습니다.")
    else: print("내가 이겼습니다.")

# 가독성
# 관례 대문자:상수, 소문자:변수

