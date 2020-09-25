# 라즈베리 파이 GPIO 및 센서 활용하기

<br>

## GPIO 제어 및 테스트

-   GPIO 핀 배치

![image-20200924161214033](03_라즈베리_파이_GPIO_및_센서_활용하기.assets/image-20200924161214033.png)

<br>

### GPIO

-   General Purpose Input Output 
-   범용 입출력 포트

<br>

### GPIO 제어 모듈

-   RPi.GPIO 모듈이 기본 설치되어 있음
-   절차
    -   모듈 임포트 
        -   핀 번호 지정 방식 설정 
            -   BCM * : GPIO 핀 번호 사용 
            -   BOARD : 보드 핀 번호 사용
        -   핀 I/O 모드 설정
        -   핀 제어 
        -   마칠때 cleanup()
            -   모든 GPIO 핀을 초기화

<br>

## LED 실습

>   ~/workspace/01_GPIO-TEST

### ex01_LED_Blink.py

```python
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.(BCM 모드)
led_pin = 18 #GPIO18

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# LED 핀의 IN/OUT 설정
GPIO.setup(led_pin, GPIO.OUT)

# 10번 반복문
for i in range(10):
    GPIO.output(led_pin,1) # LED ON
    time.sleep(1) # 1초동안 대기상태
    GPIO.output(led_pin,0) # LED OFF
    time.sleep(1) # 1초동안 대기상태
    
GPIO.cleanup() # GPIO 설정 초기화
```

>   \> `ssh pi@192.168.0.10`
>
>   $ `cd workspace/`
>
>   $ `python ex01_LED_Blink.py`

<br>

<br>

## 푸시 버튼 스위치 실습(Polling 방식)

![image-20200924164944668](03_라즈베리_파이_GPIO_및_센서_활용하기.assets/image-20200924164944668.png)

### ex02_Btn_Polling.py

```python
import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 선정합니다.
button_pin = 16

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정 , PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while 1: #무한반복
    # 만약 버튼핀에 High(1) 신호가 들어오면, "Button pushed!" 을 출력합니다.
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button pushed!")
    time.sleep(0.1) # 0.1초 딜레이
```



### ex03_LED+Btn.py

```python
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# 사용할 GPIO 핀의 번호를 선정합니다.
button_pin = 16
led_pin = 18

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 입력설정 , PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(led_pin, GPIO.OUT)

try:
    while 1: #무한반복
        GPIO.output(led_pin,GPIO.input(button_pin)) # LED ON
        time.sleep(0.1) # 0.1초 딜레이
except KeyboardInterrupt:
    GPIO.cleanup()
```

>   맨 앞줄 **#!/usr/bin/python** 넣어주고 CRLF -> **LF** 후 저장
>   : ./(파일명) 으로 실행 가능 
>
>   > 실행 권한(x)이 있어서 가능

<br>

>   **파일명으로 실행**
>   $ `echo $PATH ` > 현재 디렉토리가 없다.
>
>   $ `PATH=.:$PATH` > 현재 디렉토리를 먼저 찾음 > $ `(파일명)` 으로 실행 가능
>
>   >   단, 이번 Shell에서만 적용된다.

<br>

>   **실행 관련 변경 내용 저장**
>
>   탐색기 192.168.0.10 > .bashrc 코드로 열기
>
>   맨 밑에 `export PATH=.:$PATH` 추가
>
>   ~ $ `echo $PATH`
>
>   확인

### GPIO 핀의 상태 변경 감지

-   GPIO.add_event_detect(채널, GPIO.RISING, callback=my_callback)
    -   GPIO 핀의 상태가 0 또는 1로 변경될 때 호출할 함수(my_callback)를 등록

<br>

<br>

## 푸시 버튼 스위치 실습(Event 알림 방식)

![image-20200924165923576](03_라즈베리_파이_GPIO_및_센서_활용하기.assets/image-20200924165923576.png)

### ex04_Btn_Event.py

```python
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# button_callback 함수를 정의합니다.
def button_callback(channel):
    print("Button pushed!")

# 사용할 GPIO핀의 번호를 선정합니다.
button_pin = 16

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 IN/OUT 설정 , PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Event 방식으로 핀의 Rising 신호를 감지하면 button_callback 함수를 실행합니다.
GPIO.add_event_detect(button_pin,GPIO.RISING,callback=button_callback)

try:
    while 1: #무한반복
        time.sleep(0.1) # 0.1초 딜레이
except KeyboardInterrupt:
    GPIO.cleanup()
```

