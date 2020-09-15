# 리스트와 튜플
################################################

# 리스트 (서로 다른 data type이 있어도 괜찮다.)
# ■ 자료의 집합

score = [88, 95, 70, 100, 99]
total = 0
for s in score:
    total += s
print("총점: ", total)
print("평균: ", total/len(score))

"""
총점:  452
평균:  90.4
"""

print(list("Korea"))  # 리스트가 아닌 형을 list로 바꿔주는 함수

"""
['K', 'o', 'r', 'e', 'a']
"""

# str="hello" 나 list=[1,2,3] 등을 쓰면 str함수와 list함수를 이용할 수 없다.
# 많이하는 실수

################################################
# ■ 리스트의 요소(1) 읽기 (문자열과 똑같다. sequence이기 때문에)
#   ○ 리스트[인덱스]
#   ○ 리스트[begin:end:step]

# 문자열은 불변개체였지만, 리스트는 수정이 가능하다.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[:])
print(nums[2:5])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])

score = [88, 95, 70, 100, 99]
print(score[2])
score[2]=55
print(score[2])

"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[2, 3, 4]
[0, 1, 2, 3]
[6, 7, 8, 9]
[1, 3, 5]
70
55
"""

################################################
# ■ 리스트의 요소(2) ☆☆☆

def main():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = list(range(10))  # 둘이 같다.

    nums2 = nums  # 데이터 복사가 아니라 위치 정보를 복사한 것이다.
    # nums2 = nums[:] 를 이용하면 새로 구성된 데이터를 복사한다.
    # Heap의 새로운 위치에 리스트가 생긴다.
    print(nums == nums2)
    nums2[0] = -1  # nums2가 가르키고 있는 데이터 중 첫번째를 -1로 바꾼다.
    print(nums)  # 위치 정보로 가서 출력
    print(nums2)  # 위치 정보로 가서 출력
    print(nums == nums2)  # 그래서 같다.

main()

"""
True
[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
True
"""

# 리스트는 Heap에서 관리한다. Stack X
# 리스트 변수(nums,nums2)는 참조값(reference value)을 가지고 있다.

################################################
# ■ 리스트의 요소(3) 쓰기 (이미지 프로세싱할 때 많이 씀)
def main():

    nums = list(range(10))
    nums[2:5] = [20, 30, 40]  # 대체
    print(nums)
    nums[6:8] = [60, 70, 80, 90]  # 개수 많을 때
    print(nums)
    nums[6:8] = [60]  # 개수 적을 때
    print(nums)
    nums[6:6] = [100, 200] # 삽입만 할 때
    print(nums)

main()

"""
[0, 1, 20, 30, 40, 5, 6, 7, 8, 9]
[0, 1, 20, 30, 40, 5, 60, 70, 80, 90, 8, 9]
[0, 1, 20, 30, 40, 5, 60, 80, 90, 8, 9]
[0, 1, 20, 30, 40, 5, 100, 200, 60, 80, 90, 8, 9]
"""

# 기본적으로 삭제 -> 삽입 순
# 문자열은 읽기는 나눠서 되지면 쓰기는 안된다.

################################################
# ■ 리스트의 요소(4) 결합, 반복 (연산자)

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 11]
    listadd = list1 + list2  # 결합
    print(listadd)
    listmulti = list2 * 3  # 반복
    print(listmulti)

main()

"""
[1, 2, 3, 4, 5, 10, 11]
[10, 11, 10, 11, 10, 11]
"""

################################################
# ■ 이중 리스트(1)

lol = [
    [1, 2, 3], # 주석도 자유롭다.
    [4, 5],
    [6, 7, 8, 9]
]  # 리스트는 대괄호 때문에 들어쓰기 규칙, 개행 상관없다.

print(lol[0])
print(lol[2][1])

for sub in lol:  # 행의 숫자만큼 돈다.
    for item in sub:  # 열의 숫자만큼 돈다.
        print(item, end=' ')
    print()

"""
[1, 2, 3]
7
1 2 3 
4 5 
6 7 8 9 
"""


################################################
# ■ 이중 리스트(2)

def main():

    score = [
     [88, 76, 92, 98],
     [65, 70, 58, 82],
     [82, 80, 78, 88]
    ]

    total = 0
    totalsub =0

    for student in score:
        subject_total = 0
        for subject in student:
            subject_total += subject

        subjects = len(student)
        print("총점 %d, 평균 %.2f" % (subject_total, subject_total/subjects))
        total += subject_total
        totalsub += subjects
    print("전체평균 %.2f" % (total/totalsub))

main()

"""
총점 354, 평균 88.50
총점 275, 평균 68.75
총점 328, 평균 82.00
전체평균 79.75
"""

################################################
# 위에꺼 함수로 구현


def getSubjectTotal(student):  # 리스트가 오면 1:1로 대응
    subject_total = 0
    for subject in student:
        subject_total += subject

    return subject_total


def printAvg(student, subject_total):
    subjects = len(student)
    avg = subject_total / subjects
    print(f"총점 {subject_total}, 평균 {avg:.2f}")
    return subjects


def main():

    score = [
     [88, 76, 92, 98],
     [65, 70, 58, 82],
     [82, 80, 78, 88]
    ]

    total = 0
    totalsub =0

    for student in score:
        subject_total = getSubjectTotal(student)
        subjects = printAvg(student, subject_total)
        total += subject_total
        totalsub += subjects

    total_avg = total / totalsub  # 이 식이 바로 들어오는 것 보다
    print(f"전체평균 {total_avg}")  # 이것을 권장

main()

"""
총점 354, 평균 88.50
총점 275, 평균 68.75
총점 328, 평균 82.00
전체평균 79.75
"""


# 정리
# 문자열은 불변개체이다.(≒튜플)
# 문자열, 리스트, 튜플 슬라이싱 가능
# 슬라이싱 이용 추출 가능
# 리스트는 슬라이싱을 이용 쓰기도 가능
# 문자열, 리스트 : 객체. 자체적인 함수도 가지고 있다.

# 2020/07/16

