# 1
# 사전(Dictionary)과 집합 (순서 의미 없다. index X)

# key는 사전의 단어처럼 중복되면 안된다.
# value는 사전의 설명처럼 중복되어도 상관없다.

# ■ 키와 값의 쌍(1)
# ○ {
#        "키": 값,
#         ...
#    }

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}
print(dic)

"""
{'boy': '소년', 'school': '학교', 'book': '책'}
"""


#######################################################
# ■ 키와 값의 쌍(2)

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}

print(dic['boy'])  # index와 비슷한데 숫자대신 key
print(dic['book'])

name = 'boy'
print(dic[name])

"""
소년
책
소년
"""

# print(dic['girl']) # 오류


#######################################################
# ■ 키와 값의 쌍(3)

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}

print(dic.get('boy'))
print(dic.get('girl'))  # 인자가 없다.
print(dic.get('girl', '사전에 없는 단어입니다.'))

"""
소년
None
사전에 없는 단어입니다.
"""

#######################################################
# ■ 키와 값의 쌍(4)

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}

if 'student' in dic:
    print('사전에 있는 단어입니다.')
else:
    print('이 단어는 사전에 없습니다.')

"""
이 단어는 사전에 없습니다.
"""

#######################################################
# ■ 사전 관리(1)
#   ○ 사전[키]
#       ● 키의 값을 리턴, 키가 존재하지 않는 경우 예외 발생
#   ○ 사전.get(키 [, 기본값])
#       ● 키의 값을 리턴, 키가 존재하지 않는 경우, None 리턴, 키가 없을 때 리턴할 값 지정 가능
#   ○ .keys()
#       ● 키 목록 리턴
#   ○ .values()
#       ● 값 목록 리턴
#   ○ .itmes()
#       ● (키,값) 튜플 목록 리턴

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}

dic['boy'] = '남자아이'  # 기존값 수정
dic['girl'] = '소녀'  # 새로운 엔트리 추가
del dic['book']  # 기존 엔트리 삭제
print(dic)

"""
{'boy': '남자아이', 'school': '학교', 'girl': '소녀'}
"""

# 조건의 예외가 없음을 보장하면 사전[키] 아니면 사전.get(키 [, 기본값]) 이용


#######################################################
# ■ 사전 관리(2)

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}

print(dic.keys())
print(dic.values())
print(dic.items())

"""
dict_keys(['boy', 'school', 'book'])
dict_values(['소년', '학교', '책'])
dict_items([('boy', '소년'), ('school', '학교'), ('book', '책')])
"""

# type이 list가 아님
# type 함수 써보면 dict_keys 이런 식으로 나옴


#######################################################
# ■ 사전 관리(3)
# 직관적으로 키 순회하는 방법

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}

keylist = dic.keys()
for key in keylist:     # for key in dic.keys(s):
    print(key, dic[key])  # 이 경우는 사전안에 key가 모두 있으므로 error X

"""
boy 소년
school 학교
book 책
"""

#######################################################
# ■ 사전 관리(4)
# list 변환 함수

dic = {
    'boy': '소년',
    'school': '학교',
    'book': '책'
}

li = list(dic.keys())
print(li)
li = list(dic)  # 이것도 사전의 key만 list 변환하는 것이다.
print(li)

"""
['boy', 'school', 'book']
['boy', 'school', 'book']
"""


#######################################################
# ■ 사전 관리(5)
# Dictionary 는 + 기능을 지원하지 않음

dic = { 'boy': '소년', 'school': '학교', 'book':'책'}
dic2 = { 'student': '학생', 'teacher': '선생님', 'book':'서적'}

dic.update(dic2)
print(dic)

"""
{'boy': '소년', 'school': '학교', 'book': '서적', 'student': '학생', 'teacher': '선생님'}
"""

# update 된다.

#######################################################
# ■ 사전 관리(6)
# 함수 dict() 형태를 맞춰줘야한다. (key, value)

li = [
    ['boy', '소년'],
    ['school', '학교'],
    ['teacher', '선생님']
]

dic = dict(li)
print(dic)

"""
{'boy': '소년', 'school': '학교', 'teacher': '선생님'}
"""

# 반대로 할때는 .items() 이용


#######################################################
# ■ 사전 활용(1)
# 예전 이중 리스트는 이름이 없었다.

"""
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
]
"""

score = {
    "홍길동" : [88, 76, 92, 98],
    "고길동" : [65, 70, 58, 82]
}

score.get('고길동')  # score['고길동']은 없으면 오류가 난다.

# 이와 같이 이름을 mapping (로그인 서비스도 이런식으로)

#######################################################
# ■ 사전 활용(2)

song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()

for c in song:  # 문자(알파벳) 하나씩 순회
    if c.isalpha() == False:  # 알파벳인지 확인
        continue

    c = c.lower()  # 소문자로 통일
    if c not in alphabet:  # 알파벳이 빈 사전에 없을 때 1
        alphabet[c] = 1  # 여기서 key와 value가 모두 들어간다.
    else:  # 알파벳이 사전에 이미 있을 때 +1
        alphabet[c] += 1

print(alphabet)

"""
{'b': 4, 'y': 5, 't': 9, 'h': 9, 'e': 22, 'r': 12, 'i': 10, 'v': 2, 's': 10, 'o': 10, 'f': 2, 'a': 12, 'l': 5, 'n': 13, 'w': 12, 'd': 6, 'p': 2, 'm': 3, 'z': 1, 'c': 3, 'k': 1, 'u': 3, 'q': 1, 'g': 4}
"""

# 순서는 생각하지 말자

#######################################################
# ■ 사전 활용(3) key 정렬 위 이어서 (알파벳 순서로 정렬)

key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet[c]
    print(c, '=>', num)

# key를 sort 한다.

"""
a => 12
b => 4
c => 3
d => 6
e => 22
f => 2
g => 4
h => 9
i => 10
k => 1
l => 5
m => 3
n => 13
o => 10
p => 2
q => 1
r => 12
s => 10
t => 9
u => 3
v => 2
w => 12
y => 5
z => 1
"""

#######################################################
# ■ 사전 활용(4) value 위 이어서 (빈도 순서로 정렬)

# 리스트 23page에서 배운 .sort(key=str.lower) 이용
# 아직은 못한다. 컬렉션 배우고.

# 결론 : 사전은 key 정렬과 value 정렬의 방식이 다르다.
