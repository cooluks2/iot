# 반복문

#  while 문
#   ○ 조건이 참인 동안 명령 블럭을 실행
#       while 조건:
#            명령 블록

# while 반복문(1)

student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리합니다.")
    student += 1  # 복합 대입 연산자

####################################################
# while 반복문(2) 1~100 짝수의 합

num = 2
total = 0
while num <= 100:
    total += num
    num += 2
print("total = ", total)

####################################################
#
# while 반복문(2) 1~100 홀수,짝수의 합

num = 1
total1 = 0
total2 = 0
while num <= 100:
    if num%2 == 0:
        total1 += num
    else:
        total2 += num
    num += 1
print("odd total = ", total1, "\neven total = ", total2)

# exit code가 -1이면 비정상종료, 0이면 정상종료.






####################################################
#  for 문(1)
#   ○ 컬렉션의 요소를 하나씩 꺼내 명령 블럭을 실행
#   ○ 컬렉션의 모든 요소를 다 사용하면 반복을 끝냄
#       for 제어변수 in 컬렉션:
#           명령

for student in [1,2,3,4,5]:
    print(student, "번 학생의 성적을 처리한다.")

####################################################
#  for 문(2)
#   ○ range(시작, 끝, 증가값) # 끝은 포함되지 않음
                            # 증가값을 생락하면 1이다.
                            # 시작값을 생략하면 0

# 1~100 짝수의 합

total = 0
for num in range(2,101,2):
    total += num
print("total =", total)

####################################################

#  제어 변수의 활용

for a in range(5):
    print("이 문장을 반복합니다.")

for x in range(1,51):
    if (x % 10) == 0:
        print('+', end = '')
    else:
        print('-', end = '')


####################################################

#  break
#   ○ 반복문을 벗어나게 함

score = [92, 86, 68, 120, 56]
for s in score:
    if (s < 0) or (s > 100):
        print(s, "은(는) 데이터를 벗어났습니다.") # 이거처럼
        break # 그냥 하면 중단된 이유가 안나온다. break 위에 메시지를 남기자.
    print(s)
print('성적 처리 끝')

####################################################
#  continue
#   ○ continue 이후 멸령을 실행하지 않고 다음 반복을 시작


score = [92, 86, 68, -1, 56]
for s in score:
    if s == -1:
        continue
    print(s)
print('성적 처리 끝')

####################################################