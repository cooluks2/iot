# 3

# 파일

# 파일 입출력

# ■ 파일 쓰기
#   ○ open(파일경로, 모드)
#   ○ 모드
#       ● r : 읽기, 파일이 없는 경우 예외 발생
#       ● w : 쓰기, 파일이 없으면 새로 생김
#       ● a : 추가
#       ● x : 쓰기용으로 여나 기존 파일이 있는 경우 실패
#       ● t : text 모드로 열기 (디폴트)
#       ● b : binary 모드로 열기

# try에 open, finally에 close 해주자.
# PyCharm은 UTF-8을 사용한다. windows는 window-949를 사용(이걸로 열면 잘보인다.)


# f = open("live.txt", "wt")  # 현재 working directory에 저장된다. 터미널 왼쪽.
f = open("live.txt", "wt", encoding="utf8")  # 문자set지정

f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
f.write("""가나다라""")

f.close()

# txt 파일 생성 후 아래가 추가 됨. (기존 내용 들어간다.)
# 새로 열고 쓰면 기존 내용 버리고 다시 쓴다.

###########################################################
# ■ 파일 읽기(1)
#   ○ f.read() -> 파일 전체 내용
#   ○ f.read(n) -> n개의 내용 (바이트라서 주로 binary모드에서 사용)
#   ○ f.readline() -> 한 줄 씩
#   ○ f.readlines() -> 전체 라인 리스트
#       ● 각 라인의 끝에 개행 문자가 들어 있음

try:
    f = open("live.txt", "rt", encoding="utf8")  # 상대경로 접근(프로젝트 디렉토리)
    text = f.read()  # 파일 전체를 읽는다. 작은 파일
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()  # 파일 없으면 여기서 예외



###########################################################
# 상대경로 VS 절대경로

# 터미널
# python ex.02.py 상대경로
# python \workspace\01_python\chapter17\ex02.py 절대경로(root로 시작)

# cd 이동
# mkdir 디렉토리 만들기
# type 파일 열기
# . 자기자신
# .. 부모 directory

# Edit configurations 에서 Working directory 변경 가능

###########################################################
# 절대경로 접근

try:
    f = open("\\temp\live.txt", "rt", encoding="utf8")  # 절대경로 접근(프로젝트 디렉토리)
    # f = open("/temp/live.txt", "rt", encoding="utf8")  # / 를 써도 무방하다. 다른 곳에서도 쓸 수 있다.
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()  # 파일 없으면 여기서 예외
    
###########################################################
# 상대경로 접근 (working directory -> C:\temp)
    
try:
    f = open("test1/t.txt", "rt", encoding="utf8")  # 상대경로 접근(프로젝트 디렉토리)
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close()  # 파일 없으면 여기서 예외

"""
삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니가나다라
"""

###########################################################
# ■ 파일 읽기(2)  f.read(n) -> n개의 내용

f = open("live.txt","rt",encoding="utf8")
while True:
    text = f.read(10)  # 읽을 위치를 자동으로 갱신.
    if len(text) == 0: break
    print(text, end="")
f.close()

# 마지막은 10Byte보다 작을 수 있다. 그러면 그 만큼만 읽는다.
# n이 클수록 입출력이 속도가 빠르다.
# binary 데이터 다룰 때 작으면 512 크면 4k 정도까지

"""
삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니가나다라
"""

###########################################################
# ■ 파일 읽기(3)  f.readline() -> 한 줄 (주의: 뒤에 개행문자도 붙어있다.)

f = open("live.txt","rt",encoding="utf8")
text = ""
line = 1
while True:
    row = f.readline()
    if not row: break
    text += str(line) + " : " + row
    line += 1

f.close()
print(text)

# text 파일에서만 가능

"""
1 : 삶이 그대를 속일지라도
2 : 슬퍼하거나 노하지 말라!
3 : 우울한 날들을 견디면
4 : 믿으라, 기쁨의 날이 오리니가나다라
"""

