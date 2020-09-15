# 문자열

#  문자열
#   ○ 큰 따움표("), 작은 따움표(')로 묶음
#        한 줄로 표현
#   ○ 삼중 따움표(""")
#        여러 줄로 표현 가능
#   ○ 여는 따움표와 닫는 따움표는 동일해야 함
#   ○ 따움표 안에 동일한 따움표는 사용하지 못함

#  문자열 확장(문자 이스케이프)
#   ○ 개행 문자와 같은 특수 문자를 표기하는 방법

a = "I Say \"Hello\" to you"
print(a)
a = 'I Say \'Hello\' to you'
print(a)

a = 'first\rsecond'
print(a)

a='first\tsecond'
print(a)

####################################################
#  긴 문자열

s='''아
이
고'''
print(s)

l=365*24*\
    60*60
print(l)

s1 = "korea" "japan" "2002" #결합의 의미
print(s1)

s2 = ("korea"
      "japan"
      "2002") #결합의 의미
print(s2)

#  문자 코드

print(ord('a'))
print(chr(98))
for c in range(ord('A'), ord('Z')+1):
    print(chr(c), end='')

