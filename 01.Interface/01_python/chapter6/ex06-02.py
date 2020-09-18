#  이중 루프
#   ○ 루프 안에 루프를 실행

##################################################

# 구구단 4단
for a in range(1, 10):
    print('4X', a, '=', 4*a, sep='')

# 구구단
for a in range(2, 10):
    print(a, '단', sep='')
    for b in range(1, 10):
        print(a, 'X', b, '=', a*b, sep='')
    print()

##################################################

# triangle 이중루프 활용 (종속)
for a in range(1, 11):
    for b in range(a):
        print('*', end='')
    print()

# triangle 루프 한개
for y in range(1, 11):
    print('*'*y)  # 문자열*숫자 활용

##################################################

#  무한 루프
#   ○ while 문의 조건이 항상 True
#   ○ 반복 문에서 조건을 검사하여 break로 벗어남

# while True:
#   명령
#   if 탈출조건: break

print("3 + 4 = ?")
while True:
    a = int(input('정답을 입력하세요: '))
    if a == 7 : break
print('참 잘했어요.')

# for문 이용
print("3 + 4 = ?")
for b in range(3):
    a = int(input('정답을 입력하세요: '))
    if a == 7 :
        print('참 잘했어요.')
        break

# 강사님 : 대표적인 로그인 절차이다.
result = False
print("3 + 4 = ?")
for b in range(3):
    a = int(input('정답을 입력하세요: '))
    if a == 7:
        result = True
        break
if result == True: print('참 잘했어요.')
else: print('실패했습니다.')

# 일반적으로 반복횟수가 결정되면 for문, 아니면 while문

# 역삼각형 (range 감소하는 유형)
for y in range(10, 0, -1):
    print('*'*y)

