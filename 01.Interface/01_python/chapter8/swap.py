# 1
# 복습

def swap(x, y):
    temp = y
    y=x
    x=temp

    print('x', x)
    print('y', y)

a=10
b=20
swap(a, b)

print('a', a)
print('b', b)

'''
x 20
y 10
a 10
b 20
'''
# a,b는 swap 함수의 영향을 받지 않았다.
# 함수는 stack 영역 stack frame에 push, pop
# stack은 top만 볼 수 있다.
# call by value (복사본)

# 읽기는 지역 변수(stack frame) 살피고 전역 변수 살핀다. (지역 변수가 우선 순위가 높다)
# 쓰기는 지역 변수 살피고 전역 변수로 가지 않는다.

##########################################################
