from picamera import PiCamera
import numpy as np

with PiCamera() as camera:
    camera.resolution = (100, 100)
    camera.framerate = 24
    time.sleep(2)

    output = np.empty((112 * 128 * 3,), dtype=np.uint8)
    camera.capture(output, 'rgb')
    
    output = output.reshape((112, 128, 3))
    output = output[:100, :100, :]