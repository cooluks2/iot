# 그 외의 타입
#  진위형(부울린)
#   ○ True, False 두 가지 값만 가짐
#  None
#   ○ 어떠한 값도 없음을 나타냄

a=5
b=a==5
print(type(b))
print(b)

#  컬렉션 소개
#  ○ List


member=['손오공','저팔계','사오정','삼장법사']
print(type(member))
print(member)

for m in member:
    print(m,'출동')

#  컬렉션 소개
#  ○ Tuple
#       읽기 전용

membertuple = ('손오공','저팔계','사오정','삼장법사') #읽기 전용 빠름
print(type(membertuple))
for m in membertuple:
    print(m,'출동')

