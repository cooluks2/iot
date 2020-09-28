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