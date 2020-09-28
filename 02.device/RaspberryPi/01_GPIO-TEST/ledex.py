import RPi.GPIO as GPIO
import time

# callable class
class LedEx:
    def __init__(self):
        self.led_pin = 18
        GPIO.setup(self.led_pin, GPIO.OUT)

    def __call__(self):
        # 10번 반복문
        for i in range(10):
            GPIO.output(self.led_pin,1) # LED ON
            time.sleep(1) # 1초동안 대기상태
            GPIO.output(self.led_pin,0) # LED OFF
            time.sleep(1) # 1초동안 대기상태

# if __name__ == "__main__":
#     ex = LedEx()  # LedEx 인스턴스 생성자 호출
#     ex()  # LedEx 클래스의 __call__() 메서드 호출