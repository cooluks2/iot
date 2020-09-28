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