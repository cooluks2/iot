s1="대한민국"
s2="만세"
print(s1+s2)

print("싫어 "*3)
print("="*40)

print("#"*30)
print("  결과")
print("#"*30)

print(("+"+"-"*4)*4+"+")
print("  결과")
print(("+"+"-"*4)*4+"+")

# print("+----"*4+"+") #강사님
# print("  결과")
# print("+----"*4, end="+\n")

print(("-"*4+"+")*4+"-"*4)
print("  결과")
print(("-"*4+"+")*4+"-"*4)

#####################################################

print(10+int("22"))
# print(10 + int("22.5")) #오류 실수모양 문자형은 정수 변환 X
                          #print(10 + int(22.5)) 이건 가능
print(int("1a",16))
print(int("15",8))

# float() : 실수 변환 함수
# round(숫자 [,반올림 자리수]) : 실수 반올림 함수

print(int(2.54))
print(round(2.54))
print(round(2.54,1))
print(round(123456,-3))
