# 1
# 고스톱 패 섞기 및 패 분배
# 패의 수 : 48
#
# 게임 인원수: 3
#
# deck = []
# users = [
#     [],    #사용자 1의 패
#     [],    #사용자 2의 패
#     []     #사용자 3의 패
# ]
#
# 최종 출력:
# 각 사용자의 패, 남은패를 출력하세요.

# 내 풀이

import random

def print_result(deck, users):
    for n in range(len(users)):
        print(n+1,"번째 사용자 : ", users[n])
    print("남은 패(", len(deck), "장)", sep = "")
    print(sorted(deck))

def assign(deck, users):
    for n in range(len(users)):
        users[n] = deck[0:7]
        del deck[0:7]

def init(user_num):
    deck = [ n for n in range(1, 49)]
    users = [ [] for i in range(user_num)]
    random.shuffle(deck)
    return deck, users

def main():
    user_num = int(input("게임 인원수를 입력하세요: "))
    deck, users = init(user_num)  # 패 섞기
    assign(deck, users)  # 패 분배하기
    print_result(deck, users)  # 결과 출력

main()

# 인원의 카드를 회수하는 것은 c=users.pop(k) 이후 .extend(c) 를 이용하자.
# 유저 번호는 유지해야하니. 그리고 다시 셔플

# a == b 확인할 때 4개 씩 잘라서
# 0 1 2 3 / 4 5 6 7 / 8 9 10 11
# 이런식으로 나누기 위해서는 몫을 이용
# 행렬도 몫과 나머지 이용하여 index 활용