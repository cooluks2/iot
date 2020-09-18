# 자원의 정리

# ■ finally
#   ○ 예외 발생 여부와 상관없이 항상 호출
#   ○ 작업의 마무리 작업 (cleanup) 수행

try:
    print("네트워크 접속")
    a = 2/0
    print("네트워크 통신 수행")
finally:
    print("접속 해제")

print("작업 완료")

"""
Traceback (most recent call last):
  File "C:/workspace/01_python/chapter13/ex13-02.py", line 8, in <module>
    a = 2/0
ZeroDivisionError: division by zero
네트워크 접속
접속 해제
"""

##################################################
# 예제(?)
def comm():

    try:
        print("네트워크 접속")
        d = 0
        if d != 0 :
            return
        a = 2/d
        print("네트워크 통신 수행")
    except:
        pass
    finally:
        print("접속 해제")

    # print("접속 해제")
    print("작업 완료")

def main():
    comm()

main()


"""
네트워크 접속
접속 해제
작업 완료
"""


##################################################
# ■ assert
#   ○ assert 조건, 메시지
#       ● 조건이 True이면 통과,
#       ● False이면 메시지를 가지는 예외 발생

score = 128
assert score <= 100, "점수는 100 이하여야 합니다."
print(score)

"""
Traceback (most recent call last):
  File "C:/workspace/01_python/chapter13/test.py", line 2, in <module>
    assert score <= 100, "점수는 100 이하여야 합니다."
AssertionError: 점수는 100 이하여야 합니다.
"""
