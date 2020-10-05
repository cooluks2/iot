from time import sleep
from picamera import PiCamera

# Explicitly open a new file called my_image.jpg
my_file = open('my_image.jpg', 'wb')

camera = PiCamera()
camera.start_preview()
sleep(2)

camera.capture(my_file)