import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)

    output = np.empty((240, 320, 3), dtype=np.uint8)
    # camera.capture(output, 'rgb')

    while True:
        camera.capture(output, 'bgr', use_video_port=Ture)
        cv2.imshow('frame', output)
        key = cv2.waitKey(40)
        if key == 27 :
            break

    cv2.destroyAllWindows()
