# 1
# 복습 2020-07-17

def findMin(*numbers):
    min = 999999
    for num in numbers:
        if num < min:
            min = num
    return min

def findMax(*numbers):
    max = -999999
    for num in numbers:
        if num > max:
            max = num
    return max

min = findMin(2, 7, 5, -1, 20)
print('최소값: ', min)

"""
최소값:  -1
"""

max = findMax(2, 7, 5, -1, 20)
print('최대값: ', max)

"""
최대값:  20
"""

# lst = [2, 7, 5, -1, 20]
# max = findMax(lst)
# print('최대값: ', max)

# 위 처럼하면 finMax([2, 7, 5, -1, 20]) 이렇게 넘어간다.
# 첫번째 요소로 리스트가 넘어간다. 오류
# 루프를 한번 돈다. if에서 int와 list 비교하면서 error


lst = [2, 7, 5, -1, 20]
max = findMax(*lst)
print('최대값: ', max)

# 해결방법
# lst를 쪼개준다. print(*lst) 하면 2 7 5 -1 20

# 함수 정의 앞에 붙은 *는 묶어라
# 호출 할 때 붙은 *는 펼쳐라

# 曰 : a[0] -> index 0
# 위의 최대, 최소 함수는 범용적이지 않다.

def findMax(*numbers):
    max = numbers[0]
    for num in numbers[1:]:
        if num > max:
            max = num
    return max
