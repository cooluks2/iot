# 컬렉션의 사본 ☆☆☆☆☆

# ■ 리스트의 사본
#   ○ 시퀀스.copy() -> 시퀀스 복사본

# 예제(listcopy1)
list1 = [1, 2, 3]
list2 = list1  # 참조

print(list1 == list2)

list2[1] = 100

print(list1)
print(list2)

print(list1 == list2)

"""
True
[1, 100, 3]
[1, 100, 3]
True
"""

# Heap에 list2=list1이 참조될 뿐이다.
# list2 = list1 대입에 의해 list2가 list1의 별명이 될 뿐 독립적인 메모리까지 확보하는 것은 아니다.

###################################################
# 예제(listcopy2) 두 리스트를 완전히 독립적인 사본으로 만들기 copy 메서드

list1 = [1, 2, 3]
list2 = list1.copy()  # list2 = list1[:]와 동일(slicing)

print(list1 == list2)

list2[1] = 100

print(list1)
print(list2)

print(list1 == list2)

"""
True
[1, 2, 3]
[1, 100, 3]
False
"""

###################################################
# 예제(deepcopy1)

list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = list1.copy() # 얕은 복사
# list2 = [list0(참조), 1, 2] 이렇게 된것이다.
# list1 과 list2가 가르키는 메모리는 다름.

list2[0][1] = 'c'
list2[1] = -1
print(list1)
print(list2)
print(list0)

"""
[['a', 'c'], 1, 2]
[['a', 'c'], -1, 2]
['a', 'c']
"""

###################################################
# 예제(deepcopy2) 모듈의 메서드 (전의 메서드와 다르다.)

import copy

list0 = ['a', 'b']
list1 = [list0, 1, 2]
list2 = copy.deepcopy(list1)  # 깊은 복사 (참조를 쫒아가서 그것까지 복사)

list2[0][1] = 'c'
print(list1)
print(list2)

"""
[['a', 'b'], 1, 2]
[['a', 'c'], 1, 2]
"""

# Stack 영역은 개발자가 조정할 수 없다.
# Heap 영역은 개발자가 조정할 수 있다.

###################################################
# call by reference 예제 (p253 그림 참고) ☆☆☆

def test(numbers):
    numbers[0] = -1
    print(numbers)


def main():
    list1 = [1, 2, 3]
    test(list1)  # 참조가 복사된다. numbers = list1 과 같은 것이다.
    print(list1)

main()

"""
[-1, 2, 3]
[-1, 2, 3]
"""

###################################################
# garbage 예제(1) (p253 그림 참고)

def test2():
    numbers = [1, 2, 3]

def main():
    test2()

main()


###################################################
# garbage 예제(2) (p254 그림 참고)

def test3():
    numbers = [1, 2, 3]
    return numbers

def main():
    list3 = test3()  # list3 = numbers 한 것과 같다.
    print(list3)

main()

"""
[1, 2, 3]
"""


# 결론
# c=f(a) 는 대입 연산이 2번 이루어진다.
# 참조는 stack에서 Heap으로만 이루어진다.
# 숫자와 bool만 값이 전달된다.
# list1 = list2 (참조)
# a=10 (값 전달)
# b=a (참조)
# 숫자를 제외한 나머지는 다 참조로 운영이 된다.

# 완전히 분리된 사본을 만드려면 copy 메서드
# 이중으로 되어있는 사본을 만드려면 deepcopy

# 보통 함수 내에서 복사하고 사본을 리턴한다. (원본의 변경을 미연의 방지)

