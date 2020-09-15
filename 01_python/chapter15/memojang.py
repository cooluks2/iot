# 3

# menu


# 1차, add 및 print Test
#
# class MenuItem:
#
#     def __init__(self, title, action = None):  # 디폴트 설정(title은 문자열, action은 함수)
#         self.title = title
#         self.action = action
#
#     def __str__(self):
#         return f"<MenuItem {self.title}>"
#
#     def __repr__(self):
#         return f"<MenuItem {self.title}>"
#
#     def run(self):
#         self.action()  # action을 함수로 받아 함수 호출
#
#
# class Menu:
#
#     def __init__(self):
#         self.menus = []
#
#     def add(self, menu_item):
#         self.menus.append(menu_item)
#
#     def print(self):
#         print("[메뉴]", end=' ')
#         for i, menu in enumerate(self.menus):
#             print(f"{i}:{menu.title}  ", end="")
#
#
# menu = Menu()
# menu.add(MenuItem("열기"))
# menu.add(MenuItem("저장"))
# menu.add(MenuItem("목록보기"))
# menu.add(MenuItem("종료"))
# menu.print()
#
#


# 2차, 실행(run) Test

# import sys
#
# class MenuItem:
#
#     def __init__(self, title, action = None):  # 디폴트 설정(title은 문자열, action은 함수)
#         self.title = title
#         self.action = action
#
#     def __str__(self):
#         return f"<MenuItem {self.title}>"
#
#     def __repr__(self):
#         return f"<MenuItem {self.title}>"
#
#     def run(self):
#         self.action()  # action을 함수로 받아 함수 호출
#
#
# class Menu:
#
#     def __init__(self):
#         self.menus = []
#
#     def add(self, menu_item):
#         self.menus.append(menu_item)
#
#     def print(self):
#         print("[메뉴]", end=' ')
#         for i, menu in enumerate(self.menus):
#             print(f"{i}:{menu.title}  ", end="")
#         print()
#
#     def run(self, select):
#         if select >= len(self.menus):
#             print("잘못된 메뉴 선택입니다")
#             return
#         menu_item = self.menus[select]
#         menu_item.run()
#         # self.menus[select].run()  # ☆☆☆위꺼 한줄로
#
# menu = Menu()
# item = MenuItem("열기", lambda : print("열기 실행"))
# menu.add(item)
# menu.add(MenuItem("저장,", lambda : print("저장 실행")))
# menu.add(MenuItem("목록보기", lambda : print("목록보기 실행")))
# menu.add(MenuItem("종료", lambda : print("종료 실행")))
# menu.print()
# menu.run(1)  # 저장 메뉴 실행
# menu.run(3)  # 종료 메뉴 실행
# menu.run(4)  # 잘못된 메뉴

# 3차

# Application 설정 (열기, 저장, 목록 보기, 나가기) 종료할때까지 계속 실행

import sys


class MenuItem:

    def __init__(self, title, action = None):  # 디폴트 설정(title은 문자열, action은 함수)
        self.title = title
        self.action = action

    def __str__(self):
        return f"<MenuItem {self.title}>"

    def __repr__(self):
        return f"<MenuItem {self.title}>"

    def run(self):
        self.action()  # action을 함수로 받아 함수 호출


class Menu:

    def __init__(self):
        self.menus = []

    def add(self, menu_item):
        self.menus.append(menu_item)

    def print(self):
        print("[메뉴]", end=' ')
        for i, menu in enumerate(self.menus):
            print(f"{i}:{menu.title}  ", end="")
        print()

    def run(self, select):
        if select >= len(self.menus):
            print("잘못된 메뉴 선택입니다")
            return
        self.menus[select].run()


class Application:
    def __init__(self):
        self.menu = Menu()
        self.menu.add(MenuItem("열기", self.open))
        self.menu.add(MenuItem("저장", self.save))
        self.menu.add(MenuItem("목록보기", self.print_list))
        self.menu.add(MenuItem("종료", self.exit))

    def open(self):
        print("열기를 실행합니다.")

    def save(self):
        print("저장을 실행합니다.")

    def print_list(self):
        print("목록 보기를 실행합니다.")

    def exit(self):
        sys.exit(0)  # 정상 종료

    def run(self):  # 어플리케이션이 바뀌어도 수정이 없다.
        while True:
            self.menu.print()
            sel = int(input("선택] "))
            self.menu.run(sel)


def main():
    app = Application()
    app.run()


main()