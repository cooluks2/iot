import random

ROCK = 0
SCISSORS = 1
PAPER = 2

com_win=0 # 컴퓨터가 이긴 횟수
me_win=0 # 내가 이긴 횟수

for x in range(3):
    com = int(random.random() * 10) % 3
    me = int(input('0:주먹, 1:가위, 2:보 \n'))

    print(x+1, "번째 판은 ", end='')

    if com == me:
        print("비겼습니다.")
    elif com == SCISSORS:
        if me == PAPER:
            print("컴퓨터가 이겼습니다.")
            com_win += 1
        else:
            print("내가 이겼습니다.")
            me_win += 1
    elif com == PAPER:
        if me == ROCK:
            print("컴퓨터가 이겼습니다.")
            com_win += 1
        else:
            print("내가 이겼습니다.")
            me_win += 1
    else:
        if me == SCISSORS:
            print("컴퓨터가 이겼습니다.")
            com_win += 1
        else:
            print("내가 이겼습니다.")
            me_win += 1

print(com_win, ":", me_win, "(으)로 ", end='')
if com_win == me_win:
    print('비겼습니다.')
elif com_win > me_win:
    print('컴퓨터가 이겼습니다.')
else:
    print('내가 이겼습니다.')


# 전체 블록 잡고 tap 하면 들여쓰기, shift + tap 당기기
# 주석 Ctrl + /
