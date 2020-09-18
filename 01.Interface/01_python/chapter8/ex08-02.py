# 4
# 문자열 매서드 (sequence 계열 다 적용된다.)
# ■ 검색
#   ○ .find(str): str 문자열을 찾아 인덱스 반환 , 없으면 -1 반환
#   ○ .rfind(str): 뒤에서 str 문자열을 찾아 인덱스 반환 , 없으면 -1 반환
#   ○ .index(str): find()와 동일, 없으면 예외 발생 (오류)
#   ○ .count(str): str 문자열이 몇번 등장하는지 리턴

# .의 의미 : 개체


def main():
    s = "python programming"
    print(len(s))
    print(s.find('o'))  # 없으면 -1 반환
    print(s.rfind('o'))  # 없으면 -1 반환
    print(s.index('r'))  # 없으면 오류
    print(s.count('n'))

main()

"""
18
4
9
8
2
"""

########################################################
# ■ 조사(1)
#   ○ 단어 in 문자열 -> bool
#   ○ 단어 not in 문자열 -> bool
#   ○ .startswith(str) -> bool
#   ○ .endswith(str) -> bool


def main():
    s = "python programming"
    print('a' in s)
    print('z' in s)
    print('pro' in s)
    print('x' not in s)

main()

# method 라 한다.

"""
True
False
True
True
"""

########################################################
# ■ 조사(2)

def main():
    name = '홍길동'

    if name.startswith("홍"):
        print("홍씨입니다.")
    if name.startswith("김"):
        print("김씨입니다.")

    file = "figure.jpg"
    if file.endswith(".jpg"):
        print("JPG 그림 파일입니다.")

main()

"""
홍씨입니다.
JPG 그림 파일입니다.
"""

########################################################
# 기타 메서드
# ○ isalpha ○ islower ○ isupper ○ isspace ○ isalnum
# ○ isdecimal ○ isdigit ○ isnumeric ○ isidentifier ○ isprintable


height = input("키 : ")
if height.isnumeric():
    print("키 = ", height)
else:
    print("숫자만 입력하세요")

########################################################
# ■ 변경(1)
#   ○ .lower()
#   ○ .upper()
#   ○ .swapcase() : 대문자는 소문자로, 소문자는 대문자로 변환
#   ○ .capitalize() : 첫글자는 대문자 나머지는 모두 소문자로 변환
#   ○ .title(): 모든 단어의 첫 글자를 대문자로 나머지는 소문자로 변환
#   ○ .strip() : 좌우에 있는 공백을 제거
#   ○ .lstrip(): 왼쪽에 있는 공백을 제거
#   ○ .rstrip(): 오른쪽에 있는 공백을 제거

s = "hello"
s[2]='L'

# 오류
# 문자열은 불변 개체이다. (부분적으로 수정은 안된다.)


########################################################
# ■ 변경(2)
s = "Good Morning. my love KIM."

print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.capitalize())
print(s.title())
print(s)
print(s[::-1])

"""
good morning. my love kim.
GOOD MORNING. MY LOVE KIM.
gOOD mORNING. MY LOVE kim.
Good morning. my love kim.
Good Morning. My Love Kim.
Good Morning. my love KIM.
.MIK evol ym .gninroM dooG
"""


########################################################
# ■ 변경(3)

s = "    angel     "
print(s + "님")
print(s.strip() + "님")
print(s.lstrip() + "님")
print(s.rstrip() + "님")

"""
    angel     님
angel님
angel     님
    angel님
"""


########################################################
# ■ 분할(1)
#   ○ .slpit(구분자)
#       ● 구분자를 기준으로 단어를 분리하여 리스트로 리턴, 디폴트는 공백
#   ○ .splitlines()
#       ● 개행 문자를 기준으로 분리. 개행문자만 있는 경우 비어있는 문자열로 처리
#   ○ 결합문자열.join(문자열)
#       ● 글자들을 결합문자열로 연결하여 하나의 문자열로 리턴

s = "짜장 짬뽕 탕수육"
print(s.split())
s2 = "서울->대전->대구->부산"
cities = s2.split("->")
print(cities)

for city in cities:
    print(city)

"""
['짜장', '짬뽕', '탕수육']
['서울', '대전', '대구', '부산']
서울
대전
대구
부산
"""


########################################################
# ■ 분할(2)

trabler = """
강나루 건너서
밀밭 길을

구름에 달 가듯이
가는 나그네
"""  # 6줄 (처음 개행 포함, 마지막 미포함)

poet = trabler.splitlines()
for line in poet:
    print(line)

"""
강나루 건너서
밀밭 길을

구름에 달 가듯이
가는 나그네
"""


########################################################
# ■ 분할(3)

s = "._."
print(s.join("대한민국"))

"""
대._.한._.민._.국
"""

########################################################
# ■ 분할(4)

print("._.".join("대한민국"))

# 위와 동일

########################################################
# ■ 대체
#   ○ .replace(기존문자열, 대체문자열)
#       ● 기존 문자열을 대체 문자열로 대체
#   ○ .center(폭숫자)
#       ● 좌우에 공백을 채워 폭숫자만큼 문자열 길이를 맞춤
#   ○ .ljust(폭숫자)
#       ● 왼쪽에 공백을 채워 폭숫자만큼 문자열 길이를 맞춤
#   ○ .rjust(폭숫자)
#       ● 오른쪽에 공백을 채워 폭숫자만큼 문자열 길이를 맞춤

def main():
    s = "독도는 일본땅. 대마도도 일본땅"
    print(s)
    print(s.replace("일본", "한국"))
    print(s)

    message = "안녕하세요"
    print(message.center(30))
    print(message.ljust(30))
    print(message.rjust(30))

    trabler = """
    강나루 건너서
    밀밭 길을

    구름에 달 가듯이
    가는 나그네
    """

    poet = trabler.splitlines()
    for line in poet:
        print(line.center(30))


main()

"""
독도는 일본땅. 대마도도 일본땅
독도는 한국땅. 대마도도 한국땅
독도는 일본땅. 대마도도 일본땅
            안녕하세요             
안녕하세요                         
                         안녕하세요
                              
             강나루 건너서          
              밀밭 길을           
                              
            구름에 달 가듯이         
              가는 나그네          
"""

