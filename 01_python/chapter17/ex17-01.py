# 1

# Terminal > conda install numpy 처럼 콘다에서도 인스톨 가능


# 고급 문법

# 이런게 있구나(어렵다)

# 반복자

# ■ 열거 가능 객체
#   ○ for 반복문의 순회 대상 객체
#   ○ 해당 객체의 __iter__() 메서드로 열거 가능 객체 획득
#       ● 열거 가능 개체는 __iter__() 메서드를 정의해야 함
#   ○ 매 루프마다 __next()__ 함수를 통해 다음 요소를 추출
#   ○ 더 이상 요소가 없는 데 __next()__를 호출하는 경우
#       ● StopIteration 예외가 발생하고 for 반복문을 끝냄

# foriter (for문 내부적 구현)
nums = [11, 22, 33]
it = iter(nums)
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)

"""
11
22
33
"""

#############################################################
# 예제 classiter
# for문에 동작하는 class를 만들어보자. 2글자씩 뽑아주는
# solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
# for k in solarterm:
#   print(k, end = ',')
# 결과
# 입춘,우수,경칩,춘분,청명,곡우,입하,소만,망종,하지,소서,대서,


class Seq:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        # self.index = -2  # 추가해주면 반복가능(사작할때 초기화)
        return self

    def __next__(self):
        self.index += 2  # 먼저 업데이트
        if self.index >= len(self.data):
            # self.index = -2  # 추가해주면 반복가능(마지막 인덱스에서 초기화)
            raise StopIteration  # 예외를 강제로 발생

        return self.data[self.index:self.index+2]

solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
for k in solarterm:
    print(k, end = ',')

for k in solarterm:  # 두번째 for문은 동작하지 않음
    print(k, end = ',')  # index 값이 끝으로 이동해주었기 때문에

"""
입춘,우수,경칩,춘분,청명,곡우,입하,소만,망종,하지,소서,대서,
"""

#############################################################
# ■ 제너레이터
#   ○ 객체로 순회가능한 객체를 만드는 거는 다소 귀찮은 작업
#   ○ 제너레이터 함수로 대체 가능
#   ○ 함수에서 데이터를 연속해서 리턴 (yield)
#   ○ 함수가 끝나면(또는 return 실행) StopIteration 예외 발생
#   ○ 함수를 호출하면 함수가 실행되는 것이 아니고 순회 가능 객체가 리턴
#   ○ 순회 가능 객체로 순회할 때 실제 함수가 실행 됨

# generator
def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]  # ☆☆☆ 객체로 변환이 된다.

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")  # generator 객체
print(type(solarterm))
print(solarterm)

for k in solarterm:
    print(k, end = ',')

"""
<class 'generator'>
<generator object seqgen at 0x000002D4B3081E48>
입춘,우수,경칩,춘분,청명,곡우,입하,소만,망종,하지,소서,대서,
"""

