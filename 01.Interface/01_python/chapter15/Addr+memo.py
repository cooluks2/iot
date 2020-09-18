# 5
# 이전 두 예제 상속

import sys


class Application:  # 부모클라스에 공통적인 작업을 정의
    def __init__(self):
        self.menu = Menu()  # 공통

    def run(self):  # 공통
        while True:
            self.menu.print()
            sel = int(input("선택] "))
            self.menu.run(sel)


class NotepadApp(Application):
    def __init__(self):
        super().__init__()
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
        sys.exit(0)


class MenuItem:

    def __init__(self, title, action = None):
        self.title = title
        self.action = action

    def __str__(self):
        return f"<MenuItem {self.title}>"

    def __repr__(self):
        return f"<MenuItem {self.title}>"

    def run(self):
        self.action()


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


class AddressBookApp(Application):
    pass  # 이런식으로 만들면 앱 하나를 더 만들 수 있다.


def main():
    app = NotepadApp()  # 자식을 호출
    app.run()


main()
