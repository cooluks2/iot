# 4
# guess 게임 두번째, 그림 출력 추가

import random

# 행맨 추가.
HANGMAN = """
---+
   |
   O
  /|\\
  / \\
"""

def printHangman(lines, i):  # 추가. 프린트용 함수 (루프)
    for line in lines[:i]:
        print(line)

def rand(start, end):
    return int(random.random()*(end-start)) + start

def main():

    number = rand(1, 100)
    hangmanLines = HANGMAN.splitlines()  # 추가. 라인별로 나눈다.
    hangmanLines.pop(0)  # 추가. 첫번째 라인 제거

    print(number)
    for i in range(1, 6):
        num = int(input(str(i)+ "번째 추측값: "))
        result = number - num

        if result == 0: # 정답
            print("정답입니다.")
            break
        elif result > 0:
            printHangman(hangmanLines, i)  # 추가. 프린트 함수 실행
            print(num, "보다는 큽니다.")
        else:
            printHangman(hangmanLines, i)  # 추가. 프린트 함수 실행
            print(num, "보다는 작습니다.")

    if result != 0:
        print('실패했습니다.\n정답은 ', number)

main()