###########################################################
# ■ 파일 읽기(4)  f.readlines() -> 전체 라인 리스트(역시 개행문자있다.)

f = open("live.txt", "rt", encoding="utf8")

for line in f:
    print(line, end="")
f.close()

"""
삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니가나다라
"""

###########################################################
# 예제 readlines 이용하여 (3)처럼 실행

f = open("live.txt", "rt", encoding="utf8")
rows = f.readlines()

for ix, row in enumerate(rows, 1):
    print(f"{ix} : {row}", end="")
f.close()

"""
1  :  삶이 그대를 속일지라도
2  :  슬퍼하거나 노하지 말라!
3  :  우울한 날들을 견디면
4  :  믿으라, 기쁨의 날이 오리니가나다라
"""

###########################################################
###########################################################
# ■ 입출력 위치
#   ○ seek(위치, 기준)
#       ● 위치
#           – 기준으로부터 얼마나 떨어진 곳인지 바이트 단위로 지정
#           – 한글의 경우 주의 필요 (Byte 중간을 읽어 글자가 쪼개질수있다.)
#       ● 기준
#           – 0: 파일의 처음 위치
#           – 1: 현재 위치
#           – 2: 파일의 끝 위치

# Byte 단위의 숫자이다.

f = open("live.txt", "rt", encoding='utf-8')
f.seek(12, 0) # 12 바이트가 문자 중간 위치에 있으므로
text = f.read() # 예외 발생
f.close()
print(text)

###########################################################
# ■ 내용 추가
#   ○ w 모드
#       ● 기존에 파일이 존재하는 경우 내용을 모두 지우고 다시 작성
#   ○ a 모두
#       ● 기존에 파일이 존재하는 경우 파일의 끝에 내용을 추가

f = open("live.txt", "at")

f.write("\n\n푸쉬킨 형님의 말씀")
f.close()

###########################################################
# ■ 파일 예외 처리 -> 강의노트 14.2 - picke

try:
    f = open("live.txt", "rt")
    text = f.read()
    print(text)
except FileNotFoundError:
    print("파일이 없습니다.")
finally:
    f.close() # 파일 열기에 실패한 경우 f가 정의되지 않아 예외 발생

# 위 부분을 개선하는 메커니즘

###########################################################
# ■ with ~ as 문 (컨텍스트 매니저)
# ○ open() 함수와 함께 with ~ as문을 사용하면 명시적으로 close() 함수를
#   호출하지 않아도 파일이 항상 닫힘.

# 예제(1)

with open('test.txt', 'r') as file:
    str = file.read()
    print(str)
# file.close

# close 하는게 있으면 with ~ as 를 이용할 수 있다.
# 아직 예외처리를 안하고 있다.


# 예제(2)
try:
    with open('test.txt', 'r') as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print("파일이 없습니다.")

###########################################################
# ■  pickle 모듈
#   ○ 파이썬 자료형 그래도 저장하고, 그대로 로드(복원)
#   ○ 반드시 binary 모드로 오픈해야 함
#   ○ 다른 언어와 호환성은 없음 (Python 자체 메커니즘)
#
#   ○ import pickle
#
#   ○ 저장하기
#       pickle.dump(data, file)
#        data: 저장할 데이터
#        file: "bw"로 오픈한 파일 객체
#   ○ 로드하기
#       data = pickle.load(file)
#        file: "br"로 오픈한 파일 객체
#        data: 복원한 데이터

# csv 만드는 작업이 간단해진다.

###########################################################
# ■ pickle 모듈(저장하기)

import pickle

def save(fpath, data):
    try:
        with open(fpath, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다.")
        print(e)

###########################################################
# ■ pickle 모듈(불러오기)

import pickle

def load(fpath):
    try:
        with open(fpath, 'rb') as file:
            data = pickle.load(file)
            return data
    except:
        print(f"{fpath} 파일 읽기에 실패했습니다.")