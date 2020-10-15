import cv2
import io
import time
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera

class PiCam:
    def __init__(self, show=True, framerate=25, width=640, height=480):
        self.size = (width, height)
        self.show = show
        self.framerate = framerate

        self.camera = PiCamera()
        self.camera.rotation = 180
        self.camera.resolution = self.size
        self.camera.framerate = self.framerate


    def snapshot(self):
        frame = io.BytesIO()
        self.camera.capture(frame, 'jpeg',use_video_port=True)
        frame.seek(0)
        return frame.getvalue()


class MJpegStreamCam(PiCam):
    def __init__(self, show=True, framerate=25, width=640, height=480):
        super().__init__(show=show, framerate=framerate, width=width, height=height)

    def __iter__(self): 
        frame = io.BytesIO()
        while True:
            self.camera.capture(frame, 'jpeg',use_video_port=True)
            image = frame.getvalue()
            yield (
                b'--myboundary\n'
                b'Content-Type:image/jpeg\n'
                b'Content-Length: ' + f"{len(image)}".encode() + b'\n'
                b'\n' + image + b'\n')
            frame.seek(0)  # 읽기 쓰기 위치를 맨 앞으로 (기존 데이터 남아있음)