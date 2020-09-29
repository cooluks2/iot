# python-picamera 이미지 프로세싱

### numpy 배열에 저장하기

-   camera.capture(numpy배열, '이미지포맷')
    -   numpy 배열의 공간이 확보되야 함
    -   이미지 포맷
        -   rgb
        -   bgr (OpenCV)

<br>

**numpy 배열에 저장하기**

picam_processing_ex01.py

```python
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
        camera.capture(output, 'bgr')
        cv2.imshow('frame', output)
        key = cv2.waitKey(40)
        if key == 27 :
            break

    cv2.destroyAllWindows()

```

>   VNC에서도 볼 수 있다.

<br>

**numpy 배열로 슬라이싱(크롭)**

picam_processing_ex02.py

```python
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
```

<br>

**OpenCV 객체로 캡처하기**

picam_processing_ex03.py

```python
import time
from picamera import PiCamera
import numpy as np
import cv2

with PiCamera() as camera:
    camera.resolution = (320, 240)
    camera.framerate = 24
    time.sleep(2)
    
    image = np.empty((240 * 320 * 3,), dtype=np.uint8)
    camera.capture(image, 'bgr')
    image = image.reshape((240, 320, 3))
```

<br>

**Unencoded image capture (RGB format)**

picam_processing_ex04.py

```python
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (100, 100)
    camera.start_preview()
    time.sleep(2)
    
    camera.capture('image.data', 'rgb')
```

picam_processing_ex05.py

```python
import time
import picamera
import picamera.array
import numpy as np

with picamera.PiCamera() as camera:
    camera.resolution = (100, 100)
    time.sleep(2)

    image = np.empty((128, 112, 3), dtype=np.uint8)
    camera.capture(image, 'rgb')
    
    image = image[:100, :100]
```

<br>

### Custom outputs

-   file-like object
    -   write(self, data)
    -   flush(self)

<br>

**Custom outputs**

picam_processing_ex06.py

```python
import picamera

class MyOutput(object):
    def __init__(self):
        self.size = 0
    def write(self, s):
        self.size += len(s)
    def flush(self):
        print('%d bytes would have been written' % self.size)

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.framerate = 60
    
    camera.start_recording(MyOutput(), format='h264')
    camera.wait_recording(10)
    camera.stop_recording()
```

<br>

### 개선하기

-   picamera.array 모듈
    -   numpy로 배열로 커스텀 출력(output) 처리 지원
-   PiMotionAnalysis 클래스
    -   앞 코드의 여러 골격을 간소화 지원

>   넘어감

<br>

<br>

### 빠른 캡처와 프로세싱

-   JPEG 인코더를 이용한 빠른 jpg 이미지 캡처
-   use_video_port 파라미터 설정(True)
    -   비디오 녹화 영역만 캡처

<br>

**빠른 캡처**

picam_processing_ex07.py

```python
import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1024, 768)
    camera.framerate = 30
    camera.start_preview()
    time.sleep(2)
    camera.capture_sequence([
        'image1.jpg',
        'image2.jpg',
        'image3.jpg',
        'image4.jpg',
        'image5.jpg',
        ], use_video_port=True)
```

>   캡처 속도가 10배 정도 빨라진다. 하드웨어 지원
>   1번 예제에서도 use_video_port=Ture 추가하면 끊김없는 캡처 사용할수 있다.

<br>

<br>

### 이미지 프로세싱 + 얼굴 인식

picam.py

```python
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

```

facedetect.py

```python
import numpy as np
from picam import PiCam
import cv2

FACE_WIDTH = 200
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_image = np.array((FACE_WIDTH, FACE_WIDTH,3), dtype=int)

def detect_face(frame):
    global face_image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        minLength = min(w, h)
        if minLength < 150: break
        width = max(w, h)
        x = x + w//2 - width//2
        y = y + h//2 - width//2
        face_image = frame[y:y+width, x:x+width].copy()
        cv2.rectangle(frame,(x,y),(x+width,y+width),(255,0,0),2)

        face_image = cv2.resize(face_image, dsize=(FACE_WIDTH, FACE_WIDTH), interpolation=cv2.INTER_AREA)

    
    frame[0:FACE_WIDTH, 0:FACE_WIDTH] = face_image[:] # 좌측 상단에 출력
    
    return True


c = PiCam(show = True)
c.run(detect_face)
```

<br>

