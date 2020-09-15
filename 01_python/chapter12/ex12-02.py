# 시간

# ■ 시간조사, time 모듈
#   ○ 1970년 1월 1일 자정을 기준으로 경과한 시간을 초 단위로 표현
#       --> 에폭(Epoch) 시간 또는 유닉스 시간

import time
print(time.time())  # 전세계 공통
"""
1595234097.897746
"""

import time
t = time.time()
print(time.ctime(t))  # c는 문자로 표현해달라.
"""
Mon Jul 20 17:37:07 2020
"""

import time
t = time.time()
print(time.localtime(t))  # 현재위치 기반으로 해석
"""
time.struct_time(tm_year=2020, tm_mon=7, tm_mday=20, tm_hour=17, tm_min=39, tm_sec=15, tm_wday=0, tm_yday=202, tm_isdst=0)
"""

# tm_wday: 요일, tm_yday: 연 중 일수

import time
now = time.localtime()
print(f"{now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일")
print(f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}")

"""
2020년 7월 20일
17:48:31
"""

import datetime
now = datetime.datetime.now()  # now = 모듈명.객체명.메서드
print(f"{now.year}년 {now.month}월 {now.day}일")
print(f"{now.hour}:{now.minute}:{now.second}")

"""
2020년 7월 20일
17:50:55
"""

from datetime import datetime  # 이걸 많이쓴다. 중복되는 것을 짧게
now = datetime.now()


##########################################################
# ■ 실행 시간 측정(1) (1000번 출력하는데 걸리는 시간)

import time
start = time.time()
for a in range(1000):
    print(a)
end = time.time()

print(end - start)

"""
0
1
:
999
0.015624761581420898
"""

##########################################################
# ■ 실행 시간 측정(2) (1~999까지의 합을 구하는데 걸리는 시간)
import time
start = time.time()
total = 0
for a in range(1000):
    total += a
end = time.time()

print(end - start)

"""
0.0
"""

# 속도 차이가 어마어마하다. 입출력 수행 vs 메모리 접근
# cpu가 memory에 접근하는데 걸리는 시간 단위 10**-9
# HDD 접근하는데 걸리는 시간 단위 10**-6
# 직접적인 입출력을 최소화 시키는 것이 소프트웨어 속도를 줄이는데 효과적이다.
# 그래서 데이터를 모아서 출력한다.

##########################################################
# ■ 실행 멈춤

import time

print("안녕하세요")
time.sleep(1)
print("밤에 성시경이 두 명 있으면 뭘까요?")
time.sleep(5)
print('야간투시경입니다.')

"""
안녕하세요
밤에 성시경이 두 명 있으면 뭘까요?
야간투시경입니다.
"""

##########################################################
# ■ 달력(1)

import calendar as cal

print(cal.calendar(2018))
print(cal.month(2019, 1))

"""
                                  2018

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                1  2  3  4
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       5  6  7  8  9 10 11
15 16 17 18 19 20 21      12 13 14 15 16 17 18      12 13 14 15 16 17 18
22 23 24 25 26 27 28      19 20 21 22 23 24 25      19 20 21 22 23 24 25
29 30 31                  26 27 28                  26 27 28 29 30 31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1          1  2  3  4  5  6                   1  2  3
 2  3  4  5  6  7  8       7  8  9 10 11 12 13       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      14 15 16 17 18 19 20      11 12 13 14 15 16 17
16 17 18 19 20 21 22      21 22 23 24 25 26 27      18 19 20 21 22 23 24
23 24 25 26 27 28 29      28 29 30 31               25 26 27 28 29 30
30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                      1  2
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       3  4  5  6  7  8  9
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      10 11 12 13 14 15 16
16 17 18 19 20 21 22      20 21 22 23 24 25 26      17 18 19 20 21 22 23
23 24 25 26 27 28 29      27 28 29 30 31            24 25 26 27 28 29 30
30 31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7                1  2  3  4                      1  2
 8  9 10 11 12 13 14       5  6  7  8  9 10 11       3  4  5  6  7  8  9
15 16 17 18 19 20 21      12 13 14 15 16 17 18      10 11 12 13 14 15 16
22 23 24 25 26 27 28      19 20 21 22 23 24 25      17 18 19 20 21 22 23
29 30 31                  26 27 28 29 30            24 25 26 27 28 29 30
                                                    31

    January 2019
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31
"""

##########################################################
# ■ 달력(2)

import calendar as cal
dates = ["월", "화", "수", "목", "금", "토", "일"]
day = cal.weekday(2020, 8, 15)
print(day)
print("광복절은 %s요일입니다."%dates[day])

"""
광복절은 토요일입니다.
"""


##########################################################
# 보조자료2 12. 날짜 p.7~8
#
#  time.strftime(string[, format])
#   ○ struct_time 객체를 지정한 format에 맞게 변환
#  time.strptime(format[, t])
#   ○ 지정한 문자열을 format에 맞게 해석
#  format 변환 지시자 (보조자료 참고)

import time

print(time.strftime('%Y-%m-%d %I:%M'))  # 포맷팅

timestring = '2020-07-21 09:36:11'  # 문자열 -> 원하는 개체 : 파씽
print(time.strptime(timestring, '%Y-%m-%d %I:%M:%S'))

"""
2020-07-21 09:37
time.struct_time(tm_year=2020, tm_mon=7, tm_mday=21, tm_hour=9, tm_min=36, tm_sec=11, tm_wday=1, tm_yday=203, tm_isdst=-1)
"""

###########################################################
# 같은 기능 datetime 이용(초 이하도 출력 가능)

import time
from datetime import datetime

print(time.strftime('%Y-%m-%d %I:%M:%S'))

now = datetime.now()
print(now.strftime('%Y-%m-%d %I:%M:%S.%f'))

"""
2020-07-21 09:40:21
2020-07-21 09:40:21.966702
"""