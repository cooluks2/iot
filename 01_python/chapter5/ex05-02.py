# 블록 구조
# ■ elif 문

age=23

if age<19:
    print("애들은 가라")
elif age<25:
    print("대학생입니다")
else:
    print("들어오세요")

#######################################################
# ■ elif 문(2)
a=int(input('점수는? '))

if a>90:
    print("A등급입니다.")
elif a>80:
    print("B등급입니다.")
elif a>70:
    print("C등급입니다.")
elif a>60:
    print("D등급입니다.")
else : #밑줄 -> 비권장사항
    print("F등급입니다.")


#######################################################
# ■ elif 문(3)

age = 23
if age < 19:
    print("애들은 가라")
else:
    if age < 25:
        print("대학생입니다")
    else:
        print("들어오세요")

#######################################################
# ■ if 문 중복

man = False
age = 22
if man == True:
    if age > 19:
        print("성인 남자입니다.")
    else:
        print("미성년 남자입니다.")
else:
    if age > 19:
       print("성인 여자입니다.") #허용은 된다
    else:
      print("미성년 여자입니다.") #이거랑

