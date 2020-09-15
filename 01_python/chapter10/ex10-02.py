# 집합

# ■ 집합 정의
#   ○ { 값1, 값2, ... }
#   ○ 값의 중복을 허용하지 않음

#   ○ set(다른 시퀀스)
#       ● 집합 변환 함수
#   ○ .add(값)
#       ● 집합에 값 추가 , 이미 값이 있으면 추가하지 않음
#   ○ .remove(값)
#       ● 집합에서 값을 제거 , 값이 없는 경우 예외 발생

print(set('aaabbbccc'))  # 문자열 -> 글자 하나하나가 원소가 된다.
print(set([12, 34, 56, 78]))
print(set(('홍길동', '고길동','둘리')))
print(set({'boy': '소년', 'school': '학교', 'book': '책'})) # 사전의 키 목록을 집합으로 변환
print(set())  # 비어있는 집합

"""
{'a', 'b', 'c'}
{56, 34, 12, 78}
{'고길동', '둘리', '홍길동'}
{'boy', 'school', 'book'}
set()
"""

# []:list, ():tuple, "":문자열, {}:사전, set():비어있는 집합

asia = {'korea', 'china', 'japan'}
asia.add('vietnam')
asia.add('korea')
asia.remove('japan')
print(asia)

"""
{'vietnam', 'china', 'korea'}
"""

#############################################################
# ■ 집합 연산(1) 중요도x
# |:합집합, &:교집합, -:차집합, ^:배타적 차집합
# <=, >= : 부분집합, <,> : 진부분집합

twox = { 2, 4, 6, 8, 10, 12 }
threex = { 3, 6, 9, 12, 15 }

print("교집합", twox & threex)
print("합집합", twox | threex)
print("차집합", twox - threex)
print("차집합", threex - twox )
print("배타적 차집합", twox ^ threex )

"""
교집합 {12, 6}
합집합 {2, 3, 4, 6, 8, 9, 10, 12, 15}
차집합 {8, 2, 10, 4}
차집합 {9, 3, 15}
배타적 차집합 {2, 3, 4, 8, 9, 10, 15}
"""
