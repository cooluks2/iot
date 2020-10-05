from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

# Camera warm-up time
sleep(2)
camera.capture('foo.jpg') # 저장할 파일명 지정, 파일 확장명으로 포맷 결정