import cv2

from cam import USBCam

c = USBCam() # USBCam(show=True)

def capture(frame):
    # frame 처리
    cv2.imshow('frame', frame)
    key = cv2.waitKey(25)
    if key == 27: return False
    return True
    
c.run(capture)