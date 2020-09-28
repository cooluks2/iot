import RPi.GPIO as GPIO
import time

# callable class
class BtnEventEx:
    def __init__(self):
        self.button_pin = 16
        self.led_pin = 18

        GPIO.setup(self.button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.led_pin, GPIO.OUT)

        self.light_on = False

    # button_callback 함수를 정의합니다.
    def button_callback(self, channel):
        if self.light_on == False: # LED 불이 꺼져있을때
            GPIO.output(self.led_pin,1) # LED ON
            print("LED ON!")
        else: # LED 불이 져있을때
            GPIO.output(self.led_pin,0) # LED OFF
            print("LED OFF!")
        self.light_on = not self.light_on # False <=> True
    

    def __call__(self):
        self.light_on = False
        GPIO.add_event_detect(self.button_pin,GPIO.RISING, callback=self.button_callback, bouncetime=300)

        try:
            while 1: #무한반복
                time.sleep(0.1) # 0.1초 딜레이
        except KeyboardInterrupt:
            GPIO.remove_event_detect(self.button_pin)


if __name__ == "__main__":
    ex = BtnEventEx()
    ex()