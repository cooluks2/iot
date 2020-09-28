import RPi.GPIO as GPIO
import time

class PwmServoEx:
    def __init__(self):
        self.led_pin = 25

        GPIO.setup(self.led_pin, GPIO.OUT)
        self.servo = GPIO.PWM(self.led_pin, 50)
        self.servo.start(0)

    def __call__(self):
        try:
            while 1:
                # 듀티비를 변경하여 서보모터를 원하는 만큼 움직임
                self.servo.ChangeDutyCycle(7.5) # 90도
                time.sleep(1)
                self.servo.ChangeDutyCycle(12.5) # 180도
                time.sleep(1)
                self.servo.ChangeDutyCycle(2.5) # 0도
                time.sleep(1)
        
        except KeyboardInterrupt: # 키보드 Ctrl+C 눌렀을 때 예외발생
            self.servo.stop() # PWM을 종료