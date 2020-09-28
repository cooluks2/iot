from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(18, 23, 24)

# 모두 같이 동작
leds.on()
sleep(1)
leds.off()
sleep(1)

# 개별적인 값을 튜플로 지정
leds.value = (1, 0, 1)
sleep(1)
leds.blink()
pause()