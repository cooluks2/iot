# 3
# ■ 컴프리핸션
#   ○ [수식 for 변수 in 리스트 if 조건]
#       ● 내부의 리스트를 순회하며 각 요소에 대한 수식을 적용하여 최종 요소를 생성
#       ● if 조건을 추가하면 조건을 만족하는 요소만 추가

# [ n for n in range (1, 11) ] (＝ list(range(1, 11)) )

nums = [ n*2 for n in range(1, 11)]
for i in nums:
    print(i, end = ', ')

"""
2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 
"""

nums = []
for n in range(1, 11):
    nums.append(n*2)
print(nums)

"""
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""

print([n for n in range(1, 11) if n % 3 == 0])  # 만족하는 조건만 필터링

"""
[3, 6, 9]
"""


##########################################################
# 컴프리핸션의 대상이 되는 패턴
nums = []
for v in 시퀀스:
    ...
    value = ...
    nums.append(value)

# 비어있는 리스트에 값을 추가하는데 루프를 돈다!!


##########################################################
# 예제

def getRandomList(start, end, count):
    nums=[]
    for _ in range(count):
        r = rand(start, end)
        nums.append(r)
    return nums

def main():
    # l = getRandomList(1, 100, 6)
    l = [ rand(1,100) for _ in range(6)]
    print(l)

main()

# 둘이 같다.