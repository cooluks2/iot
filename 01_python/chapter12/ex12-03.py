# 난수

# ■ random 모듈
#   ○ .random()
#       ● 0 ~ 1 사이의 난수 리턴 (1은 미포함)

import random
for i in range(5):
    print(random.random())

"""
0.31613467782098836
0.9210269418989194
0.37451066214301465
0.7120744921368977
0.16548941180523558
"""

###########################################
# ■ random 모듈(1)
#   ○ .randint(begin, end)
#       ● begin ~ end 사이의 정수 난수를 리턴 (end도 포함)
#   ○ .randrange(begin, end)
#       ● begin ~ end 사이의 정수 난수를 리턴 (end도 포함되지 않음 )
#   ○ .uniform(begin, end)
#       ● begin ~ end 사이의 실수 난수를 리턴 (end 미포함)

import random

for i in range(5):
    print(random.randint(1, 10))

"""
7
5
1
4
10
"""

###########################################

import random

for i in range(5):
    print(random.randrange(1, 10))

"""
6
4
2
9
3
"""

###########################################


import random
for i in range(5):
    print(random.uniform(1, 10))

"""
5.545056961964819
1.2273746287541747
5.6900833492861285
5.568495544111174
7.88719856182608
"""

###########################################
# ■ random 모듈(2)
#   ○ .choice(시퀀스)
#       ● 시퀀스에서 랜덤하게 요소 선택하여 리턴

import random

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.choice(food))
"""
군만두
"""

######################### 위와 같다
i = random.randrange(len(food))
print(food[i])
"""
짜장면
"""

###########################################
# ■ random 모듈(3)
#   ○ .shuffle(시퀀스)
#       ● 시퀀스의 내용을 랜덤하게 섟음

# 리턴값이 없고 원본을 shuffle 한다.

import random

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(food)
random.shuffle(food)  # call by reference
print(food)

"""
['짜장면', '짬뽕', '탕수육', '군만두']
['군만두', '짬뽕', '탕수육', '짜장면']
"""

###########################################
# ■ random 모듈(4)
#   ○ .sample(시퀀스, count)
#       ● 시퀀스에서 랜덤하게 count개의 요소 리턴

import random

food = ["짜장면", "짬뽕", "탕수육", "군만두"]
print(random.sample(food, 2))

"""
['군만두', '짬뽕']
"""

####################################### 로또
import random

nums = random.sample(range(1, 46), 6)
nums.sort()
print(nums)

"""
[4, 13, 15, 33, 37, 41]
"""

# 확률을 조절하면서 뽑기 위해서는 간격을 조정. 정규분포 이용하면 좋다.

