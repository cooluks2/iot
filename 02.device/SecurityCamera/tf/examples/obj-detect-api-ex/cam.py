import cv2

class USBCam:
    def __init__(self, show=False, framerate=25, width=640, height=480):
        self.size = (width, height)
        self.show = show
        self.framerate = framerate

    def __iter__(self):
        self.cap = cv2.VideoCapture(0) # 0번 카메라
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size[1])
        
        while True:
            retval, frame = self.cap.read() # 프레임 캡처
            yield frame

    def run(self, callback):
        # self.cap = cv2.VideoCapture(0) # 0번 카메라
        self.cap = cv2.VideoCapture("http://192.168.0.10:8000/mjpeg/stream/")
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.size[0])
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.size[1])
        
        while True:
            retval, frame = self.cap.read() # 프레임 캡처
            if not retval: break
            if not callback(frame): break
            
            if self.show:
                cv2.imshow('frame', frame)
                key = cv2.waitKey(self.framerate)
                if key == 27: break

        if self.cap.isOpened():
            self.cap.release()