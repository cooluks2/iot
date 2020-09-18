# 가변 인수
  ○ 인수의 수가 고정되지 않음
  ○ 호출시 원하는 만큼 인수를 지정
  ○ 함수에서는 이를 튜플 변수로 받음
  ○ 일반 인수 뒤에만 올 수 있음
  ○ 하나만 사용 가능

def 함수명(*인수명):
  명령 블럭


def intsum(*ints):
    total = 0
    for num in ints:
        total += num

    return total


print(intsum(1, 2, 3))
print(intsum(5, 7, 9, 11, 13))
print(intsum(8, 9, 6, 2, 9, 7, 5, 8))

추가적으로 가변인수는 인수 목록 마지막에만 올 수 있다.
intsum(s, *ints) 꼴만 가능





########################################################
# 인수의 기본값
  ○ 함수 호출시 인수가 지정되지 않았을 때 사용할 값
  ○ 함수 정의시 인수에 값을 대입
  ○ 인수 목록의 마지막 부분에 배정 (∵ calcstep(2)의 의미가 몇번째 인수랑 매칭되는 지 모름)
  ○ 중간에 배정시 구분 불가


def calcstep(begin, end, step = 1): # 전달이 되면 그 값, 안되면 기본값
    total = 0
    for num in range(begin, end +1, step):
        total += num

    return total


print("1 ~ 10 =", calcstep(1, 10, 2))
print("2 ~ 10 =", calcstep(1, 100))

# 모듈(module) : 핵심 용어 -> 부품 ; 모듈화한다.
# 여기서는 코드 블록 규격화
# 함수 장점 : 블랙박스화 시킬 수 있다.
# blackbox : 안을 모르겠다. 대신 입출력을 앎. ex: print()
# whitebox : 안을 들여다 볼 수 있는 상황
# blackbox test : 많은 입력으로 출력을 알아냄

# 키워드 인수 : print() 에서 사용했었다.

# 뒷부분은 나중에 다룸 (∵dictionary 아직 다루지 않음)
# pdf 14~20 skip
