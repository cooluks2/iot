# sys 모듈
# ■ 시스템 정보

import sys

print("버전: ", sys.version)
print("플랫폼: ", sys.platform)
print("바이트 순서: ", sys.byteorder)
print("모듈 경로: ", )
for path in sys.path:  # 자신의 directory를 먼저 찾는다.
    print(path)
sys.exit(0)  # 프로그램 강제 종료, 인수로 종료 코드 지정 가능

"""
버전:  3.7.7 (default, May  6 2020, 11:45:54) [MSC v.1916 64 bit (AMD64)]
플랫폼:  win32
바이트 순서:  little
모듈 경로: 
C:\workspace\01_python\chapter12  # 실행 파일 디렉토리 위치 먼저 찾는다.
C:\workspace\01_python\chapter12
C:\Users\i\anaconda3\envs\chapter12\python37.zip
C:\Users\i\anaconda3\envs\chapter12\DLLs
C:\Users\i\anaconda3\envs\chapter12\lib  # random, datetime 등 파일 존재
C:\Users\i\anaconda3\envs\chapter12
C:\Users\i\anaconda3\envs\chapter12\lib\site-packages
# 왼쪽 External Libraries에서도 확인 가능(인터넷에서 가져오는 정보 저장되는 곳)
"""

#############################################
# ■ 명령형 인수

import sys
print(sys.argv)  # list로 실행파일 파일명, 추가 인수 저장
# [파일경로, 인자1, 인자2, ...]  # 명령창에서도 동일

"""
['C:/workspace/01_python/chapter12/test.py']
"""

# 터미널에서 python test.py a b c 입력시
# ['test.py', 'a', 'b', 'c'] 이런식으로 문자 저장

# 오른쪽 위 ▽ 누르고 Edit Configurations 에서 Parameters에 a b 209 900 입력시
# ['C:/workspace/01_python/chapter12/test.py', 'a', 'b', '209', '900']
# 공백을 전달하고 싶을 때는 따옴표("") 이용
# "hello world" 2009 입력시
# ['C:/workspace/01_python/chapter12/test.py', 'hello world', '2009']
