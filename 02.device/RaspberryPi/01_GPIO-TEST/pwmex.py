import RPi.GPIO as GPIO
import time

class PwmEx:
    def __init__(self):
        self.led_pin = 18

        GPIO.setup(self.led_pin, GPIO.OUT)
        self.p = GPIO.PWM(self.led_pin, 50)
        self.p.start(0)

    def __call__(self):
        try:
            while 1:
                # fade in
                for dc in range(0, 101, 5): # dc의 값은 0에서 100까지 5만큼 증가
                    self.p.ChangeDutyCycle(dc) # dc의 값으로 듀티비 변경
                    time.sleep(0.1) # 0.1초 딜레이
                
                # fade out
                for dc in range(100, -1, -5): # dc의 값은 100에서 0까지 5만큼 감소
                    self.p.ChangeDutyCycle(dc) # dc의 값으로 듀티비 변경
                    time.sleep(0.1) # 0.1초 딜레이
        
        except KeyboardInterrupt: # 키보드 Ctrl+C 눌렀을 때 예외발생
            self.p.stop() # PWM을 종료