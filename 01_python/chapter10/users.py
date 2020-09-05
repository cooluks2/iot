# 2
# 회원 정보 dict(id, password)

# 내 풀이

users = {
    "go":"g1234",
    "hong":"h1234"
}

"""
[문제]
사용자로부터 id와 password를 입력 받아 로그인 성공 여부를 출력 한다.

[성공시]
로그인에 성공했습니다. 반갑습니다. "<id>님"

[실패시]
<id>는 존재하지 않습니다:
비밀번호가 틀렸습니다.

실패시 최대 3번 시도 가능
"""


def main():

    for _ in range(3):
        ID = input("ID를 입력하세요. ")
        PW = input("PW를 입력하세요. ")

        if ID in users:
            if PW == users.get(ID):
                print(f'로그인에 성공했습니다. 반갑습니다. "{ID}님"')
                break
            else:
                print("비밀번호가 틀렸습니다..")
        else:
            print(f"{ID}는 존재하지 않습니다. ")


main()



###########################################################
# 강사님 (메인 함수를 간단하게 하자. 줄거리처럼 나머진 함수가 하게)

users = {
    "go":"g1234",
    "hong":"h1234",
}



def get_user_info():
    user_id = input("사용자 ID : ")
    password = input("비밀번호 : ")
    return user_id, password


def check_login(user_id, password):
    if user_id not in users:
        print(f"{user_id}는 존재하지 않는 ID 입니다. ")
        return False
    elif users[user_id] == password:
        return True
    else:
        print("비밀번호가 틀렸습니다..")
        return False


def print_result(result, ueer_id):
    if result:
        print(f"로그인에 성공했습니다. 반갑습니다. {ueer_id}님")
    else:
        print("로그인에 실패했습니다. \n다음 기회에...")


def main():
    result = False  # 로그인 결과 상태 저장, 디폴트 False

    for i in range(3):  # 최대 3회 시도
        user_id, password = get_user_info()  # User ID, Password 입력
        result = check_login(user_id, password)  # 로그인 검사
        if result:  # 로그인 성공시 탈출
            break

    print_result(result, user_id)  # 결과 출력

main()

# 함수를 많이 이용해야겠다.

# 데이터 베이스를 대신 할 수 있는 가장 적합한 대안이다.


###########################################################