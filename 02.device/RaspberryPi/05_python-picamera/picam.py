import time
from picamera import PiCamera
import numpy as np
import cv2

class PiCam:
    def __init__(self, show=False, framerate=25, width=640, height=480):
        self.size = (width, height)
        self.show = show
        self.framerate = framerate

    def run(self, callback):
        camera = PiCamera()
        camera.rotation = 180
        camera.resolution = self.size
        camera.framerate = self.framerate
        output = np.empty((self.size[1], self.size[0], 3), dtype=np.uint8)

        while True:
            camera.capture(output, 'bgr', use_video_port=True)
            cv2.imshow('frame', output)
            if callback(output) == False: break

            if self.show:
                cv2.imshow('frame', output)
                key = cv2.waitKey(1)
                if key == 27: break

        cv2.destroyAllWindows()
