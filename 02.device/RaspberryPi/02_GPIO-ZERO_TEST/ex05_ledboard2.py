from gpiozero import LEDBoard
from signal import pause

leds = LEDBoard(18, 23, 24, pwm=True)

leds.value = (0.2, 0.4, 0.6)

pause()