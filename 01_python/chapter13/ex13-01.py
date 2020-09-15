# 예외 처리

# 에러: 복구 불가, 예외: 복구 가능(defalut action: 종료)

####################################################
# ■ 예외
#   ○ 프로그램 실행 중 발생한 에러 --> 프로그램 실행 종료 (디폴트)

str = "89점"
score = int(str)
print(score)
print("작업완료")

"""
Traceback (most recent call last):
  File "C:/workspace/01_python/chapter13/ex13-01.py", line 9, in <module>
    score = int(str)
ValueError: invalid literal for int() with base 10: '89점'
"""

####################################################
# ■ 예외 처리
#   ○ 예외 발생을 감지하고 복구하는 방법
#
# try:
#   실행할 명령
# except 예외 as 변수:
#   오류 처리문
# else:
#   예외가 발생하지 않을 때의 처리

str = "89점"
try:
    score = int(str)
    print(score)
except:
    print("예외가 발생했습니다.")

print("작업완료")


"""
예외가 발생했습니다.
작업완료
"""

# 쓰는 습관을 가지자.

####################################################
# ■ 예외의 종류(1)
#   ○ NameError
#   ○ ValueError
#   ○ ZeroDivisionError
#   ○ IndexError
#   ○ TypeError 등

str = "89"

try:
    score = int(str)
    print(score)
    a = str[5]
except ValueError:
    print("점수의 형식이 잘못되었습니다.")
except IndexError:
    print("첨자 범위를 벗어났습니다.")

print("작업완료")

"""
89
첨자 범위를 벗어났습니다.
작업완료
"""

#  예외의 종류에 따라 적절한 except 블록으로 점프

####################################################
# ■ 예외의 종류(2) : 튜플로 묶어서 지정

str = "89"
try:
    score = int(str)
    print(score)
    a = str[5]
except (ValueError, IndexError):
    print("점수의 형식이나 첨자가 잘못되었습니다.")

print("작업완료")

"""
89
점수의 형식이나 첨자가 잘못되었습니다.
작업완료
"""

####################################################
# ■ 예외의 종류(3) : as 변수 이용 -> 변수에 예외 메세지 저장
# 많이 쓴다. 구체적인 정보 볼 수 있다.

str = "89점"
try:
    score = int(str)
    print(score)
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)

print("작업완료")

"""
invalid literal for int() with base 10: '89점'
작업완료
"""

###############################################
# 예제(1) : .print 이용하여 오류 경로 보기
def test(str):
    try:
        score = int(str)
        print(score)
    except ValueError as e:
        e.print()  # 예외가 발생하는 위치를 출력해줌
        print(e)
    except IndexError as e:
        e.print()  # StackOverflow 라고 부름
        print(e)
    print("작업완료")


def work():
    str = "89점"
    test(str)

def work2():
    str = "89"
    test(str)

def main():
    work()
    work2()

main()

###############################################
# 예제(2) : 호출하는 쪽에서 예외 처리(이용하는 쪽에서)
#        : 모든 예외 처리 except Exception

def test(str):
    score = int(str)
    print(score)

def work():
    str = "89점"
    try:
        test(str)
    except Exception as e:  # 모든 예외를 묶음
        print(e)
    print("작업완료")

def work2():
    str = "89"
    try:
        test(str)
    except Exception as e:
        print(e)
    print("작업완료")

def main():
    work()
    work2()

main()


###############################################
# ■ raise
#   ○ 개발자에 의해 임의로 예외를 발생시킴

def calcsum(n):
    if n < 0:
        raise ValueError

    total = 0
    for i in range(n + 1):
        total += i
    return total


try:
    print("~10 =", calcsum(10))
    print("~-5 =", calcsum(-5))
except ValueError:
    print('입력값이 잘못되었습니다.')

"""
~10 = 55
입력값이 잘못되었습니다.
"""