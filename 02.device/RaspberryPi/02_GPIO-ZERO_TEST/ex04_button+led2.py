from gpiozero import LED, Button
from signal import pause

led = LED(23)
button = Button(18)

led.source = button.values

pause()