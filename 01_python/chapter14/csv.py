# 4

# data = [
#     [1,2,3,54,45],
#     [7,8,3,4,5],
#     [1,12,13,4,25]
# ]
#
# "data.csv" 이름의 파일로 저장하세요.



def save(fpath, data):
    f=open(fpath,"wt")
    for l in data:
        l = map(str, l)  # ★★정수형을 문자열로★★★★★★★ 모르면 노가다
        row = ','.join(l)  # ★ 모르면 노가다 csv 파일을 위해 ',' 넣어준다.
        f.write(row + "\n")
    f.close()

def main():
    data = [
        [1, 2, 3, 54, 45],
        [7, 8, 3, 4, 5],
        [1, 12, 13, 4, 25]
    ]

    save("data.csv", data)

main()


#########################################################
# with ~ as 이후

def save(fpath, data):
   try:
        with open(fpath,"wt") as f:  # f = open(fpath, "wt")과 동일
            for l in data:
                l = map(str, l)
                row = ','.join(l)
                f.write(row + "\n")
   except Exception as e:  # 모든 예외 처리
       print(e)

def main():
    data = [
        [1, 2, 3, 54, 45],
        [7, 8, 3, 4, 5],
        [1, 12, 13, 4, 25]
    ]

    save("data.csv", data)

main()