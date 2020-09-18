# 4

# 패키지
# ex16-02

# ■ 패키지
#   ○ 모듈들을 모아 놓은 디렉토리
#   ○ 반드시 __init__.py가 존재해야 함  # 패키지용 디렉토리임을 알림
#       ● 일반적으로 내용은 없음

# ■ __init__.py
#   ○ from 패키지 import *
#       ● *에 의해 임포트될 모듈 목록을 __all__ 리스트로 지정
#       ● 지정하지 않으면 모든 모듈이 임포트됨

# 이런식

from mypack.calc import *

add.outadd(1,2)
multi.outmulti(1,2)


##############################################
# ■ __init__.py

# 기능은 있지만 사용하지 않음

__all__ = ["add", "multi"]
print("add module imported")




# ex16-03
##############################################
# 써드 파티 모듈

# ■ 모듈의 내부

import sys
print(sys.builtin_module_names)

"""
('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', '_sha512', '_signal', '_sre', '_stat', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', '_warnings', '_weakref', '_winapi', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'parser', 'sys', 'time', 'winreg', 'xxsubtype', 'zipimport', 'zlib')
"""

###################################################
# ■ dir() 함수
#   ○ 모듈내 함수 목록 출력

import math
print(dir(math))

"""
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
"""

###################################################
# ■ help() 함수
#   ○ 함수의 docstring 출력

import math
help(math.hypot)

"""
Help on built-in function hypot in module math:

hypot(x, y, /)
    Return the Euclidean distance, sqrt(x*x + y*y).
"""

###################################################
# ■ 외부 모듈 관리 pip
#   ○ install : 패키지를 설치
#   ○ uninstall : 설치한 패키지를 삭제한다 .
#   ○ freeze : 설치한 패키지의 목록을 보여준다 .
#   ○ show : 패키지의 정보를 보여준다 .
#   ○ search : pyPI에서 패키지를 검색한다 .

# 라이브러리 다운로드

pip install beautifulsoup4  # beautifulsoup4를 다운받겠다. (터미널)

# External Libraries -> site-packages 에서 확인 가능

