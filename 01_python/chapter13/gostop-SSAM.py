# 2

import random

# 패 섞기
def init(user_num):
    deck = list(range(1, 49))
    random.shuffle(deck)

    users = [[] for _ in range(user_num)]
    return deck, users

# 패 분배
def assign(deck, users):
    for _ in range(7):
        for user_card in users:
            card = deck.pop()
            user_card.append(card)

def print_result(deck, users):
    print("사용자 패")
    for ix, user_cards in enumerate(users, 1):
        print(f"{ix} 번째 사용자 : ", user_cards)
    print(f"남은 패({len(deck)}장)")
    print(deck)

def main():
    user_num = int(input("게임 인원수를 입력하세요: "))
    deck, users = init(user_num)  # 패 섞기
    assign(deck, users)  # 패 분배하기
    print_result(deck, users)  # 결과 출력

main()
