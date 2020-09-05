# 모듈 : 재사용 가능
# 모듈의 가장 낮은 단위는 함수이다.

# 표준모듈

# python 에서 성격이 유사한 함수끼리 파일에 모아두었다.

# ■ 임포트(import)
#     ○ 다른 파일에 정의된 변수 , 함수, 객체 등을 사용하기 전에 이를 알리는 것
#     ○ 표준 모듈
#         ● 파이썬에서 제공하는 모듈

# import 모듈 [as alias]  # 별칭(옵션)
# from 모듈 import 함수명  # 필요한 함수만 쓸 때

import math
print(math.sqrt(2))

from math import sqrt
print(sqrt(2))

import math as m
print(m.sqrt(2))

from math import sqrt as sq
print(sq(2))

"""
1.4142135623730951
"""

# 많이하는 실수 파일명을 math.py (모듈을 찾을 때 현재 디렉토리를 먼저 본다.)
# 파일명=모듈명

##########################################################
# ■ math 모듈
#   ○ 상수
#       ● pi : 원주율 상수
#       ● tau : 원주율의 2배되는 상수
#       ● e : 자연 대수 상수
#       ● inf : 무한대 값
#       ● nan : 숫자가 아닌 값을 의미
#
#   ○ 함수
#       ● sqrt(x) ● pow(x,y) ● hypot(x,y) ● factorial(x)
#       ● sin(x), cos(x), tan(x) ● degrees(x) ● radians(x)
#       ● ceil(x) : 올림● floor(x) : 버림 ● fabs(x) ● trunc(x)
#       ● log(x, base) ● log10(x) ● gcd(a, b)

# round() : 반올림 (일반 함수)

import math

print(math.sin(math.radians(45)))
print(math.sqrt(2))
print(math.factorial(5))

"""
0.7071067811865476
1.4142135623730951
120
"""


##########################################################
# ■ 통계 모듈, statistics (중요성 x)
#   ○ 함수
#       ● mean() : 평균
#       ● harmonic_mean() : 조화평균
#       ● median() : 중앙값, 짝수인 경우 보간값 계산
#       ● median_low() : 중앙값을 구함, 집합 내의 낮은 값 선택
#       ● median_high() : 중앙값을 구함, 집합 내의 높은 값 선택
#       ● mdeian_grouped() : 그룹 연속 중앙값
#       ● mode(): 최빈값
#       ● pstdev() : 모표준편차
#       ● stddev() : 표준편차
#       ● variance() : 분산
