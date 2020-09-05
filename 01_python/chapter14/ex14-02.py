# 파일 관리

# ■ 파일 관리 함수
#   ○ shutil.copy(a, b)
#   ○ shutil.move(a, b)
#   ○ shutil.rmtree(path)  # 비어있는 directory만 삭제 가능
#   ○ os.rename(a, b)
#   ○ os.remove(f)

#   리눅스 용
#   ○ os.chmod(f, m)
#   ○ shutil.chown(f, u, g)
#   ○ os.link(a, b)
#   ○ os.symlink(a, b)

import shutil

shutil.copy("live.txt", "live2.txt")

######################################################
# ■ 디렉토리 관리 함수(1)
# ○ os.chdir(d) # change
# ○ os.mkdir(d) # make ☆ (이미 존재하면 예외)
# ○ os.rmdir(d) # remove
# ○ os.getcwd()  # 현재 working directory 문자열 리턴
# ○ os.listdir(d) # directory 목록
# ○ glob.glob(pattern)
# ○ os.path.isabs(f)  # 절대경로 검사
# ○ os.path.abspath(f)  # 상대경로 -> 절대경로
# ○ os.path.realpath(f)
# ○ os.path.exists(f)  # 경로 존재 검사 ☆
# ○ os.path.isfile(f)  # 파일인지 검사
# ○ os.path.isdir(f)  # directory인지 검사

# is로 시작하는 함수는 True, False만 리턴

import os

files = os.listdir('/workspace/01_Python')
for f in files:
    print(f)

# 터미널 창에서 dir /b 와 같다.

"""
chapter10
chapter11
chapter12
chapter13
chapter14
chapter3
chapter4
chapter5
chapter6
chapter7
chapter8
chapter9
ex01.py
"""

######################################################
# ■ 디렉토리 관리 함수(2) - file과 directory 모두 출력

import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = os.path.join(path, f)  # 두 문자열을 결합하는데 \ 얘를 끼워줌
                                          # file과 directory를 결합할때 사용
                                          # OS마다 달라 번거로울 때 이용
        if os.path.isdir(fullpath):
            print("[%s]"%fullpath)
            dumpdir(fullpath)  # 재귀호출
        else:
            print("\t" + f)
dumpdir("/workspace/01_Python")

######################################################
# 14.3은 데이터베이스 배운 뒤에~