# picamera 라이브러리 임포트
import picamera

# time 라이브러리 임포트
import time

# PiCamera 객체 인스턴스 생성
with picamera.PiCamera() as camera:

    camera.start_preview()

    for i in range(5):
        time.sleep(5)
        camera.capture(format('/home/pi/workspace/05_python-picamera/image{str}.jpg', i))
        
    camera.stop_preview()
