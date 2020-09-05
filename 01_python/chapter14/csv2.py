# 5

# 원래대로 복원

def load(fpath):
    f = open(fpath, "rt")
    lines = f.readlines()
    data = []
    for line in lines:
        print(line, end='')  # 한줄의 문자열이 출력된다.
        row = line.split(',')
        print(row)  # ,를 기준으로 split 된 문자열이 출력된다.
        row = list(map(int, row))  # 문자열 요소를 정수 요소로 변환
        print(row)  # white space 문자 또한 없어진다!
        data.append(row)
    f.close()
    return data


def main():

    data = load("data.csv")
    print(data)


main()

# (이중)리스트는 binary(구조가 있다.)이다. (text data가 아니면 다 binary)
# binary <-> text 변환에서 과정이 필요하다.


#########################################################
# with ~ as 이후

def load(fpath):
    try:
        with open(fpath, "rt") as f:  # f = open(fpath, "rt")과 동일
            lines = f.readlines()
            data = []
            for line in lines:
                print(line, end='')
                row = line.split(',')
                print(row)
                row = list(map(int, row))
                print(row)
                data.append(row)
            return data
    except Exception as e:
        print(e)


def main():

    data = load("data.csv")
    print(data)

main()