<br>

### 디바운싱

![image-20200925093931129](03_라즈베리_파이_GPIO_및_센서_활용하기.assets/image-20200925093931129.png)

<br>

### ex05_Btn_LED.py

```python
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# 사용할 GPIO핀의 번호를 선정합니다.
button_pin = 16
led_pin = 18

# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM)

# 버튼 핀의 INPUT설정 , PULL DOWN 설정
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# LED 핀의 OUT설정
GPIO.setup(led_pin, GPIO.OUT)

# boolean 변수 설정
light_on = False

# button_callback 함수를 정의합니다.
def button_callback(channel):
    global light_on # Global 변수선언
    if light_on == False: # LED 불이 꺼져있을때
        GPIO.output(led_pin,1) # LED ON
        print("LED ON!")
    else: # LED 불이 져있을때
        GPIO.output(led_pin,0) # LED OFF
        print("LED OFF!")
    light_on = not light_on # False <=> True

# Event 알림 방식으로 GPIO 핀의 Rising 신호를 감지하면 button_callback 함수를 실행
# 300ms 바운스타임을 설정하여 잘못된 신호를 방지합니다.
GPIO.add_event_detect(button_pin,GPIO.RISING, callback=button_callback, bouncetime=300)

try:
    while 1: #무한반복
        time.sleep(0.1) # 0.1초 딜레이
except KeyboardInterrupt:
    GPIO.cleanup()
```

<br>

<br>

## 모듈화

### python_lib/myapp.py

기존 myapp.py 이용

```python
import sys

class MenuItem:
    def __init__(self, title, action):
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
        self.menus= []

    def add_menu(self, menu_item):
        self.menus.append(menu_item)

    def print(self):
        print("[메뉴] ", end="")
        for i, menu in enumerate(self.menus):
            print(f"{i}:{menu.title}  ", end="")
        print()

    def run(self, select):
        if select >= len(self.menus):
            print("잘못된 메뉴 선택입니다.")
            return
        self.menus[select].run()        



class Application:
    def __init__(self):
        self.book = [1, 2, 3]
        self.menu = Menu()
        self.create_menu(self.menu)

    def create_menu(self, menu):	
        pass

    def exit(self):
        sys.exit(0)

    def run(self):
        while True:
            self.menu.print()
            sel = int(input("선택] "))
            self.menu.run(sel)
            print()        
```

>   **pi/python_lib/myapp.py** 저장
>
>   .bashrc 파일 끝 `export PYTHONPATH=/home/pi/python_lib` 추가
>
>   등록 $ `source ~/.bashrc`
>
>   확인 $ `echo $PYTHONPATH`
>
>     
>
>   vscode에 **pi/python_lib/** workspace 추가

<br>

### python_lib/piapp.py

```python
from myapp import *
import RPi.GPIO as GPIO

class PiApplication(Application):
    def __init__(self):
        super().__init__()
        GPIO.setmode(GPIO.BCM)

    def exit(self):
        GPIO.cleanup()
        sys.exit(0)
```

<br>

### 01_GPIO-TEST/gpioapp.py

```python
from piapp import *
import RPi.GPIO as GPIO

from ledex import LedEx
from btnex import btnex
from btneventex import BtnEventEX

class GpioApp(PiApplication):
    def __init__(self):
        super().__init__()

    def create_menu(self, menu):	
        menu.add_menu(MenuItem("종료", self.exit))
        menu.add_menu(MenuItem("LED", LedEx()))
        menu.add_menu(MenuItem("Button", BtnEx()))
        menu.add_menu(MenuItem("Button Event", BtnEventEX()))

if __name__ == "__main__"
    app = GpioApp()
    app.run()
```

<br>

### 01_GPIO-TEST/ledex.py

```python
import RPi.GPIO as GPIO
import time

# callable class
class LedEx:
    def __init__(self):
        pass

    def __call__(self):
        print("LedEx call")


if __name__ == "__main__":
    ex = LedEx()  # LedEx 인스턴스 생성자 호출
    ex()  # LedEx 클래스의 __call__() 메서드 호출
```

**~/workspace/01_GPIO-TEST $ `python ledex.py`**

LexEx call

___



<br>

<br>

<br>

## PWM으로 LED 실습

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>

<br>