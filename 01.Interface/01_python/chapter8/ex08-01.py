# 3
# 문자열 관리
# 리스트, 튜플, 문자 공통점 : 위치 정보(index)가 있다.

# ■ 첨자
#   ○ 문자열[정수] 0부터 인덱싱
#   ○ 문자열[-정수] 끝에서부터 인덱싱

# offset : 떨어져있는 간격

# 문자열도 for문에서 이용 가능 (문자열도 컬렉션이라고 할 수 있다.)

# 문자열 분리
s = "python"
for c in s:
    print(c, end = ",")

"""
p,y,t,h,o,n,
"""

####################################################################

s = "python"
for i in range(len(s)):  # len() : 문자열의 길이
    print(s[i], end = ",")

"""
p,y,t,h,o,n,
"""

# 문자열도 일종의 Sequence(문자열, 리스트, 튜플)


####################################################################
# 슬라이싱(1)
# ○ 문자열[begin:end:step] (end 미포함)
#   ● step: 음수이면 뒤에서부터 진행

s = "0123456789"
print(s[2:5])
print(s[3:])
print(s[:4])

"""
234
3456789
0123
"""

####################################################################
# 슬라이싱(2)

file = "20200101-104830.jpg"
print("촬영 날짜" + file[4:6] + "월" + file[6:8] + "일")
print("촬영 시간" + file[9:11] + "월" + file[11:13] + "일")
print("확장자" + file[-3:])

"""
촬영 날짜 01월01일
촬영 시간10월48일
확장자jpg
"""

# file[4:6] 등에서 end가 햇갈리면 start에 offset 추가한다고 생각하자.


####################################################################
# 슬라이싱(3)

dates = "월화수목금토일"
print(dates[::2])
print(dates[::-1])

"""
월수금일
일토금목수화월
"""

# 슬라이싱의 출력은 새로운 문자열이다.
# 회문(palindrome) 판별 때 편리하다. (=>reverse)
