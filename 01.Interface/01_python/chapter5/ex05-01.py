# if 조건문
# ■ if 문
#   ○ 단일 라인 표현식
#       if 조건 : 명령




age = int(input("나이를 입력하세요 : "))

if age < 19:
    print("애들은 가라")


#####################################################
# ■ 비교 연산자(1)

a=3
if a==3:
    print('3이다')
if a>5:
    print('5보다 크다')
if a<5:
    print('5보다 작다')

#####################################################
# ■ 비교 연산자(2)

country="Korea"
if country=="Korea":
    print("한국입니다")
if country!="Korea":
    print("한국이 아닙니다")

if "korea" > "japan":
    print("한국이 더 크다")
if "korea" < "japan":
    print("일본이 더 크다")

if "Korea" > "korea":
    print("Korea가 더 크다")

#####################################################
# ■ 거짓 값

print(None, bool(None))
print(0, bool(0))
print("", bool(""))
print([], bool([]))
print((), bool(()))

#####################################################
# ■ 논리 연산자

a=3
b=4
if a==3 and b==4:
    print("OK")

a=3
b=5
if a==3 or b==4:
    print("OK")

a=3
if a>1 and a<10:
    print("OK")
if 1<a<10:
    print("OK")