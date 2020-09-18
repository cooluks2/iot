# 사전의 value 정렬!!!!

song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

alphabet = dict()

for c in song:
    if c.isalpha() == False:
        continue

    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] += 1

def get_value(x):  # x는 튜플로 가정
    return x[1]  # 튜플의 두번째 값을 반환하는 함수

alphabet_list = list(alphabet.items())  # 튜플의 리스트
alphabet_list.sort(key=get_value, reverse=True)  # 어느 부분을 정렬해주는지 알려줘야한다. get_value 함수
# alphabet_list.sort(key=get_value)  # 오름차순


for item in alphabet_list:
    print(item)
    
# for a, c in alphabet_list:  # 이렇게도 가능
#     print(f"{a} : {c}")

"""
('e', 22)
('n', 13)
('r', 12)
('a', 12)
('w', 12)
('i', 10)
('s', 10)
('o', 10)
('t', 9)
('h', 9)
('d', 6)
('y', 5)
('l', 5)
('b', 4)
('g', 4)
('m', 3)
('c', 3)
('u', 3)
('v', 2)
('f', 2)
('p', 2)
('z', 1)
('k', 1)
('q', 1)
"""

#####################################################
"""
def get_value(x):
    return x[1]

alphabet_list.sort(key=get_value, reverse=True)

# 위 부분을 lambda 함수 이용하면 아래와 같이 바꿀 수 있다.

alphabet_list.sort(key=lambda x : x[1], reverse=True)
"""
#####################################################


