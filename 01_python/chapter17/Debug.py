# 3

# 디버그 해보기!!!!!
# 이전 generator이용

def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
print(solarterm)

for k in solarterm:
    print(k, end = ',')

# line number 옆에 break poin 걸기
# Shift + F9 이용 디버그, 이후 F9 이용 다음 step

# step over
# F8은 한 라인씩 실행 (함수 안으로 안들어간다)

# 변수값이 어떻게 바뀌나 확인할 때 주로 사용한다.

