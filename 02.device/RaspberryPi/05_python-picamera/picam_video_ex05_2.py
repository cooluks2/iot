from gpiozero import DistanceSensor
import io
import random
from picamera import PiCamera, PiCameraCircularIO

sensor = DistanceSensor(23, 24)

def motion_detected():
    return sensor.distance <= 0.2

camera = PiCamera()
stream = PiCameraCircularIO(camera, seconds=20)

camera.start_recording(stream, format='h264')
try:
    while True:
        camera.wait_recording(1)
        if motion_detected():
            print('motion detected')
            camera.start_preview()
            # 동작이 감지됬다면 10초간 녹화하여 디스크에 스트림을 기록
            camera.wait_recording(10)
            camera.stop_preview()
            stream.copy_to('motion.h264') # 스트림을 파일로 저장하기
finally:
	camera.stop_recording()