# 2
# 리스트 관리
# CRUD -> 용어
# Python tutorial 검색 키워드

# ■ 삽입(1)
# ○ .append(값) ★★★
#   ● 리스트의 끝에 값을 추가
# ○ .insert(위치, 값)
#   ● 지정한 위치에 값을 삽입

nums = [1, 2, 3, 4]  # empty list -> nums=[]
nums.append(5)
print(nums)

nums.insert(2, 99)
print(nums)


######################################################
# 예제

nums=[]
for n in range(100):
    r = rand(1, 100)  # 예전에 만든 함수
    nums.append(r)

# 랜덤한 숫자 100개가 담긴 list가 만들어진다.
# 다만 숫자가 겹칠 수는 있다.

######################################################
# 위 예제 범용적인 함수로 만들기
def getRandomList(start, end, count):
    nums=[]
    for _ in range(count):  # 변수 _ 를 이용해서 안쓰이는 변수 대신 사용한다.
        r = rand(start, end)
        nums.append(r)
    return nums



######################################################
# ■ 삽입(2)
nums = [1, 2, 3, 4]
nums[2:2] = [90, 91, 92]  # 새로운 값들을 삽입
print(nums)

"""
[1, 2, 90, 91, 92, 3, 4]
"""

nums = [1, 2, 3, 4]
nums[2] = [90, 91, 92]  # 지정한 위치의 엘리먼트에 리스트 대체 ☆☆☆
print(nums)

"""
[1, 2, [90, 91, 92], 4]
"""

######################################################
# ■ 리스트 연결
#   ○ 리스트1.extend(리스트2)
#   ○ 리스트1 = 리스트1 + 리스트2

list1 = [1, 2, 3, 4, 5]
list2 = [10, 11]
list3 = list1 + list2  # 새로운 리스트를 리턴
print(list3)
list1.extend(list2)  # 기존 리스트를 확장
print(list1)

"""
[1, 2, 3, 4, 5, 10, 11]
[1, 2, 3, 4, 5, 10, 11]
"""


######################################################
# ■ 삭제(1)
#   ○ .remove(값)
#       ● 리스트에서 값을 찾아 첫번째 해당 요소를 제거
#   ○ del(리스트[인덱스])
#       ● 지정한 인덱스의 요소를 제거
#   ○ [시작:끝] = []
#       ● 지정한 범위의 요소를 제거


score = [88, 95, 70, 100, 99, 88, 78, 50]
score.remove(100)
print(score)

del(score[2])
print(score)

score[1:4]=[]
print(score)

"""
[88, 95, 70, 99, 88, 78, 50]
[88, 95, 99, 88, 78, 50]
[88, 78, 50]
"""

######################################################
# ■ 삭제(2) ★★★
#   ○ .pop()
#       ● 리스트의 끝 요소를 삭제하고 삭제한 요소를 리턴
#   ○ .pop(인덱스)
#       ● 지정한 인덱스의 요소를 삭제하고 삭제한 요소를 리턴

score = [88, 95, 70, 100, 99]
print(score.pop())
print(score)
print(score.pop())
print(score)
print(score.pop(1))
print(score)

"""
99
[88, 95, 70, 100]
100
[88, 95, 70]
95
[88, 70]
"""

######################################################
# ■ 삭제(3)
# Queue -> First In First Out -> FIFO
# Stack -> Last In First Out -> LIFO

score = [88, 95, 70, 100, 99]
score.append(50)
print('Queue', score)
score.pop(0)
print('Queue', score)
score.pop(0)
print('Queue', score)
score.append(67)
print('Queue', score)
score.append(98)
print('Queue', score)

"""
Queue [88, 95, 70, 100, 99, 50]
Queue [95, 70, 100, 99, 50]
Queue [70, 100, 99, 50]
Queue [70, 100, 99, 50, 67]
Queue [70, 100, 99, 50, 67, 98]
"""

score = [88, 95, 70, 100, 99]
score.append(50)
print('Stack', score)
score.pop()
print('Stack', score)
score.pop()
print('Stack', score)
score.append(67)
print('Stack', score)
score.append(98)
print('Stack', score)

"""
Stack [88, 95, 70, 100, 99, 50]
Stack [88, 95, 70, 100, 99]
Stack [88, 95, 70, 100]
Stack [88, 95, 70, 100, 67]
Stack [88, 95, 70, 100, 67, 98]
"""

######################################################
# ■ 검색
#   ○ .index(값)   ( ≒ .find(값) )
#       ● 지정한 값을 찾아 해당 요소를 리턴 , 없으면 예외 발생
#   ○ .count(값)
#       ● 지정한 값이 리스트에 몇 번 나오는지 계산하여 리턴
#   ○ len(시퀀스)
#       ● 시퀀스의 길이(요소수) 리턴
#   ○ max(시퀀스)
#       ● 시퀀스 요소중 최대값 리턴
#   ○ min(시퀀스)
#       ● 시퀀스 요소중 최소값 리턴
#   ○ 값 in 시퀀스, 값 not in 시퀀스 (단순히 있냐 없냐)
#       ● 값이 시퀀스에 포함되어 있는지 여부를 True/False로 리턴

ans = input("결제 하시겠습니까? ")
if ans in ['yes', 'y', 'ok', '예']:  # or 연산을 대신 할 수 있다.
    print("결제를 진행합니다.")
else:
    print("결제를 취소합니다.")

"""
결제 하시겠습니까? ok
결제를 진행합니다.
"""


######################################################
# ■ 정렬
#   ○ .sort([reverse=True][key=키에 적용할 함수 ])
#       ● 리스트를 정렬(디폴트는 오름차순), reverse=True로 오름차순/내림차순 선택
#       # 숫자는 key를 이용할 필요없다.
#   ○ .reverse()
#       ● 리스트의 순서를 역으로 바꿈
#   ○ sorted(시퀀스)
#       ● 지정한 시퀀스를 정렬하여 새로운 리스트로 리턴
#       # 일반 함수(메서드 아니다)

score = [88, 95, 70, 100, 99]
score.sort()
print(score)
score.reverse()
print(score)

"""
[70, 88, 95, 99, 100]
[100, 99, 95, 88, 70]
"""

score = [88, 95, 70, 100, 99]
score.sort(reverse=True)
print(score)

"""
[100, 99, 95, 88, 70]
"""

country = ["Korea", "japan", "CHINA", "america"]
country.sort()
print(country)
country.sort(key = str.lower)  # key 함수를 적용 (원본 변화X)
print(country)

"""
['CHINA', 'Korea', 'america', 'japan']
['america', 'CHINA', 'japan', 'Korea']
"""

score = [88, 95, 70, 100, 99]
sorted_score = sorted(score)
print(score)
print(sorted_score)

"""
[88, 95, 70, 100, 99]
[70, 88, 95, 99, 100]
"""

score = [88, 95, 70, 100, 99]
sorted_score = sorted(score, reverse=True)
print(score)
print(sorted_score)

"""
[88, 95, 70, 100, 99]
[100, 99, 95, 88, 70]
"""

# 중요 slicing, append, pop, sort

###############################################
# 모두 소문자로 출력하는 예제

def main():
    country = ["Korea", "japan", "CHINA", "america"]
    for i in range(len(country)):
        country[i] = country[i].lower()
    country.sort()
    print(country)

    country = ["Korea", "japan", "CHINA", "america"]
    country.sort(key=str.lower)
    for c in country:
        print(c.lower(), end=", ")

main()

"""
['america', 'china', 'japan', 'korea']
america, china, japan, korea, 
"""

