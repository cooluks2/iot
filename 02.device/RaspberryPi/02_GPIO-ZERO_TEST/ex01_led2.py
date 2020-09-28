from gpiozero import LED
from signal import pause

red = LED(18)

red.blink()

pause()
print("end...")