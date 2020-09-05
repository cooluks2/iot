import pickle


def save(fpath, data):
    try:
        with open(fpath, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다.")
        print(e)


def load(fpath):
    try:
        with open(fpath, 'rb') as file:
            data = pickle.load(file)
            return data
    except Exception as e:
        print(f"{fpath} 파일 읽기에 실패했습니다.")


def main():
    data = [
        [1, 2, 3, 54, 45],
        [7, 8, 3, 4, 5],
        [1, 12, 13, 4, 25]
    ]

    save("./data/data2.dat", data)  # 하위 디렉토리에 data 폴더가 없으면 오류

    data2 = load("./data/data2.dat")  # 디렉토리는 새로 만들어지지 않는다.
    print(data2)


main()
